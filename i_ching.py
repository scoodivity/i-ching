#! python3

import logging
import re

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
#logging.disable(logging.CRITICAL)

basic_trigrams = {
    'heaven':   (1, 1, 1),
    'lake':     (1, 1, 0),
    'flame':    (1, 0, 1),
    'thunder':  (1, 0, 0),
    'wind':     (0, 1, 1),
    'water':    (0, 1, 0),
    'mountain': (0, 0, 1),
    'earth':    (0, 0, 0),
    }

hex_details = {
    1: ('the creative, heaven', ('heaven', 'heaven')),
    2: ('the receptive, earth', ('earth', 'earth')),
    3: ('difficulty at the beginning', ('thunder', 'water')),
    4: ('youthful folly', ('water', 'mountain')),
    5: ('waiting', ('heaven', 'water')),
    6: ('conflict', ('water', 'heaven')),
    7: ('the army', ('water', 'earth')),
    8: ('holding together', ('earth', 'water')),
    9: ('the taming power of the small', ('heaven', 'wind')),
    10: ('treading (conduct)', ('lake', 'heaven')),
    11: ('peace', ('heaven', 'earth')),
    12: ('standstill (stagnation)', ('earth', 'heaven')),
    13: ('fellowship with men', ('flame', 'heaven')),
    14: ('possession in great measure', ('heaven', 'flame')),
    15: ('modesty', ('mountain', 'earth')),
    16: ('enthusiasm', ('earth', 'thunder')),
    17: ('following', ('thunder', 'lake')),
    18: ('work on what has been spoiled (decay)', ('wind', 'mountain')),
    19: ('approach', ('lake', 'earth')),
    20: ('contemplation (view)', ('earth', 'wind')),
    21: ('biting through', ('thunder', 'flame')),
    22: ('grace', ('flame', 'mountain')),
    23: ('splitting apart', ('earth', 'mountain')),
    24: ('return (the turning point)', ('thunder', 'earth')),
    25: ('innocence (the unexpected)', ('thunder', 'heaven')),
    26: ('the taming power of the great', ('heaven', 'mountain')),
    27: ('the corners of the mouth '
            '(providing nourishment)', ('thunder', 'mountain')),
    28: ('preponderance of the great', ('wind', 'lake')),
    29: ('the abysmal (water)', ('water', 'water')),
    30: ('the clinging, fire', ('flame', 'flame')),
    31: ('influence (wooing)', ('mountain', 'lake')),
    32: ('duration', ('wind', 'thunder')),
    33: ('retreat', ('mountain', 'heaven')),
    34: ('the power of the great', ('heaven', 'thunder')),
    35: ('progress', ('earth', 'flame')),
    36: ('brilliance injured', ('flame', 'earth')),
    37: ('the family (the clan)', ('flame', 'wind')),
    38: ('opposition', ('lake', 'flame')),
    39: ('obstruction', ('mountain', 'water')),
    40: ('deliverance', ('water', 'thunder')),
    41: ('decrease', ('lake', 'mountain')),
    42: ('increase', ('thunder', 'wind')),
    43: ('break-through (resoluteness)', ('heaven', 'lake')),
    44: ('coming to meet', ('wind', 'heaven')),
    45: ('gathering together (massing)', ('earth', 'lake')),
    46: ('pushing upward', ('wind', 'earth')),
    47: ('oppression (exhaustion)', ('water', 'lake')),
    48: ('the well', ('wind', 'water')),
    49: ('revolution (molting)', ('flame', 'lake')),
    50: ('the cauldron', ('wind', 'flame')),
    51: ('the arousing (shock, thunder)', ('thunder', 'thunder')),
    52: ('keeping still, mountain', ('mountain', 'mountain')),
    53: ('development (gradual progress)', ('mountain', 'wind')),
    54: ('the marrying maiden', ('lake', 'thunder')),
    55: ('abundance', ('flame', 'thunder')),
    56: ('the wanderer', ('mountain', 'flame')),
    57: ('the gentle (the penetrating, wind)', ('wind', 'wind')),
    58: ('the joyous, lake', ('lake', 'lake')),
    59: ('dispersion (dissolution)', ('water', 'wind')),
    60: ('limitation', ('lake', 'water')),
    61: ('inner truth', ('lake', 'wind')),
    62: ('preponderance of the small', ('mountain', 'thunder')),
    63: ('after completion', ('flame', 'water')),
    64: ('before completion', ('water', 'flame')),
    }

sample_correct_sequence = '50.1.2.3.4.5.42'
sample_wrong_sequence1 = '1.64'
sample_wrong_sequence2 = '64.5.23'

def create_hex_vars(hex_sequence):
    """Breaks hex_sequence into components (cast, changing, lines)."""
    sequence_list = hex_sequence.split('.')
    cast_hex = None
    relating_hex = None
    changing_lines = []

    if len(sequence_list) == 1:
        cast_hex = int(sequence_list(0))

    elif len(sequence_list) == 2:
        pass

    else:
        cast_hex = int(sequence_list.pop(0))
        relating_hex = int(sequence_list.pop(-1))
        for line in sequence_list:
            changing_lines.append(int(line))

    return cast_hex, relating_hex, changing_lines

def get_hex_lines(hex_number):
    """Makes hexagram sequence from basic_trigrams and hex_instruct."""
    hex_lines = []

    for trigram in hex_details[hex_number][1]:
        hex_lines += basic_trigrams[trigram]

    return hex_lines

def verify_sequence(hex_sequence):
    """Verifies a hexagram sequence. Boolean result."""
    valid = None
    cast_hex, relating_hex, changing_lines = create_hex_vars(hex_sequence)

    logging.info(f"sequence to check: {hex_sequence}")
    logging.info(f"cast_hex: {cast_hex}")
    logging.info(f"relating_hex: {relating_hex}")
    logging.info(f"changing_lines: {changing_lines}")    

    try:
        transform = get_hex_lines(cast_hex)
        relating_hex_lines = get_hex_lines(relating_hex)

        logging.info(f"transform start: {transform}")
        for i in changing_lines:
            if transform[i - 1] == 1:
                transform[i - 1] = 0
            else:         
                transform[i - 1] = 1

        logging.info(f"transform end: {transform}")
        logging.info(f"relating hex: {relating_hex_lines}")

        if transform == relating_hex_lines:
            valid = True
        else:
            valid = False

    except KeyError:
        valid = False

    return valid

def print_hex_lines(hex_lines):
    """Creates hexagram diagrams."""
    yang =          '▀▀▀▀▀▀▀▀▀▀▀'
    yin =           '▀▀▀▀   ▀▀▀▀'
    changing_yin =  '▀▀▀▀▀∆▀▀▀▀▀'
    changing_yang = '▀▀▀▀ ∆ ▀▀▀▀' 

    logging.info(hex_lines)
    hex_lines.reverse()

    for line in hex_lines:
        visual = yang if line == 1 else yin
        print(visual)

# TODO reading + line scraper
    # TODO scrape from cafeausoul
    # TODO scrape from dekorne

# TODO casting (coin method, stick method)


"""
while True:
    hex_num = int(input("Enter hexagram #: "))
    hex_lines = get_hex_lines(hex_num)
    #print(hex_lines)
    print_hex_lines(hex_lines)
"""

print(verify_sequence(sample_correct_sequence))
print(verify_sequence(sample_wrong_sequence1))
print(verify_sequence(sample_wrong_sequence2))
