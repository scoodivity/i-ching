import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logging.disable(logging.CRITICAL)

basic_trigrams = {
    'heaven':   (1, 1, 1),
    'lake':     (0, 0, 1),
    'flame':    (0, 1, 0),
    'thunder':  (1, 0, 0),
    'wind':     (0, 0, 0),
    'water':    (1, 1, 0),
    'mountain': (1, 0, 1),
    'earth':    (0, 1, 1),
    }

hex_details = {
    1: ('force', ('heaven', 'heaven')), 
    2: ('field', ('earth', 'earth')),
    3: ('sprouting', ('water', 'thunder')), 
    5: ('waiting', ('water', 'heaven')),
    7: ('the army', ('earth', 'water')),
    9: ('the taming power of the small', ('wind', 'heaven')),
    11: ('peace', ('earth', 'heaven')),
    13: ('fellowship with men', ()),
    15: ('modesty', ()),
    17: ('following', ()),
    19: ('approach', ()),
    21: ('biting through', ()),
    23: ('splitting apart', ()),
    25: ('innocence (the unexpected)', ()),
    27: ('the corners of the mouth (providing nourishment)', ()),
    28: ('preponderance of the great', ()),
    29: ('the abysmal (water)', ()),
    30: ('the clinging, fire', ()),
    31: ('influence', ()),
    33: ('retreat', ()),
    35: ('progress', ()),
    37: ('the family (the clan)', ()),
    39: ('obstruction', ()),
    41: ('decrease', ()),
    43: ('break-through (resoluteness)', ()),
    45: ('gathering together (massing)', ()),
    47: ('oppression (exhaustion)', ()),
    49: ('revolution (molting)', ()),
    51: ('the arousing (shock, thunder)', ()),
    53: ('development (gradual progress)', ()),
    55: ('abundance', ()),
    57: ('the gentle (the penetrating, wind)', ()),
    59: ('dispersion (dissolution)', ()),
    61: ('inner truth', ()),
    62: ('preponderance of the small', ()),
    63: ('after completion', ()),

    }

def get_hex_lines(hex_number):
    """Makes hexagram sequence from basic_trigrams and hex_instruct."""
    hex_lines = []

    for trigram in hex_details[hex_number][1]:
        hex_lines += basic_trigrams[trigram]

    return hex_lines

# TODO verify changing lines

def print_hex_lines(hex_lines):
    yang = '▀▀▀▀▀▀▀▀▀▀▀'    #'▀▀▀▀▀✖▀▀▀▀▀'
    yin =  '▀▀▀▀   ▀▀▀▀'    #'▀▀▀▀ ✖ ▀▀▀▀'

    for line in hex_lines:
        visual = yang if line == 1 else yin
        print(visual)

# TODO reading + line scraper
    # TODO scrape from cafeausoul
    # TODO scrape from dekorne

hex_lines = get_hex_lines(9)
print(hex_lines)
print_hex_lines(hex_lines)
