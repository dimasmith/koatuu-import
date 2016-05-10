from string import capwords

CRIMEA = 'крим'
OBLAST_SUFFIXES = ['область']
RAION_SUFFIXES = ['район', 'р-н']
CITY_PREFIXES = ['м.', 'смт.', 'с.', 'м ', 'смт ', 'с ']


def normalize_oblast_name(oblast_name):
    if oblast_name.lower().endswith(CRIMEA):
        return capwords(CRIMEA)
    return _capitalize_words(_strip_suffixes(oblast_name, OBLAST_SUFFIXES))


def normalize_city_name(city_name):
    return _capitalize_words(_strip_prefixes(city_name, CITY_PREFIXES))


def normalize_raion_name(name):
    return _capitalize_words(_strip_suffixes(name, RAION_SUFFIXES))


def _capitalize_words(name):
    if name.find('-') != -1:
        return capwords(name, '-').rstrip()
    return capwords(name).rstrip()


def _strip_prefixes(name, prefixes):
    corrected_name = name
    for prefix in prefixes:
        if corrected_name.lower().startswith(prefix):
            corrected_name = corrected_name[len(prefix):]
    return corrected_name


def _strip_suffix(name, suffix):
    if name.lower().endswith(suffix):
        stripped_name = name[0: len(name) - len(suffix)]
        return stripped_name
    return name


def _strip_suffixes(name, suffixes):
    corrected_name = name
    for suffix in suffixes:
        corrected_name = _strip_suffix(corrected_name, suffix)
    return corrected_name
