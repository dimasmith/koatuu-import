def _normalize_oblast(oblast):
    return oblast.lower()


def _normalize_raion(raion):
    return raion.lower()


def _normalize_city(city):
    return city.lower()


def generate_key(oblast, raion, city):
    return '/'.join([_normalize_oblast(oblast), _normalize_city(city)])
