import logging

from os import getenv

from os.path import join

from coordinates.csv import reader as coordinates_reader
from koatuu.csv import reader as koatuu_reader
from koatuu.mongo.writer import insert_raions


def main():
    raion_centers = koatuu_reader.read_raion_centers(join('data', 'koatuu.csv'))
    raion_centers_map = {}
    for raion_center in raion_centers:
        raion_centers_map[raion_center['key']] = raion_center

    coordinates_points = coordinates_reader.read_points(join('data', 'cities-with-coordinates_utf-8.csv'))
    for cp in coordinates_points:
        raion = raion_centers_map.pop(cp['key'], None)
        if raion:
            raion['loc'] = cp['loc']

    insert_raions(raion_centers, mongo_uri=getenv('MONGO_URI'))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
