# -*- coding: utf-8 -*-

from PMS import *

from common import ROUTE_PREFIX
import tv
import radio

NAME = 'NRK'
ART = 'art-default.png'
ICON = 'icon-default.png'


def Start():
    ObjectContainer.title1 = NAME
    #HTTP.CacheTime = CACHE_1HOUR # in sec: CACHE_1MINUTE, CACHE_1HOUR, CACHE_1DAY, CACHE_1WEEK, CACHE_1MONTH
    HTTP.ClearCache()


#@handler(ROUTE_PREFIX, NAME, art=ART, thumb=ICON)
@handler(ROUTE_PREFIX, NAME, ICON)
@route(ROUTE_PREFIX + '/MainMenu')
def Main_Menu():
    Log.Debug("Staring MainMenu")
    oc = ObjectContainer()
    oc.add(
        DirectoryObject(
            key = Callback(tv.tv_menu),
            title = u'NRK TV',
            thumb = R('tv-icon.png')
        )
    )
    oc.add(
        DirectoryObject(
            key = Callback(radio.radio_menu),
            title = u'NRK Radio',
            thumb = R('radio-icon.png')
        )
    )
    return oc

