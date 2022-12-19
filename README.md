# OBWX
*Olive Branch Weather*

*A skin/theme extension for [weewx](http://www.weewx.com) weather software*

## Description
OBWX generates html, javascript, css, and json files to display live weather
conditions, forecasts, and other observations.

### Goals
The goal of this project is to provide a direct replacement of the
weather console that is shipped with commercial personal weather stations.
In my experience these consoles will lose their data when the batteries die,
they do not provide the data I desire, and generally have a sub-par quality to them.

To be honest, I would rather these companies put the development money into the sensors
themselves so that we can have the most accurate measurements we can get for the money, so please
do not take these criticisms as something that needs to be addressed per se. That is where the weewx
developers, folks like Belchertown developers, and myself come into play!

### Example
As an example, my current OBWX display is using a 14" portable monitor with a raspberry pi zero wireless
providing the CPU power to run the display. Previously it was displayed on a 10" monitor,
which is a good size for the display. I will add some screenshots/pictures soon.

It also displays nicely on laptops, and is built using Bootstrap 5 to provide cell phone / tablet functionality. 

### Status
OBWX has changed in scope a few times during its implementation, firstly as a personal (unpublished) add-on 
to the Belchertown skin, and now as its own stand-alone extention to weewx.
OBWX is still in development, and will eventually have a release version.
Current work includes:

1) Changing css based graphics to HTML5 Canvas drawings and animation
    * Re-designing the wind section using HTML5 Canvas
    * Re-designing the Rain section using HTML5 Canvas
    * Adding HTML5 canvas animation for almanac sun and moon
2) Add "extra sensors" table
3) Add/rework daily/weekly records table/section

### Prerequisites
* weewx weather software
* mqtt extension
* web server 
* mqtt broker
* Aeries Weather account for forecast, alerts, and other observations

#### Acknowledgments
Outside of a couple of minor websites, this could be considered my first large coding project and it has been
an extremely fun and challenging journey. From learning linux, javascript, and a touch of python ... 
this project continues to enhanced my skill set which I can apply to 
my other personal and professional projects. I need to mention the Belchertown skin as I have
used that extension as a learning platform and it provided lots of insperation for this project. Thanks!!

More to come!!

![obwx_current(small)](https://user-images.githubusercontent.com/116417003/208509364-560b3c28-fcfd-4604-a8e0-4c3a3683a616.PNG)

![obwx(small)](https://user-images.githubusercontent.com/116417003/208509492-5cf0b30d-d955-4058-996a-060f51b9a92e.PNG)


