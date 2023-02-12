from weecfg.extension import ExtensionInstaller

def loader():
    return OBWX_Installer()

class OBWX_Installer(ExtensionInstaller):
    def __init__(self):
        super(OBWX_Installer, self).__init__(
            version='0.30',
            name='obwx',
            description='Weather Data Console',
            author=StormchaserTech,
            author_email=stormchaserlitofb@gmail.com,
            data_services='user.obwx.GetAerisForecast',
            config={
                'StdReport': {
                    'OBWX': {
                        'skin': 'obwx',
                        'HTML_ROOT' : 'obwx',
                        'enable': True,
                        'Extras' : {
                            'logo_img' : 'logo.png',
                            'logo_title' : 'Site Title',
                            'logo_alt' : 'Site Alt',
                            'api_id' : '',
                            'api_secret' : '',
                            'api_call_frequency' : '240',
                            'websocket_enable' : '',
                            'websocket_host' : '',
                            'websocket_port' : '8080',
                            'websocket_topic' : '',
                            'metar_id_1' : '',
                            'metar_id_2' : '',
                            'timezone' : 'undefined',
                        }
                    }
                }
            },
            files=[('bin/user', ['bin/user/obwx.py']),
                ('skins/obwx',
                    [
                    'skins/obwx/skin.conf',
                    'skins/obwx/index.html.tmpl',
                    'skins/obwx/obwx.css',
                    'skins/obwx/obwx.js.tmpl',
                    ]
                ),
                ('skins/obwx/icons',
                    [
                    'skins/obwx/icons/mcloudytn@2x.png',
                    'skins/obwx/icons/showersw@2x.png',
                    'skins/obwx/icons/pcloudywn.png',
                    'skins/obwx/icons/snowshowersw.png',
                    'skins/obwx/icons/sunnyn.png',
                    'skins/obwx/icons/pcloudysn@2x.png',
                    'skins/obwx/icons/mcloudys@2x.png',
                    'skins/obwx/icons/cold@2x.png',
                    'skins/obwx/icons/mcloudyr.png',
                    'skins/obwx/icons/snowshowersn.png',
                    'skins/obwx/icons/sleetsnown@2x.png',
                    'skins/obwx/icons/tstormn.png',
                    'skins/obwx/icons/showers.png',
                    'skins/obwx/icons/pcloudyrw@2x.png',
                    'skins/obwx/icons/blowingsnown@2x.png',
                    'skins/obwx/icons/mcloudysfwn.png',
                    'skins/obwx/icons/wintrymix.png',
                    'skins/obwx/icons/freezingrainn@2x.png',
                    'skins/obwx/icons/showersn@2x.png',
                    'skins/obwx/icons/sunny.png',
                    'skins/obwx/icons/pcloudyr@2x.png',
                    'skins/obwx/icons/dust.png',
                    'skins/obwx/icons/mcloudytwn.png',
                    'skins/obwx/icons/mcloudysfw.png',
                    'skins/obwx/icons/pcloudysfw@2x.png',
                    'skins/obwx/icons/rain.png',
                    'skins/obwx/icons/mcloudyrn@2x.png',
                    'skins/obwx/icons/drizzlef@2x.png',
                    'skins/obwx/icons/hazyn@2x.png',
                    'skins/obwx/icons/hazy@2x.png',
                    'skins/obwx/icons/raintosnown.png',
                    'skins/obwx/icons/flurriesn.png',
                    'skins/obwx/icons/blizzardn.png',
                    'skins/obwx/icons/fogn.png',
                    'skins/obwx/icons/pcloudyw.png',
                    'skins/obwx/icons/pcloudytw.png',
                    'skins/obwx/icons/showersw.png',
                    'skins/obwx/icons/cloudyn.png',
                    'skins/obwx/icons/clearn@2x.png',
                    'skins/obwx/icons/sleet@2x.png',
                    'skins/obwx/icons/tstorm.png',
                    'skins/obwx/icons/raintosnown@2x.png',
                    'skins/obwx/icons/mcloudy.png',
                    'skins/obwx/icons/mcloudyn@2x.png',
                    'skins/obwx/icons/snowshowers.png',
                    'skins/obwx/icons/freezingrain.png',
                    'skins/obwx/icons/pcloudysf.png',
                    'skins/obwx/icons/snown@2x.png',
                    'skins/obwx/icons/sleetsnow.png',
                    'skins/obwx/icons/sunnywn.png',
                    'skins/obwx/icons/mcloudy@2x.png',
                    'skins/obwx/icons/pcloudytwn@2x.png',
                    'skins/obwx/icons/smoke.png',
                    'skins/obwx/icons/blizzardn@2x.png',
                    'skins/obwx/icons/snowtorainn@2x.png',
                    'skins/obwx/icons/showers@2x.png',
                    'skins/obwx/icons/pcloudyswn.png',
                    'skins/obwx/icons/rainandsnown@2x.png',
                    'skins/obwx/icons/pcloudytn.png',
                    'skins/obwx/icons/tstormn@2x.png',
                    'skins/obwx/icons/mcloudysf.png',
                    'skins/obwx/icons/fdrizzlen@2x.png',
                    'skins/obwx/icons/pcloudy@2x.png',
                    'skins/obwx/icons/sleet.png',
                    'skins/obwx/icons/pcloudyn.png',
                    'skins/obwx/icons/mcloudyswn@2x.png',
                    'skins/obwx/icons/fairn@2x.png',
                    'skins/obwx/icons/drizzlen.png',
                    'skins/obwx/icons/coldn.png',
                    'skins/obwx/icons/drizzle.png',
                    'skins/obwx/icons/mcloudyt.png',
                    'skins/obwx/icons/flurriesw@2x.png',
                    'skins/obwx/icons/flurriesn@2x.png',
                    'skins/obwx/icons/mcloudytwn@2x.png',
                    'skins/obwx/icons/mcloudysf@2x.png',
                    'skins/obwx/icons/hot.png',
                    'skins/obwx/icons/fdrizzlen.png',
                    'skins/obwx/icons/smoke@2x.png',
                    'skins/obwx/icons/mcloudyrwn.png',
                    'skins/obwx/icons/fair@2x.png',
                    'skins/obwx/icons/mcloudysfw@2x.png',
                    'skins/obwx/icons/snowshowerswn.png',
                    'skins/obwx/icons/mcloudyr@2x.png',
                    'skins/obwx/icons/raintosnow@2x.png',
                    'skins/obwx/icons/dustn@2x.png',
                    'skins/obwx/icons/dust@2x.png',
                    'skins/obwx/icons/snowtorain@2x.png',
                    'skins/obwx/icons/mcloudysfn.png',
                    'skins/obwx/icons/snoww@2x.png',
                    'skins/obwx/icons/flurries.png',
                    'skins/obwx/icons/clearwn.png',
                    'skins/obwx/icons/sleetn.png',
                    'skins/obwx/icons/rainandsnow.png',
                    'skins/obwx/icons/raintosnow.png',
                    'skins/obwx/icons/hazyn.png',
                    'skins/obwx/icons/clear.png',
                    'skins/obwx/icons/pcloudytwn.png',
                    'skins/obwx/icons/pcloudysfn.png',
                    'skins/obwx/icons/pcloudyrwn@2x.png',
                    'skins/obwx/icons/mcloudys.png',
                    'skins/obwx/icons/tstormswn.png',
                    'skins/obwx/icons/blizzard.png',
                    'skins/obwx/icons/fog@2x.png',
                    'skins/obwx/icons/freezingrainn.png',
                    'skins/obwx/icons/flurrieswn@2x.png',
                    'skins/obwx/icons/wind@2x.png',
                    'skins/obwx/icons/flurries@2x.png',
                    'skins/obwx/icons/sunnyw.png',
                    'skins/obwx/icons/pcloudyrn.png',
                    'skins/obwx/icons/freezingrain@2x.png',
                    'skins/obwx/icons/snowshowersw@2x.png',
                    'skins/obwx/icons/pcloudysfw.png',
                    'skins/obwx/icons/rainn@2x.png',
                    'skins/obwx/icons/snowshowersn@2x.png',
                    'skins/obwx/icons/pcloudyr.png',
                    'skins/obwx/icons/clearw@2x.png',
                    'skins/obwx/icons/tstormswn@2x.png',
                    'skins/obwx/icons/pcloudy.png',
                    'skins/obwx/icons/blizzard@2x.png',
                    'skins/obwx/icons/mcloudysfwn@2x.png',
                    'skins/obwx/icons/tstorm@2x.png',
                    'skins/obwx/icons/sleetsnow@2x.png',
                    'skins/obwx/icons/rainandsnow@2x.png',
                    'skins/obwx/icons/na.png',
                    'skins/obwx/icons/sunnyn@2x.png',
                    'skins/obwx/icons/sleetsnown.png',
                    'skins/obwx/icons/na@2x.png',
                    'skins/obwx/icons/drizzle@2x.png',
                    'skins/obwx/icons/sunnyw@2x.png',
                    'skins/obwx/icons/pcloudysf@2x.png',
                    'skins/obwx/icons/rain@2x.png',
                    'skins/obwx/icons/hot@2x.png',
                    'skins/obwx/icons/tstormsw.png',
                    'skins/obwx/icons/pcloudysfn@2x.png',
                    'skins/obwx/icons/pcloudyrwn.png',
                    'skins/obwx/icons/mcloudyswn.png',
                    'skins/obwx/icons/mcloudyt@2x.png',
                    'skins/obwx/icons/pcloudysw.png',
                    'skins/obwx/icons/pcloudyrn@2x.png',
                    'skins/obwx/icons/blowingsnow@2x.png',
                    'skins/obwx/icons/showersn.png',
                    'skins/obwx/icons/blowingsnow.png',
                    'skins/obwx/icons/pcloudysfwn.png',
                    'skins/obwx/icons/pcloudysn.png',
                    'skins/obwx/icons/wintrymixn@2x.png',
                    'skins/obwx/icons/cloudyw.png',
                    'skins/obwx/icons/smoken@2x.png',
                    'skins/obwx/icons/pcloudyrw.png',
                    'skins/obwx/icons/pcloudyw@2x.png',
                    'skins/obwx/icons/mcloudyrw.png',
                    'skins/obwx/icons/pcloudysfwn@2x.png',
                    'skins/obwx/icons/showerswn.png',
                    'skins/obwx/icons/windy@2x.png',
                    'skins/obwx/icons/mcloudysfn@2x.png',
                    'skins/obwx/icons/snowflurries@2x.png',
                    'skins/obwx/icons/fdrizzle@2x.png',
                    'skins/obwx/icons/rainw.png',
                    'skins/obwx/icons/wind.png',
                    'skins/obwx/icons/clear@2x.png',
                    'skins/obwx/icons/mcloudyrwn@2x.png',
                    'skins/obwx/icons/flurrieswn.png',
                    'skins/obwx/icons/pcloudywn@2x.png',
                    'skins/obwx/icons/wintrymix@2x.png',
                    'skins/obwx/icons/mcloudyrw@2x.png',
                    'skins/obwx/icons/coldn@2x.png',
                    'skins/obwx/icons/mcloudyrn.png',
                    'skins/obwx/icons/rainn.png',
                    'skins/obwx/icons/pcloudyn@2x.png',
                    'skins/obwx/icons/tstorms.png',
                    'skins/obwx/icons/fdrizzle.png',
                    'skins/obwx/icons/pcloudys@2x.png',
                    'skins/obwx/icons/pcloudytn@2x.png',
                    'skins/obwx/icons/wintrymixn.png',
                    'skins/obwx/icons/cloudyw@2x.png',
                    'skins/obwx/icons/snowtorain.png',
                    'skins/obwx/icons/mcloudytw.png',
                    'skins/obwx/icons/cloudy.png',
                    'skins/obwx/icons/snowwn.png',
                    'skins/obwx/icons/flurriesw.png',
                    'skins/obwx/icons/tstormsn.png',
                    'skins/obwx/icons/cloudyn@2x.png',
                    'skins/obwx/icons/clearw.png',
                    'skins/obwx/icons/snowshowerswn@2x.png',
                    'skins/obwx/icons/blowingsnown.png',
                    'skins/obwx/icons/smoken.png',
                    'skins/obwx/icons/snow@2x.png',
                    'skins/obwx/icons/tstormsw@2x.png',
                    'skins/obwx/icons/cloudy@2x.png',
                    'skins/obwx/icons/snow.png',
                    'skins/obwx/icons/clearn.png',
                    'skins/obwx/icons/snowtorainn.png',
                    'skins/obwx/icons/mcloudyw.png',
                    'skins/obwx/icons/snoww.png',
                    'skins/obwx/icons/fogn@2x.png',
                    'skins/obwx/icons/mcloudytw@2x.png',
                    'skins/obwx/icons/mcloudyw@2x.png',
                    'skins/obwx/icons/sleetn@2x.png',
                    'skins/obwx/icons/cold.png',
                    'skins/obwx/icons/snown.png',
                    'skins/obwx/icons/cloudywn.png',
                    'skins/obwx/icons/pcloudytw@2x.png',
                    'skins/obwx/icons/snowshowers@2x.png',
                    'skins/obwx/icons/mcloudytn.png',
                    'skins/obwx/icons/mcloudysw@2x.png',
                    'skins/obwx/icons/drizzlef.png',
                    'skins/obwx/icons/rainw@2x.png',
                    'skins/obwx/icons/tstorms@2x.png',
                    'skins/obwx/icons/pcloudysw@2x.png',
                    'skins/obwx/icons/pcloudyswn@2x.png',
                    'skins/obwx/icons/mcloudysn.png',
                    'skins/obwx/icons/clearwn@2x.png',
                    'skins/obwx/icons/pcloudyt@2x.png',
                    'skins/obwx/icons/rainandsnown.png',
                    'skins/obwx/icons/fair.png',
                    'skins/obwx/icons/hazy.png',
                    'skins/obwx/icons/showerswn@2x.png',
                    'skins/obwx/icons/mcloudyn.png',
                    'skins/obwx/icons/dustn.png',
                    'skins/obwx/icons/tstormsn@2x.png',
                    'skins/obwx/icons/mcloudywn@2x.png',
                    'skins/obwx/icons/fog.png',
                    'skins/obwx/icons/sunny@2x.png',
                    'skins/obwx/icons/fairn.png',
                    'skins/obwx/icons/mcloudywn.png',
                    'skins/obwx/icons/pcloudyt.png',
                    'skins/obwx/icons/drizzlen@2x.png',
                    'skins/obwx/icons/pcloudys.png',
                    'skins/obwx/icons/cloudywn@2x.png',
                    'skins/obwx/icons/mcloudysn@2x.png',
                    'skins/obwx/icons/mcloudysw.png',
                    'skins/obwx/icons/raindrop.png',
                    'skins/obwx/icons/windicon.png',
                    ]
                )
            ]
        )
