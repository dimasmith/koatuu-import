import csv

from geoid.key import generate_key
from geoid.names import normalize_oblast_name, normalize_city_name, normalize_raion_name
from koatuu.koatuu import KoatuuCode, parse_unit_name


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
                    '_id': koatuu_code.as_string(),
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
