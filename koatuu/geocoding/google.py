from string import Template

from os import getenv

import googlemaps


def geocode(query):
    google_maps = _create_maps_client()
    return google_maps.geocode(query, language='uk', region='UA')


def geocode_raion(raion):
    geocode_query = _create_raion_geocode_query(raion)
    return geocode(geocode_query)


def geocode_raions(raions):
    google_maps = _create_maps_client()
    queries = map(_create_raion_geocode_query, raions)
    geocodes = [google_maps.geocode(query, language='uk', region='UA') for query in queries]
    return geocodes


def _create_raion_geocode_query(raion):
    geocode_query = Template('$oblast, $city').substitute(oblast=raion['oblast']['oblast'], city=raion['city'])
    return geocode_query


def _create_maps_client():
    google_api_key = getenv('GOOGLE_API_KEY')
    google_maps = googlemaps.Client(google_api_key)
    return google_maps
