import logging

from koatuu.csv.reader import read_raion_centers


def main():
    raions = read_raion_centers('data/koatuu.csv')

    logging.info('Filtered %s cities', len(raions))
    for raion in raions:
        print(raion)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
