"""
OBWX custom weather display extention to weewx
Gets JSON data from Aires weather API
"""
import json
import time
import logging
import weewx
from weewx.engine import StdService
from pathlib import Path
from urllib.request import Request, urlopen

log = logging.getLogger(__name__)

class GetAerisForecast(StdService):
    def __init__(self, engine, config_dict):
        super(GetAerisForecast, self).__init__(engine, config_dict)

        self.obwx_dict = config_dict.get('StdReport', {}).get('OBWX').get('Extras')
        self.forecast_file = Path( config_dict['WEEWX_ROOT'] , config_dict['StdReport']['OBWX']['HTML_ROOT'] , 'forecast.json' )
        self.latitude = config_dict['Station']['latitude']
        self.longitude = config_dict['Station']['longitude']
        self.api_call_frequency = self.obwx_dict.get('api_call_frequency')
        self.api_id = self.obwx_dict.get('api_id')
        self.api_secret = self.obwx_dict.get('api_secret')
        self.current_url = 'https://api.aerisapi.com/conditions/%s,%s?format=json&plimit=1&filter=1min&client_id=%s&client_secret=%s' % ( self.latitude, self.longitude, self.api_id, self.api_secret )
        self.observations_url = 'https://api.aerisapi.com/observations/%s,%s?format=json&filter=metar&limit=4&client_id=%s&client_secret=%s' % ( self.latitude, self.longitude, self.api_id, self.api_secret )
        self.daynight_url = 'https://api.aerisapi.com/forecasts/%s,%s?format=json&filter=daynight&limit=6&client_id=%s&client_secret=%s' % ( self.latitude, self.longitude, self.api_id, self.api_secret )
        self.alerts_url = 'https://api.aerisapi.com/alerts/%s,%s?format=json&limit=5&fields=details.name,details.color,details.body,timestamps.beginsISO,timestamps.expiresISO&client_id=%s&client_secret=%s' % ( self.latitude, self.longitude, self.api_id, self.api_secret )
        self.user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
        self.headers = {'User-Agent': self.user_agent}

        log.info('OBWX initialized')

        self.bind(weewx.NEW_ARCHIVE_RECORD, self.update_aeris_data)

    def fetch_aeris_data (self, url):
            req = Request(url, None, self.headers)
            response = urlopen(req)
            page = response.read()
            response.close
            return page

    def update_aeris_data (self, event):

        forecast_update_needed = False

        # Check if forecast file exists
        if self.forecast_file.is_file():
            #File exists, now get how old it's data is using last modified time
            forecast_age = time.time() - self.forecast_file.stat().st_mtime
            
            if int(forecast_age) > int(self.api_call_frequency):
                # File has old data, lets update it
                forecast_update_needed = True

        else:
            #File doesnt exit, lets make a new one
            forecast_update_needed = True

        # Update/create forecast file 
        if forecast_update_needed:

            try:
                # Get current conditions
                current_page = self.fetch_aeris_data (self.current_url)
                # Get METAR observations
                observations_page = self.fetch_aeris_data (self.observations_url)
                # Get Forecast data
                daynight_page = self.fetch_aeris_data (self.daynight_url)
                # Get Alerts data
                alerts_page = self.fetch_aeris_data (self.alerts_url)

            except Exception:
                log.warning('Error fetching Aeris Weather data')

            else:
                ## Combine the json information 
                forecast_file_result = json.dumps(
                    {
                        'timestamp' : int(time.time()),
                        'current' : [json.loads(current_page)],
                        'observations' : [json.loads(observations_page)],
                        'daynight' : [json.loads(daynight_page)],
                        'alerts' : [json.loads(alerts_page)],
                    },
                )

                ## Write the json information to file
                try:
                    with open(self.forecast_file, 'w+') as file:
                        file.write(forecast_file_result)

                    log.info('Aeris weather data has been updated')

                except Exception:
                    log.warning('Error writing Aeris data file')

        else:
            log.info('Aeris update skipped')
