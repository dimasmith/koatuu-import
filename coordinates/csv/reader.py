import csv

from geoid.key import generate_key


def _create_geo_json_point(lat, lon):
    return {'type': 'Point', 'coordinates': [float(lat), float(lon)]}


def read_points(file_path):
    points = []
    with open(file_path, 'r', encoding='utf-8') as coords_file:
        reader = csv.DictReader(coords_file, delimiter=';', fieldnames=['oblast', 'raion', 'city', 'lon', 'lat'])
        for point in reader:
            loc = _create_geo_json_point(point['lat'], point['lon'])
            point['key'] = generate_key(point['oblast'], point['raion'], point['city'])
            point['loc'] = loc
            points.append(point)
    return points
