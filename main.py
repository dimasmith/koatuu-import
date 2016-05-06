import logging

from koatuu.csv.reader import read_raion_centers
from koatuu.geocoding.google import geocode_raions
from koatuu.mongo import writer as mongo


def main():
    raions = read_raion_centers('data/koatuu.csv')
    geocodes = geocode_raions(raions)
    for raion, geocode in zip(raions, geocodes):
        raion['geocode'] = geocode

    mongo.insert_raions(raions)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
