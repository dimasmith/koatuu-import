import csv
import logging

from koatuu.koatuu import KoatuuCode, parse_unit_name


def read_raion_centers(path):
    """
    Read list of raion and raion center cities from KOATUU csv.

    Raion description contains oblast which it belongs to.
    """
    raions = []
    oblasts_map = {}
    with open(path) as koatuu:
        reader = csv.DictReader(koatuu)
        for row in reader:
            koatuu_code = KoatuuCode(row['TE'])
            oblast_code = koatuu_code.get_oblast_code()
            title = row['NU']
            if koatuu_code.is_raion_descriptor():
                region_name, city_name = parse_unit_name(title)
                city = {'region': region_name, 'city': city_name, 'koatuu': koatuu_code.as_string(),
                        'oblast_code': oblast_code}
                raions.append(city)

            if koatuu_code.is_oblast_descriptor():
                oblast_name, _ = parse_unit_name(title)
                oblast = {'oblast': oblast_name, 'koatuu': koatuu_code.as_string(), 'oblast_code': oblast_code}
                oblasts_map[oblast_code] = oblast

    return map_raions_to_oblasts(raions, oblasts_map)


def map_raions_to_oblasts(raions, oblasts_map):
    for raion in raions:
        oblast = oblasts_map.get(raion['oblast_code'])
        if oblast is None:
            logging.warning('Failed to find oblast for raion %s', raion)
            continue

        raion.pop('oblast_code')
        raion['oblast'] = oblast

    return raions
