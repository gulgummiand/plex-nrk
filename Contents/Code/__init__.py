# -*- coding: utf-8 -*-

import tv
import radio
from common import ROUTE_PREFIX

NAME = 'NRK'
ART = 'art-default.png'
ICON = 'icon-default.png'


def Start():
    ObjectContainer.title1 = NAME
    #HTTP.CacheTime = CACHE_1HOUR
    HTTP.ClearCache()


@handler(ROUTE_PREFIX, NAME, art=ART, thumb=ICON)
def main_menu():
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

