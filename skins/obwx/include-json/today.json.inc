#encoding UTF-8
#errorCatcher Echo
#*
    Daily Observations and Records JSON data
*#
    "today": {
        "outTemp": {
            "max": "$day.outTemp.max",
            "min": "$day.outTemp.min",
            "maxtime": #echo $day.outTemp.maxtime.raw*1000#,
            "mintime": #echo $day.outTemp.mintime.raw*1000#
        },
        "dewpoint": {
            "max": "$day.dewpoint.max",
            "min": "$day.dewpoint.min",
            "maxtime": #echo $day.dewpoint.maxtime.raw*1000#,
            "mintime": #echo $day.dewpoint.mintime.raw*1000#
        },
        "wind": {
            "max": "$day.wind.max.format(format_string='%.1f',add_label=False)",
            "min": "$day.wind.min.format(add_label=False)",
            "maxtime": #echo $day.wind.maxtime.raw*1000#,
            "mintime": #echo $day.wind.mintime.raw*1000#,
            "windSpd_20minMax": "$span($time_delta=1200).windGust.max.format(add_label=False)",
            "windSpd_20minAvg": "$span($time_delta=1200).windSpeed.avg",
            "windDir_20minAvg": "$span($time_delta=1200).wind.vecdir.ordinal_compass"
        },
        "barometer": {
            "trend":"$trend.barometer.format(format_string='%.2f',add_label=False)",
            "max": "$day.barometer.max.format(format_string='%.2f',add_label=False)",
            "min": "$day.barometer.min.format(format_string='%.2f',add_label=False)",
            "maxtime": #echo $day.barometer.maxtime.raw*1000#,
            "mintime": #echo $day.barometer.mintime.raw*1000#
        },
        "rain": {
            "maxRate": "$day.rainRate.max",
            "maxRateTime": #echo $day.rainRate.maxtime.raw*1000#,
            "sum": {
                "today": "$day.rain.sum",
                "yesterday": "$yesterday.rain.sum",
                "week": "$span($week_delta=1).rain.sum",
                "month": "$month.rain.sum",
                "year": "$year.rain.sum"
            }
        }
    }
