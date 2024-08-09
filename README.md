# OBWX
*Olive Branch Weather*

*A skin/theme extension for [weewx](http://www.weewx.com) weather software*

## Description
OBWX displays weather information using data generated from the weewx 
weather system and Aeris Weather's API. It is designed to be used as a
weather console using a web browser's full-screen option and displayed on a 
standard 16:9 panel (monitor or TV).
I use a 14" monitor powered by a raspberry pi for an 'always on' weather console in the kitchen.

OBWX also dynamically adjusts to display your weather on mobile devices.

***Note: Aeris Weather is now [Vaisala Xweather](https://www.xweather.com/weather-api)***

![Capture](https://user-images.githubusercontent.com/116417003/222556565-7beb0513-def3-4818-a713-f74a556e21eb.PNG)

## Prerequisites
* weewx weather software
* mqtt extension (e.g., weewx-mqtt)
* mqtt broker (e.g., mosquitto)
* Aeries Weather account for forecast, alerts, and other observations
* Modern web-broswer that supports HTML5 (Firefox, Chrome, etc.)
* web server software (optional) (e.g., nginx)

## Installation
- Install the prerequisites
- Install OBWX
    * weewx 5.0+ versions

          weectl extension install https://github.com/stormchasertech/obwx/archive/main.zip

    * weewx 4 versions
        + Download the zip file

               wget -O obwx.zip https://github.com/stormchasertech/obwx/archive/main.zip
        + Run the installer

               wee_extension --install obwx.zip

- Configure OBWX options by editing the [StdReport] [[OBWX]] section that was added to weewx.conf
- Restart weewx
  
### Use as a weather display
- Open the generated 'obwx/index.html' page in a web browser
- Press 'F11' to enter Full screen mode
- Zoom in (CTRL++) or zoom out (CTRL+-) to adjust as needed

## OBWX options
### HTML settings
| Setting    | Description |
| ---------- | ------------ |
| html_title | Browser window title |
| logo_img   | Relative path to the logo image file |
| logo_title | Alt. text to display when logo image is not available/desired |

### Aries Weather API settings
| Setting            | Description |
| ------------------ | ----------- |
| api_id             | Your API id |
| api_secret         | Your API secret |
| api_call_frequency | How often the API is queried |

### Web-socket settings
| Setting          | Description |
| ---------------- | ------------ |
| websocket_host | IP/domain name of websocket server |
| websocket_port | port number of websocket server |
| websocket_topic | mqtt topic to listen subcribe to |
| websocketHasPassword | True/False - Enable if websocket data uses a password (default=False) |

### Other settings
| Setting          | Description |
| ---------------- | ------------ |
| metar_id_1       | Primary METAR station ID (example: KOLV) |
| metar_id_2       | Fallback METAR station ID |
| timezone         | All times are converted to this timezone  |

If the 'timezone' setting is left 'undefined', the web browser will make timezone decisions based on browser location. 
Valid timezones are listed in timezones.html
Example: timezone = America/Chicago

### Theme settings
| Setting          | Description |
| ---------------- | ------------ |
| color            | general text color |
| background_color | site background color |
| border_color     | site border color|

Takes #hex, rgb, or any other valid css values
Example: background_color = "rgb(0,0,0)"

