# -*- coding: utf-8 -*-

from common import *
from string import ascii_uppercase as upper_atoz

@route(ROUTE_PREFIX + '/tv')
def tv_menu():
    oc = ObjectContainer()

    oc.add(
        DirectoryObject(
            key = Callback(tv_live_channels),
            title = u'Direkte TV'
        )
    )
    # oc.add(
    #     DirectoryObject(
    #         key = Callback(tv_filtered, filter_suffix = 'recommendedprograms'),
    #         title = u'Anbefalt'
    #     )
    # )
    # oc.add(
    #     DirectoryObject(
    #         key = Callback(tv_filtered, filter_suffix = 'recentlysentprograms'),
    #         title = u'Nylig sendt'
    #     )
    # )
    # oc.add(
    #     DirectoryObject(
    #         key = Callback(tv_filtered, filter_suffix = 'popularprograms'),
    #         title = u'Populært'
    #     )
    # )
    # oc.add(
    #     DirectoryObject(
    #         key = Callback(tv_categories),
    #         title = u'Kategorier'
    #     )
    # )
    # oc.add(
    #     DirectoryObject(
    #         key = Callback(tv_index_menu),
    #         title = u'A-Å'
    #     )
    #)
    return oc

@route(ROUTE_PREFIX + '/tv/live')
def tv_live_channels():
    return populate_from_list(CHANNELS_ROOT_URL)


# @route(ROUTE_PREFIX + '/tv/categories')
# def tv_categories():
#     # Drop first category which is all-programs, weirdly labeled "Anbefalt"
#     categories = fetch_json_from_tvapi(CATEGORIES_ROOT_URL)[1:]
#     oc = ObjectContainer()
#     for category in categories:
#         oc.add(
#             DirectoryObject(
#                 key = Callback(tv_category, category_id = category['categoryId']),
#                 title = category['displayValue']
#             )
#         )
#     return oc


# @route(ROUTE_PREFIX + '/tv/categories/{category_id}')
# def tv_category(category_id):
#     url = CATEGORY_BASE_URL.format(category_id, 'programs')
#     return populate_from_list(url)


# @route(ROUTE_PREFIX + '/tv/filtered/{filter_suffix}')
# def tv_filtered(filter_suffix):
#     url = CATEGORY_BASE_URL.format('all-programs', filter_suffix)
#     return populate_from_list(url)


# @route(ROUTE_PREFIX + '/tv/index')
# def tv_index_menu():
#     oc = ObjectContainer()
#     for index in ['[0-9]'] + list(upper_atoz) + [u'Æ', u'Ø', u'Å']:
#         oc.add(
#             DirectoryObject(
#                 key = Callback(tv_indexed, letter = index),
#                 title = index
#             )
#         )
#     return oc


# @route(ROUTE_PREFIX + '/tv/index/{letter}')
# def tv_indexed(letter):
#     # NOTE: This fetches all programs indexed. Haven't found a way to fetch only by letter.
#     # FIXME: Doesn't handle programs with titles starting with non-alphanumeric characters
#     all_programs_indexed = fetch_json_from_tvapi(INDEX_URL)
#     oc = ObjectContainer(
#         objects = [clip_from_program_json(program) for program in all_programs_indexed if starts_with(program['title'], letter)]
#     )
#     return oc


# @route(ROUTE_PREFIX + '/tv/series/{series_id}')
# def tv_series(series_id):
#     series = fetch_json_from_tvapi(SERIES_ROOT_URL + series_id)
#     oc = ObjectContainer()
#     for i, season in enumerate(series['seasonIds'][::-1]):
#         available_episodes = len([program for program in series['programs'] if program['seasonId'] == season['id'] and is_playable(program)])
#         if available_episodes > 0:
#             oc.add(
#                 SeasonObject(
#                     key = Callback(tv_season, series_id = series_id, season_id = str(season['id'])),
#                     rating_key = SERIES_ROOT_URL + series_id + '/' + str(season['id']),
#                     index = i,
#                     title = season['name'],
#                     show = series['title'],
#                     episode_count = len([program for program in series['programs'] if program['seasonId'] == season['id']]),
#                     thumb = get_url_from_image_id(series.get('imageId')),
#                     art = get_url_from_image_id(series.get('imageId'))
#                 )
#             )
#     return oc


# @route(ROUTE_PREFIX + '/tv/series/{series_id}/{season_id}')
# def tv_season(series_id, season_id):
#     series = fetch_json_from_tvapi(SERIES_ROOT_URL + series_id)
#     oc = ObjectContainer(
#         objects = [clip_from_program_json(program) for program in series['programs'] if str(program['seasonId']) == season_id and is_playable(program)]
#     )
#     return  oc
