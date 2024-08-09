#encoding UTF-8
#errorCatcher Echo
#*
    Almanac JSON data
*#
#set $daylight = $almanac.sun.set.raw - $almanac.sun.rise.raw
    "almanac": {
        "sun": {
            "rise": #echo $almanac.sun.rise.raw*1000#,
            "transit": #echo $almanac.sun.transit.raw*1000#,
            "set": #echo $almanac.sun.set.raw*1000#,
            "daylight": $daylight,
            "antitransit": {
                "previous": #echo $almanac.sun.previous_antitransit.raw*1000#,
                "next": #echo $almanac.sun.next_antitransit.raw*1000#
            }
        },
        "moon": {
            "rise": #echo $almanac.moon.rise.raw*1000#,
            "set": #echo $almanac.moon.set.raw*1000#,
            "phase": "$almanac.moon_phase",
            "percentfull": "$almanac.moon_fullness",
            "index": "$almanac.moon_index",
            "antitransit": {
                "previous": #echo $almanac.moon.previous_antitransit.raw*1000#,
                "next": #echo $almanac.moon.next_antitransit.raw*1000#
            },
            "new": {
                "previous": #echo $almanac.previous_new_moon.raw*1000#,
                "next": #echo $almanac.next_new_moon.raw*1000#
            },
            "full": {
                "previous": #echo $almanac.previous_full_moon.raw*1000#,
                "next": #echo $almanac.next_full_moon.raw*1000#
            }
        }
    }
