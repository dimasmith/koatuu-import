import logging

from koatuu.csv.reader import read_raion_centers
from koatuu.mongo import writer


def main():
    raions = read_raion_centers('data/koatuu.csv')
    writer.write_raions(raions)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
