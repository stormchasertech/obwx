# OBWX
*Olive Branch Weather*

*A skin/theme extension for [weewx](http://www.weewx.com) weather software*

## Description
OBWX displays weather information using data generated from the weewx 
weather system and Aeris Weather's API. It is designed to be an alternate 
weather console using a web browser's full-screen option and displayed on a 
standard 16:9 panel (monitor or TV). Think of a laptop screen or portable monitor. 


![Capture](https://user-images.githubusercontent.com/116417003/222556565-7beb0513-def3-4818-a713-f74a556e21eb.PNG)


### Status
OBWX is still in development, and will eventually have a release version.
* Currently, most data has been added. Continue working general layout.
* Next, begin refining placement/layout of elements/graphics.

### Prerequisites
* weewx weather software
* mqtt extension
* mqtt broker
* Aeries Weather account for forecast, alerts, and other observations
* Modern web-broswer that supports HTML5

### Some skin.conf options explained
Aeris Weather api settings
* api_id
* api_secret
* api_call_frequency (in seconds)

Set these to the desired metar Station ID to display. 'KOLV' for example.
If option 1 is down, option 2 will take over.
* metar_id_1
* metar_id_2

All times are converted to this timezone. If it is left undefined, 
the web browser will make timezone decisions based on browser location data. 
This seems to be a [up-to-date listing](https://github.com/vvo/tzdb/blob/main/time-zones-names.json) of valid timezone names
* timezone (Example: timezone = America/Chicago)


More to come!!
