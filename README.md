# OBWX
*Skin extension for [weewx](http://www.weewx.com) weather software*

## Description

OBwx generates html, javascript, css, and json files to display live weather 
conditions, forecasts, and other obeservations.

### Goals

The goal of this project is to provide a direct replacement of the 
weather console that is shipped with commercial personal weather stations.
In my experiance these consoles will loose their data when the batteries die, 
they do not provide the data I desire, and generally have a sub-par quality to them. 

To be honest, I would rather these companies put the development money into the sensors
themselves so that we can have the most accurate measurements we can get for the money, so please 
do not take these critisisms as something that needs to be addressed per say. That is where the weewx
developers, folks like Belchertown developers, and myself come into play! 

#### Secondary Goals
This is my first big coding project and it has been an extremely fun and challenging journey. From learning linux, 
javascript, and a touch of python ... this project has enhanced my skill set which to use in my personal and professional projects.
I need to mention the Belchertown skin as I have used that extension as a learning platform to s

### Example

As an example, my current OBwx console is using a 14" portable monitor with a raspberry pi zero wireless
providing CPU power to run the display. I will add some screenshots/pictures soon.


### Status

OBwx has changed in scope a few times during its implementation, and is still in development. Evenutally
a version will be make that will be released. Current work includes:

1) Changing css based graphics to HTML5 Canvas drawings and animation
* Re-designing the wind section using HTML5 Canvas
* Re-designing the Rain section using HTML5 Canvas
* Adding HTML5 canvas animation for almanac sun and moon 

2) Add "extra sensors" table
3) Add daily/weekly records table/section

### Prerequesets

weewx
mqtt extension
webserver (which can be local only)
Aeries weather account for forecast, aleart, and other observations
