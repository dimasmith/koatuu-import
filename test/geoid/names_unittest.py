import unittest

from geoid.names import normalize_oblast_name, normalize_raion_name, normalize_city_name


class NamesTest(unittest.TestCase):
    def test_oblast_name_normalization(self):
        self.assertEqual('Запорізька', normalize_oblast_name('ЗАПОРІЗЬКА ОБЛАСТЬ'))
        self.assertEqual('Запорізька', normalize_oblast_name('ЗАПОРІЗЬКА'))
        self.assertEqual('Крим', normalize_oblast_name('АВТОНОМНА РЕСПУБЛІКА КРИМ'))

    def test_city_name_normalization(self):
        self.assertEqual('Радехів', normalize_city_name('РАДЕХІВ'))
        self.assertEqual('Радехів', normalize_city_name('М.РАДЕХІВ'))
        self.assertEqual('Радехів', normalize_city_name('СМТ.РАДЕХІВ'))
        self.assertEqual('Радехів', normalize_city_name('С.РАДЕХІВ'))
        self.assertEqual('Радехів', normalize_city_name('М РАДЕХІВ'))
        self.assertEqual('Радехів', normalize_city_name('СМТ РАДЕХІВ'))
        self.assertEqual('Радехів', normalize_city_name('С РАДЕХІВ'))

    def test_city_names_with_defis(self):
        self.assertEqual('Володимир-Волинський', normalize_city_name('ВОЛОДИМИР-ВОЛИНСЬКИЙ'))
        self.assertEqual('Нова Каховка', normalize_city_name('НОВА КАХОВКА'))

    def test_raion_name_normalization(self):
        self.assertEqual('Радехівський', normalize_raion_name('РАДЕХІВСЬКИЙ РАЙОН'))
        self.assertEqual('Радехівський', normalize_raion_name('РАДЕХІВСЬКИЙ Р-Н'))
        self.assertEqual('Володимир-Волинський', normalize_raion_name('ВОЛОДИМИР-ВОЛИНСЬКИЙ РАЙОН'))
