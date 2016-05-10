import csv
import logging

from geoid.names import normalize_oblast_name, normalize_city_name, normalize_raion_name
from geoid.key import generate_key
from koatuu.koatuu import KoatuuCode, parse_unit_name


def strip_city_type(city_name):
    prefixes = ['М ', 'СМТ ', 'М.', 'СМТ.', 'С.']
    for prefix in prefixes:
        if city_name.startswith(prefix):
            return city_name[len(prefix):len(city_name) + 1].lower()

    logging.warning(city_name)
    return city_name.lower()


def strip_raion_name(raion_name):
    return raion_name[0: len(raion_name) - len(' РАЙОН')].lower()


def strip_oblast_name(oblast):
    if oblast.endswith('КРИМ'):
        return 'крим'
    return oblast[0: len(oblast) - len(' ОБЛАСТЬ')]


def read_points(file_path):
    points = []
    with open(file_path, 'r', encoding='utf-8') as koatuu_file:
        reader = csv.DictReader(koatuu_file, fieldnames=['koatuu', 'type', 'title'])
        for point in reader:
            points.append(point)
    return points


def read_raion_centers(path):
    """
    Read list of raion and raion center cities from KOATUU csv.

    Raion description contains oblast which it belongs to.
    """
    raions = []
    oblasts_map = {}
    with open(path, 'r', encoding='utf-8') as koatuu:
        reader = csv.DictReader(koatuu)
        for row in reader:
            koatuu_code = KoatuuCode(row['TE'])
            oblast_code = koatuu_code.get_oblast_code()
            title = row['NU']
            if koatuu_code.is_raion_descriptor():
                oblast_name = oblasts_map[oblast_code]
                raion_name, city_name = parse_unit_name(title)
                raion_name = normalize_raion_name(raion_name)
                city_name = normalize_city_name(city_name)
                oblast_name = normalize_oblast_name(oblast_name)
                key = generate_key(oblast_name, raion_name, city_name)

                city = {
                    'id': koatuu_code.get_raion_code(),
                    'raion': raion_name,
                    'city': city_name,
                    'oblast': oblast_name,
                    'key': key,
                    'koatuu': koatuu_code.as_string()}
                raions.append(city)

            if koatuu_code.is_oblast_descriptor():
                oblast_name, _ = parse_unit_name(title)
                oblasts_map[oblast_code] = oblast_name

    return raions


def map_raions_to_oblasts(raions, oblasts_map):
    for raion in raions:
        oblast = oblasts_map.get(raion['oblast_code'])
        oblast_key = strip_oblast_name(oblast['oblast'])
        obl = normalize_oblast_name(oblast['oblast'])
        raion['obl'] = obl
        raion['key']['oblast'] = oblast_key
        if oblast is None:
            logging.warning('Failed to find oblast for raion %s', raion)
            continue

        raion.pop('oblast_code')
        raion['oblast'] = oblast

    return raions
