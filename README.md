# OBWX
*Olive Branch Weather*

*A skin/theme extension for [weewx](http://www.weewx.com) weather software*

## Description
OBWX displays weather information using data generated from the weewx weather system and Aeris Weather's API. It is designed to be an alternate weather console using a web browser's full-screen option and displayed on a standard 16:9 panel (monitor or TV). Think of a laptop screen or portable monitor. 


 ![Capture](https://user-images.githubusercontent.com/116417003/222553391-8f729d2c-4d13-42ea-9a1a-9961103cff51.PNG)


### Status
OBWX is still in development, and will eventually have a release version.
* Live updates using mqtt web-sockets is a requirement.

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


More to come!!
