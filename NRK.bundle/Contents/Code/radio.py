# -*- coding: utf-8 -*-

from common import *

# Hardcoded channels. Have so far not found a way to extract
# these from api. Format: [(channel_id, title), ...]
RADIO_CHANNELS_NATIONAL = [
    ('p1', u'NRK P1'),
    ('p1pluss', u'NRK P1+'),
    ('p2', u'NRK P2'),
    ('p3', u'NRK P3'),
    ('p13', u'NRK P13'),
    ('mp3', u'NRK MP3'),
    ('alltid_nyheter', u'NRK Alltid Nyheter'),
    ('radio_super', u'NRK Super'),
    ('klassisk', u'NRK Klassisk'),
    ('sapmi', u'NRK Sápmi'),
    ('jazz', u'NRK Jazz'),
    ('folkemusikk', u'NRK Folkemusikk'),
    ('sport', u'NRK Sport'),
    ('urort', u'NRK Urørt'),
    ('radioresepsjonen', u'NRK Radioresepsjonen'),
    ('national_rap_show', u'NRK National Rap Show')
]

RADIO_CHANNELS_DISTRICT = [
    ('p1_buskerud', u'NRK P1 Buskerud'),
    ('p1_finnmark', u'NRK P1 Finnmark'),
    ('p1_hedmark_oppland', u'NRK P1 Hedmark og Oppland'),
    ('p1_hordaland', u'NRK P1 Hordaland'),
    ('p1_more_romsdal', u'NRK P1 Møre og Romsdal'),
    ('p1_nordland', u'NRK P1 Nordland'),
    ('p1_oslo_akershus', u'NRK P1 Oslo og Akershus'),
    ('p1_rogaland', u'NRK P1 Rogaland'),
    ('p1_sogn_fjordane', u'NRK P1 Sogn og Fjordane'),
    ('p1_sorlandet', u'NRK P1 Sørlandet'),
    ('p1_telemark', u'NRK P1 Telemark'),
    ('p1_troms', u'NRK P1 Troms'),
    ('p1_trondelag', u'NRK P1 Trøndelag'),
    ('p1_vestfold', u'NRK P1 Vestfold'),
    ('p1_ostfold', u'NRK P1 Østfold')
]



@route(ROUTE_PREFIX + '/radio')
def radio_menu():
    oc = ObjectContainer()

    oc.add(
        DirectoryObject(
            key = Callback(radio_live_channels),
            title = u'Direkte Radio'
        )
    )
    return oc


@route(ROUTE_PREFIX + '/radio/live')
def radio_live_channels(region = 'national'):
    oc = ObjectContainer()
    channels = RADIO_CHANNELS_NATIONAL if region == 'national' else RADIO_CHANNELS_DISTRICT
    for channel_id, channel_name in channels:
        oc.add(
            TrackObject(
                url = PROGRAMS_ROOT_URL + channel_id,
                title = channel_name,
                thumb = R(channel_id + '_logo.png') if region == 'national' else R('p1_logo.png')
            )
        )
    if region != 'district':
        oc.add(
            DirectoryObject(
                key = Callback(radio_live_channels, region = 'district'),
                title = u'Distriktskanaler'
            )
        )
    return oc



