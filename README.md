# OBWX
*Olive Branch Weather*

*A skin/theme extension for [weewx](http://www.weewx.com) weather software*

## Description
OBWX displays weather information using data generated from the weewx weather system and Aeris Weather's API. It is designed to be an alternate weather console using a web browser's full-screen option and displayed on a standard 16:9 panel (monitor or TV). Think of a laptop screen or portable monitor. 


 Put a picture here


### Status
OBWX is still in development, and will eventually have a release version.
* Live updates using using mqtt web-sockets is a requirement. It does not update with archive packets, however that functionality is planned.

### Prerequisites
* weewx weather software
* mqtt extension
* mqtt broker
* Aeries Weather account for forecast, alerts, and other observations

### Some skin.conf options explained
Aeris Weather api settings
* api_id
* api_secret
* api_call_frequency (in seconds)

Set these to the desired metar Station ID to display. 'KOLV' for example.
If option 1 is down, option 2 will take over.
* metar_id_1
* metar_id_1


More to come!!
