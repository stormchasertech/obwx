"""
OBWX custom weather display extention to weewx

"""
import json
import datetime
import time

from weewx.cheetahgenerator import SearchList
from weewx.tags import TimespanBinder
from weeutil.weeutil import TimeSpan

# https://github.com/weewx/weewx/wiki/WeeWX-v4-and-logging
import weeutil.logger
import logging
log = logging.getLogger(__name__)

def logdbg(msg):
    log.debug(msg)

def loginf(msg):
    log.info(msg)

def logerr(msg):
    log.error(msg)

VERSION = "OBWX V.10"
loginf("%s enabled" % VERSION)

# https://www.weewx.com/docs/sle.html
class getForecast(SearchList):

    def __init__(self, generator):
        SearchList.__init__(self, generator)

    # Hook into weewx engine, and get stuff done
    def get_extension_list(self, timespan, db_lookup):

        ##########################################
        ## Download API data into forecast.json ##
        ##########################################

        # Set the path and other prep
        from pathlib import Path
        forecast_file = Path( self.generator.config_dict['WEEWX_ROOT'] , self.generator.config_dict['StdReport']['OBWX']['HTML_ROOT'] , 'forecast.json' )
        forecast_update_needed = False

        # Check if forecast file exists
        if forecast_file.is_file():
            #File exists, now get how old it's data is using last modified time
            forecast_age = time.time() - forecast_file.stat().st_mtime
            
            if int(forecast_age) > int(self.generator.skin_dict['Extras']['api_call_freqency']):
                # File has old data, lets update it
                forecast_update_needed = True

        else:
            #File doesnt exit, lets make a new one
            forecast_update_needed = True

        # Update/create forecast file 
        if forecast_update_needed:

            ## Prep for API requests
            from urllib.request import Request, urlopen

            latitude = self.generator.config_dict['Station']['latitude']
            longitude =  self.generator.config_dict['Station']['longitude']
            api_id = self.generator.skin_dict['Extras']['api_id']
            api_secret = self.generator.skin_dict['Extras']['api_secret']

            current_url = "https://api.aerisapi.com/conditions/%s,%s?format=json&plimit=1&filter=1min&client_id=%s&client_secret=%s" % ( latitude, longitude, api_id, api_secret ) 
            observations_url = "https://api.aerisapi.com/observations/%s,%s?format=json&filter=metar&limit=4&client_id=%s&client_secret=%s" % ( latitude, longitude, api_id, api_secret )
            daynight_url = "https://api.aerisapi.com/forecasts/%s,%s?format=json&filter=daynight&limit=6&client_id=%s&client_secret=%s" % ( latitude, longitude, api_id, api_secret )
            alerts_url = "https://api.aerisapi.com/alerts/%s,%s?format=json&limit=5&client_id=%s&client_secret=%s" % ( latitude, longitude, api_id, api_secret )

            user_agent = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3"
            headers = {"User-Agent": user_agent}
        
            ## Make the API requests
            req = Request(current_url, None, headers)
            response = urlopen(req)
            current_page = response.read()
            response.close

            req = Request(observations_url, None, headers)
            response = urlopen(req)
            observations_page = response.read()
            response.close

            req = Request(daynight_url, None, headers)
            response = urlopen(req)
            daynight_page = response.read()
            response.close

            req = Request(alerts_url, None, headers)
            response = urlopen(req)
            alerts_page = response.read()
            response.close

            ## Combine the json information 
            forecast_file_result = json.dumps(
                {
                    "timestamp" : int(time.time()),
                    "current" : [json.loads(current_page)],
                    "observations" : [json.loads(observations_page)],
                    "daynight" : [json.loads(daynight_page)],
                    "alerts" : [json.loads(alerts_page)],
                },
            )

            ## Write the json information to file
            try:
                with open(forecast_file, "w+") as file:
                    file.write(forecast_file_result)
                loginf("Forecast file updated")
            except Exception:
                logerr("Forecast file NOT updated")

        else:
            logdbg('Forecast file generation skipped')

        # From weewx documentaion
        all_stats = TimespanBinder(
            timespan,
            db_lookup,
            formatter=self.generator.formatter,
            converter=self.generator.converter,
            skin_dict=self.generator.skin_dict,
        )

        #Explore this more, looks like it makes variables available for use in the skin
        search_list_extension = {
            "obwx_version" : VERSION,
            "alltime" : all_stats,
        }

        # Return the list
        return [search_list_extension]
