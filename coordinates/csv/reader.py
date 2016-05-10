import csv

from geoid.key import generate_key


def read_points(file_path):
    points = []
    with open(file_path, 'r', encoding='utf-8') as coords_file:
        reader = csv.DictReader(coords_file, delimiter=';', fieldnames=['oblast', 'raion', 'city', 'lon', 'lat'])
        for point in reader:
            point['key'] = generate_key(point['oblast'], point['raion'], point['city'])
            points.append(point)
    return points
