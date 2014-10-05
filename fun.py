import core

def braille(start=0, end=26):
    """
    fun.braille([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is alphabet) and value is its braille
    Note: Braille of uppercase and lowercase alphabets is same.
    """

    letters = {
            'a': [[1, 0], [0, 0], [0, 0]],

           'b': [[1, 0], [1, 0], [0, 0]],

           'c': [[1, 1], [0, 0], [0, 0]],

           'd': [[1, 1], [0, 1], [0, 0]],

           'e': [[1, 0], [0, 1], [0, 0]],

           'f': [[1, 1], [1, 0], [0, 0]],

           'g': [[1, 1], [1, 1], [0, 0]],

           'h': [[1, 0], [1, 1], [0, 0]],

           'i': [[0, 1], [1, 0], [0, 0]],

           'j': [[0, 1], [1, 1], [0, 0]],

           'k': [[1, 0], [0, 0], [1, 0]],

           'l': [[1, 0], [1, 0], [1, 0]],

           'm': [[1, 1], [0, 0], [1, 0]],

           'n': [[1, 1], [0, 1], [1, 0]],

           'o': [[1, 0], [0, 1], [1, 0]],

           'p': [[1, 1], [1, 0], [1, 0]],

           'q': [[1, 1], [1, 1], [1, 0]],

           'r': [[1, 0], [1, 1], [1, 0]],

           's': [[0, 1], [1, 0], [1, 0]],

           't': [[0, 1], [1, 1], [1, 0]],

           'u': [[1, 0], [0, 0], [1, 1]],

           'v': [[1, 0], [1, 0], [1, 1]],

           'w': [[0, 1], [1, 1], [0, 1]],

           'x': [[1, 1], [0, 0], [1, 1]],

           'y': [[1, 1], [0, 1], [1, 1]],

           'z': [[1, 0], [0, 1], [1, 1]]
    }

    d = core.dic(0,start,end)
    for i in d:
        d[i] = letters[i]
    return d


def lipsum():
    """
    Returns filler text, lorem ipsum.
    """
    lorem = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed \
do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim \
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip \
ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate \
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat \
cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id \
est laborum."
    return lorem


def morse(char):
    """
    fun.morse(char) -> list

    input is a single alphabet.

    Returns morse notation of the alphabet in "dots and dashes" and
    "dits and dahs" forms, in a list.
    """
    if not char.isalpha() or len(char) > 1:
        raise Exception("Not a valid input!! Give in a single character.")

    letters = {
            'a': ['._', 'dit-dah'],
            'b': ['_...', 'dah-di-di-dit'],
            'c': ['_._.', 'dah-di-dah-dit'],
            'd': ['_..', 'dah-di-dit'],
            'e': ['.', 'dit'],
            'f': ['.._.', 'di-di-dah-dit'],
            'g': ['__.', 'dah-dah-dit'],
            'h': ['....', 'di-di-di-dit'],
            'i': ['..', 'di-dit'],
            'j': ['.___', 'di-dah-dah-dah'],
            'k': ['_._', 'dah-di-dah'],
            'l': ['._..', 'di-dah-di-dit'],
            'm': ['__', 'dah-dah'],
            'n': ['_.', 'dah-dit'],
            'o': ['___', 'dah-dah-dah'],
            'p': ['.__.', 'di-dah-dah-dit'],
            'q': ['__._', 'dah-dah-di-dah'],
            'r': ['._.', 'di-dah-dit'],
            's': ['...', 'di-di-dit'],
            't': ['-', 'dah'],
            'u': ['.._', 'di-di-dah'],
            'v': ['..._', 'di-di-di-dah'],
            'w': ['.__', 'di-dah-dah'],
            'x': ['_.._', 'dah-di-di-dah'],
            'y': ['_.__', 'dah-di-dah-dah'],
            'z': ['__..', 'dah-dah-di-dit']
    }

    return letters[char.lower()]


def nato(char):
    """
    fun.nato(char) -> list

    input is a single alphabet.

    Returns NATO notation of the alphabet.`
    """
    if not char.isalpha() or len(char) != 1:
        raise Exception("Not a valid input!! Give in a single character.")

    letters = {
            'a': 'Alfa',
            'b': 'Bravo',
            'c': 'Charlie',
            'd': 'Delta',
            'e': 'Echo',
            'f': 'Foxtrot',
            'g': 'Golf',
            'h': 'Hotel',
            'i': 'India',
            'j': 'Juliett',
            'k': 'Kilo',
            'l': 'Lima',
            'm': 'Mike',
            'n': 'November',
            'o': 'Oscar',
            'p': 'Papa',
            'q': 'Ouebec',
            'r': 'Romeo',
            's': 'Sierra',
            't': 'Tango',
            'u': 'Uniform',
            'v': 'Victor',
            'w': 'Whiskey',
            'x': 'X-ray',
            'y': 'Yankee',
            'z': 'Zulu'
    }

    return letters[char.lower()]


def pronun(char):
    """
    fun.pronun(char) -> list

    input is a single alphabet.

    Returns the letter name to pronunciation dictionary of the alphabet.
    """
    if not char.isalpha() or len(char) != 1:
        raise Exception("Not a valid input!! Give in a single character.")

    letters = {
            'a': {
                'a': '/ˈeɪ/'
            },
            'b': {
                'bee': '/ˈbiː/'
            },
            'c': {
                'cee': '/ˈsiː/'
            },
            'd': {
                'dee': '/ˈdiː/'
            },
            'e': {
                'e': '/ˈiː/'
            },
            'f': {
                'ef': '/ˈɛf/'
            },
            'g': {
                'gee': '/ˈdʒiː/'
            },
            'h': {
                'aitch': '/ˈeɪtʃ/',
                'haitch': '/ˈheɪtʃ/',
                'hetch': '/ˈhetʃ/'
            },
            'i': {
                'i': '/ˈaɪ/'
            },
            'j': {
                'jay': '/ˈdʒeɪ/',
                'jy': '/ˈdʒaɪ/'
            },
            'k': {
                'kay': '/ˈkeɪ/'
            },
            'l': {
                'el': '/ˈɛl/'
            },
            'm': {
                'em': '/ˈɛm/'
            },
            'n': {
                'en': '/ˈɛn/'
            },
            'o': {
                'o': '/ˈəʊ/'
            },
            'p': {
                'pee': '/ˈpiː/'
            },
            'q': {
                'cue': '/ˈkjuː/'
            },
            'r': {
                'ar': '/ˈɑː/'
            },
            's': {
                'ess': '/ˈɛs/',
                'es': '/ˈɛs/'
            },
            't': {
                'tee': '/ˈtiː/'
            },
            'u': {
                'u': '/ˈjuː/'
            },
            'v': {
                'vee': '/ˈviː/'
            },
            'w': {
                'double-u': '/ˈdʌbəl.juː/'
            },
            'x': {
                'ex': '/ˈɛks/'
            },
            'y': {
                'wy': '/ˈwaɪ/',
                'wye': '/ˈwaɪ/'
            },
            'z': {
                'zed': '/ˈzɛd/',
                'zee': '/ˈziː/',
                'izzard': '/ˈɪzərd/'
            }
    }

    return letters[char.lower()]