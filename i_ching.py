import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logging.disable(logging.CRITICAL)

basic_trigrams = {
    'heaven':   (1, 1, 1),
    'lake':     (0, 1, 1),
    'flame':    (1, 0, 1),
    'thunder':  (0, 0, 1),
    'wind':     (1, 1, 0),
    'water':    (0, 1, 0),
    'mountain': (1, 0, 0),
    'earth':    (0, 0 , 0),
    }

hex_details = {
    1: ('the creative, heaven', ('heaven', 'heaven')),
    2: ('the receptive, earth', ('earth', 'earth')),
    3: ('difficulty at the beginning', ('water', 'thunder')),
    4: ('youthful folly', ('mountain', 'water')),
    5: ('waiting', ('water', 'heaven')),
    6: ('conflict', ('heaven', 'water')),
    7: ('the army', ('earth', 'water')),
    8: ('holding together', ('water', 'earth')),
    9: ('the taming power of the small', ('wind', 'heaven')),
    10: ('treading (conduct)', ('heaven', 'lake')),
    11: ('peace', ('earth', 'heaven')),
    12: ('standstill (stagnation)', ('heaven', 'earth')),
    13: ('fellowship with men', ('heaven', 'flame')),
    14: ('possession in great measure', ('flame', 'heaven')),
    15: ('modesty', ('earth', 'mountain')),
    16: ('enthusiasm', ('thunder', 'earth')),
    17: ('following', ('lake', 'thunder')),
    18: ('work on what has been spoiled (decay)', ('mountain', 'wind')),
    19: ('approach', ('earth', 'lake')),
    20: ('contemplation (view)', ('wind', 'earth')),
    21: ('biting through', ('flame', 'thunder')),
    22: ('grace', ('mountain', 'flame')),
    23: ('splitting apart', ('mountain', 'earth')),
    24: ('return (the turning point)', ('earth', 'thunder')),
    25: ('innocence (the unexpected)', ('heaven', 'thunder')),
    26: ('the taming power of the great', ('mountain', 'heaven')),
    27: ('the corners of the mouth '
            '(providing nourishment)', ('mountain', 'thunder')),
    28: ('preponderance of the great', ('lake', 'wind')),
    29: ('the abysmal (water)', ('water', 'water')),
    30: ('the clinging, fire', ('flame', 'flame')),
    31: ('influence (wooing)', ('lake', 'mountain')),
    32: ('duration', ('thunder', 'wind')),
    33: ('retreat', ('heaven', 'mountain')),
    34: ('the power of the great', ('thunder', 'heaven')),
    35: ('progress', ('flame', 'earth')),
    36: ('brilliance injured', ('earth', 'flame')),
    37: ('the family (the clan)', ('wind', 'flame')),
    38: ('opposition', ('flame', 'lake')),
    39: ('obstruction', ('water', 'mountain')),
    40: ('deliverance', ('thunder', 'water')),
    41: ('decrease', ('mountain', 'lake')),
    42: ('increase', ('wind', 'thunder')),
    43: ('break-through (resoluteness)', ('lake', 'heaven')),
    44: ('coming to meet', ('heaven', 'wind')),
    45: ('gathering together (massing)', ('lake', 'earth')),
    46: ('pushing upward', ('earth', 'wind')),
    47: ('oppression (exhaustion)', ('lake', 'water')),
    48: ('the well', ('water', 'wind')),
    49: ('revolution (molting)', ('lake', 'flame')),
    50: ('the cauldron', ('flame', 'wind')),
    51: ('the arousing (shock, thunder)', ('thunder', 'thunder')),
    52: ('keeping still, mountain', ('mountain', 'mountain')),
    53: ('development (gradual progress)', ('wind', 'mountain')),
    54: ('the marrying maiden', ('thunder', 'lake')),
    55: ('abundance', ('thunder', 'flame')),
    56: ('the wanderer', ('flame', 'mountain')),
    57: ('the gentle (the penetrating, wind)', ('wind', 'wind')),
    58: ('the joyous, lake', ('lake', 'lake')),
    59: ('dispersion (dissolution)', ('wind', 'water')),
    60: ('limitation', ('water', 'lake')),
    61: ('inner truth', ('wind', 'lake')),
    62: ('preponderance of the small', ('thunder', 'mountain')),
    63: ('after completion', ('water', 'flame')),
    64: ('before completion', ('flame', 'water')),
    }

def get_hex_lines(hex_number):
    """Makes hexagram sequence from basic_trigrams and hex_instruct."""
    hex_lines = []

    for trigram in hex_details[hex_number][1]:
        hex_lines += basic_trigrams[trigram]

    return hex_lines

def verify_changing(hex_sequence):
    """Verifies a hexagram sequence."""
    # TODO
    pass

def print_hex_lines(hex_lines):
    """Creates hexagram diagrams."""
    yang =          '▀▀▀▀▀▀▀▀▀▀▀'
    yin =           '▀▀▀▀   ▀▀▀▀'
    changing_yin =  '▀▀▀▀▀∆▀▀▀▀▀'
    changing_yang = '▀▀▀▀ ∆ ▀▀▀▀' 

    for line in hex_lines:
        visual = yang if line == 1 else yin
        print(visual)

# TODO reading + line scraper
    # TODO scrape from cafeausoul
    # TODO scrape from dekorne

while True:
    hex_num = int(input("Enter hexagram #: "))
    hex_lines = get_hex_lines(hex_num)
    print(hex_lines)
    print_hex_lines(hex_lines)
