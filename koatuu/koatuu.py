class KoatuuCode:
    """Parse string representation of KOATUU code."""
    def __init__(self, code):
        super().__init__()
        self.code = code

    def is_raion_descriptor(self):
        return self.code.endswith('00000') \
               and self.code[2] == '2' \
               and not self.code.endswith('0000000')

    def is_oblast_descriptor(self):
        return self.code.endswith('00000000')

    def get_oblast_code(self):
        oblast_code = self.code[:2]
        if oblast_code == '52':
            return '50'  # exception for Vinnytska oblast
        if oblast_code == '72':
            return '70'  # exception for Volynska oblast
        return oblast_code

    def as_string(self):
        return self.code


def parse_unit_name(compound_name):
    """Separates KOATUU unit names into unit name and city name."""
    parts = compound_name.partition('/')
    unit_name = parts[0]
    city_name = parts[2]
    return unit_name, city_name

