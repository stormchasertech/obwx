#encoding UTF-8
#errorCatcher Echo
#*
    Station JSON data
*#
    "station": {
        "latitude": "$station.stn_info.latitude_f",
        "longitude": "$station.stn_info.longitude_f",
        "altitude": "$station.altitude",
        "serveruptime": "$station.os_uptime"
    }
