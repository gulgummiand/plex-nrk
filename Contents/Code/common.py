# -*- coding: utf-8 -*-

ROUTE_PREFIX = '/video/nrk'
TVAPI_URL = 'http://tvapi.nrk.no/v1'
CHANNELS_ROOT_URL = TVAPI_URL + '/channels/'
CATEGORIES_ROOT_URL = TVAPI_URL + '/categories/'
CATEGORY_BASE_URL = CATEGORIES_ROOT_URL + '{}/{}'
INDEX_URL = CATEGORY_BASE_URL.format('all-programs', 'indexelements')
PROGRAMS_ROOT_URL = TVAPI_URL + '/programs/'
SERIES_ROOT_URL = TVAPI_URL + '/series/'
SEARCH_ROOT_URL = TVAPI_URL + '/search/'

IMAGE_BASE_URL = 'http://gfx.nrk.no/{}'

HTTP_HEADERS = {
    'User-Agent': 'plex.tv',
    'app-version-android': 999
}


def populate_from_list(url, is_audio_only = False):
    programs = fetch_json_from_tvapi(url)
    oc = ObjectContainer(
        objects = [clip_from_program_json(program, is_audio_only) for program in programs if is_playable(program)]
    )
    return oc


def starts_with(title, letter):
    return title[0].isdigit() if letter == '[0-9]' else title[0].upper() == letter.upper()


def is_playable(program_json):
    return 'mediaUrl' in program_json or program_json.get('isAvailable', False)


def clip_from_program_json(json, is_audio_only = False):
    if json.get('type') == 'SERIES':
        clip_object = TVShowObject(
            key = Callback(tv_series, series_id = json['seriesId']),
            rating_key = SERIES_ROOT_URL + json['seriesId'],
            title = json.get('title'),
            summary = json.get('description'),
            thumb = get_url_from_image_id(json.get('imageId')),
            art = get_url_from_image_id(json.get('imageId'))
        )
    else:
        program_id = json.get('programId') or json.get('channelId')
        clip_object_type = TrackObject if is_audio_only else VideoClipObject

        clip_object = clip_object_type(
            url = PROGRAMS_ROOT_URL + program_id,
            title = ' '.join(filter(None, [json.get('title'), json.get('episodeNumberOrDate')])),
            thumb = get_url_from_image_id(json.get('imageId')),
            art = get_url_from_image_id(json.get('imageId'))
        )
    return clip_object


def get_url_from_image_id(image_id):
    return IMAGE_BASE_URL.format(image_id)


def fetch_json_from_tvapi(url):
    return JSON.ObjectFromURL(url, headers = HTTP_HEADERS)

