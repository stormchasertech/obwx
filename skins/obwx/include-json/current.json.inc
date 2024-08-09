#encoding UTF-8
#errorCatcher Echo
#*
    Check if an observation is present
*#
#def setObs($obs, $val)
  #if $val
  "$obs": $val,
  #end if
#end def
#*
    Current observations JSON data
*#
    "current": {
        $setObs("UV",$current.UV.raw)
        $setObs("appTemp_F", $current.appTemp.raw)
        $setObs("barometer_inHg", $current.barometer.raw)
        $setObs("dewpoint_F", $current.dewpoint.raw)
        $setObs("inHumidity", $current.inHumidity.raw)
        $setObs("inTemp_F", $current.inTemp.raw)
        $setObs("outTemp_F", $current.outTemp.raw)
        $setObs("outHumidity", $current.outHumidity.raw)
        $setObs("dayRain_in", $day.rain.sum.raw)
        $setObs("rainRate_inch_per_hour", $current.rainRate.raw)
        $setObs("windDir", $current.windDir.raw)
        $setObs("windGust_mph", $current.windGust.raw)
        $setObs("windSpeed_mph", $current.windSpeed.raw)
        "dateTime": $current.dateTime.raw
    }
