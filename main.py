import logging
import csv


def is_raion_city(koatuu_code):
    return koatuu_code.endswith('00000') \
           and koatuu_code[2] == '2' \
           and not koatuu_code.endswith('0000000')


def is_oblast(koatuu_code):
    return koatuu_code.endswith('00000000')


def main():
    logging.info('Starting import')
    with open('data/koatuu.csv') as koatuu:
        reader = csv.DictReader(koatuu)
        raions = []
        oblasts = []
        oblasts_map = {}
        for row in reader:
            city_code = row['TE']
            oblast_code = city_code[:2]
            if is_raion_city(city_code):
                city_name = row['NU'].partition('/')[2]
                region_name = row['NU'].partition('/')[0]
                city = {'region': region_name, 'city': city_name, 'koatuu': city_code, 'oblast_code': oblast_code}
                raions.append(city)

            if is_oblast(city_code):
                oblast = {'oblast': row['NU'], 'koatuu': city_code, 'oblast_code': oblast_code}
                oblasts.append(oblast)
                oblasts_map[oblast_code] = oblast


    oblasts_map['52'] = oblasts_map['50']
    oblasts_map['72'] = oblasts_map['70']

    for raion in raions:
        oblast = oblasts_map.get(raion['oblast_code'])
        raion['oblast'] = oblast
        if oblast == None:
            logging.warning(raion)

    logging.info('Filtered %s cities', len(raions))
    for raion in raions:
        print(raion)
    logging.info('Filtered %s oblasts', len(oblasts))
    for oblast in oblasts:
        print(oblast)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
