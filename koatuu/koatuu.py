class KoatuuCode:
    """Parse string representation of KOATUU code."""
    def __init__(self, code):
        super().__init__()
        self.code = code.rjust(10, '0')

    def is_raion_descriptor(self):
        return self.code.endswith('00000') \
               and self.code[2] == '2' \
               and not self.code.endswith('0000000')

    def is_oblast_descriptor(self):
        return self.code.endswith('00000000')

    def get_oblast_code(self):
        return self.code[:2]

    def as_string(self):
        return self.code

    def get_raion_code(self):
        return self.code[:5]


def parse_unit_name(compound_name):
    """Separates KOATUU unit names into unit name and city name."""
    parts = compound_name.partition('/')
    unit_name = parts[0]
    city_name = parts[2]
    return unit_name, city_name

