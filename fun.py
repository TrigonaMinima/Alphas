# -*- coding: utf-8 -*-

from Alphas import core
import time

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
    fun.pronun(char) -> dict

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


def song():
    """
    Prints the lyrics of The Alphabet Song, with the proper time gap.
    """
    lyrics = [['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                ['H', 'I', 'J', 'K', 'LMNO', 'P'],
                ['Q', 'R', 'S'],
                ['T', 'U', 'V'],
                ['W'],
                ['X'],
                ['Y'],
                ['and','Z'],
                ['Now I know my ABCs'],
                'Next time, won\'t you sing with me?']

    for line in lyrics:
        for l in line:
            print(l)
            time.sleep(.2)
        time.sleep(1)


def lovesong():
    """
    Prints the lyrics of The Alphabet Love Song, with the proper time gap.
    """
    lyrics = ["A, you're adorable",
                "B, you're so beautiful",
                "C, you're a cutie full of charms",
                "D, you're a darling",
                "And E, you're exciting",
                "And F, you're a feather in my arms",
                "G, you look good to me",
                "H, you're so heavenly",
                "I, you're the one I idolize",
                "J, we're like Jack and Jill",
                "K, you're so kissable",
                "L, is the love light in your eyes",
                "M, N, O, P",
                "I could go on all day",
                "Q, R, S, T",
                "Alphabetically speaking: \"You're OK\"",
                "U, made my life complete",
                "V, means you're very sweet",
                "W, X, Y, Z",
                "It's fun to wander through the alphabet with you to tell you what you mean to me."]

    for line in lyrics:
        print(line)
        time.sleep(2)


def country(char):
    """
    fun.country(char) -> list

    input is a single alphabet.

    Returns a list of country names starting from alphabet char.
    """
    if not char.isalpha() or len(char) != 1:
        raise Exception("Not a valid input!! Give in a single character.")

    countries = {
            'a' : ['Abkhazia', 'Afghanistan',
                    'Akrotiri and Dhekelia(United Kingdom)', 'Albania', 'Algeria',
                    'American Samoa(United States)','Andorra', 'Angola',
                    'Anguilla(United Kingdom)', 'Antarctica', 'Antigua and Barbuda',
                    'Argentina', 'Armenia', 'Aruba(Netherlands)',
                    'Ashmore and Cartier Islands(Australia)', 'Australia',
                    'Austria', 'Azerbaijan'],
            'b' : ['Bahamas','Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                    'Belgium', 'Belize', 'Benin', 'Bermuda(United Kingdom)',
                    'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana',
                    'Bouvet Island(Norway)', 'Brazil',
                    'British Indian Ocean Territory(United Kingdom)',
                    'British Virgin Islands(United Kingdom)', 'Brunei', 'Bulgaria',
                    'Burkina Faso', 'Burundi'],
            'c' : ['Cambodia', 'Cameroon', 'CanadaChina', 'Cape Verde',
                    'Cayman Islands(United Kingdom)', 'Central African Republic',
                    'Chad', 'Chile', 'Christmas Island(Australia)',
                    'Clipperton Island(France)', 'Cocos (Keeling) Islands(Australia)',
                    'Colombia', 'Comoros', 'Cook Islands(New Zealand)',
                    'Coral Sea Islands(Australia)', 'Costa Rica', 'Cote d Ivoire',
                    'Croatia', 'Cuba', 'Curacao(Netherlands)', 'Cyprus',
                    'Czech Republic'],
            'd' : ['Democratic Republic of the Congo', 'Denmark', 'Djibouti',
                    'Dominica', 'Dominican Republic'],
            'e' : ['East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
                    'Eritrea', 'Estonia', 'Ethiopia'],
            'f' : ['Falkland Islands(United Kingdom)', 'Faroe Islands(Denmark)',
                    'Federated States of Micronesia', 'Fiji', 'Finland',
                    'French Polynesia(France)',
                    'French Southern and Antarctic Lands(France)'],
            'g' : ['Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
                    'Gibraltar(United Kingdom)', 'Greece', 'Greenland', 'Grenada',
                    'Guam(United States)', 'Guatemala', 'Guernsey(United Kingdom)',
                    'Guinea', 'Guinea-Bissau', 'Guyana'],
            'h' : ['Haiti', 'Heard Island and McDonald Islands(Australia)',
                    'Honduras', 'Hong Kong(China)', 'Hungary'],
            'i' : ['Iceland', 'India', 'Indonesia', 'Iran', 'Iraq',
                    'Isle of Man(British Crown Dependency)', 'Israel', 'Italy'],
            'j' : ['Jamaica', 'Jan Mayen(Norway)', 'Japan',
                    'Jersey(United Kingdom)', 'Jordan'],
            'k' : ['Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait',
                    'Kyrgyzstan'],
            'l' : ['Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
                    'Liechtenstein', 'Lithuania', 'Luxembourg'],
            'm' : ['Macau(China)', 'Macedonia', 'Madagascar', 'Malawi',
                    'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
                    'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco',
                    'Metropolitan France&overseas regions(France)',
                    'Mongolia', 'Montenegro', 'Montserrat(United Kingdom)',
                    'Morocco', 'Mozambique', 'Myanmar'],
            'n' : ['Nagorno-Karabakh', 'Namibia', 'Nauru', 'Niger', 'Nigeria',
                    'Navassa Island(disputed)', 'Nepal', 'Netherlands',
                    'New Caledonia(France)', 'New Zealand', 'Nicaragua',
                    'Niue(New Zealand)', 'Norfolk Island(Australia)', 'North Korea',
                    'Northern Cyprus', 'Northern Mariana Islands(United States)',
                    'Norway'],
            'o' : ['Oman'],
            'p' : ['Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay',
                    'Peru', 'Philippines', 'Pitcairn Islands(United Kingdom)',
                    'Poland', 'Portugal', 'Puerto Rico(United States)'],
            'q' : ['Qatar'],
            'r' : ['Republic of Ireland', 'Republic of the Congo', 'Romania',
                    'Russia', 'Rwanda'],
            's' : ['Saint Barthelemy(France)', 'Saint Kitts and Nevis',
                    'Saint Helena, Ascension and Tristan da Cunha(United Kingdom)',
                    'Saint Lucia', 'Saint Martin(France)', 'Samoa', 'San Marino',
                    'Saint Pierre and Miquelon(France)', 'Sao Tome and Principe',
                    'Saint Vincent and the Grenadines', 'Saudi Arabia',
                    'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore',
                    'Sint Maarten(Netherlands)', 'Slovakia', 'Slovenia', 'Somalia',
                    'Solomon Islands', 'Somaliland', 'South Africa', 'South Korea',
                    'South Georgia and the South Sandwich Islands(United Kingdom)',
                    'South Ossetia', 'South Sudan', 'Spain', 'Spratly Islands(disputed)',
                    'Sri Lanka', 'State of Palestine', 'Sudan', 'Suriname',
                    'Svalbard(Norway)', 'Swaziland', 'Sweden', 'Switzerland', 'Syria'],
            't' : ['Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo',
                    'Tokelau(New Zealand)', 'Tonga', 'Transnistria',
                    'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                    'Turks and Caicos Islands(United Kingdom)', 'Tuvalu'],
            'u' : ['U.S. Virgin Islands(United States)', 'Uganda', 'Ukraine',
                    'United Arab Emirates', 'United Kingdom', 'United States',
                    'United States Pacific Island Wildlife Refuges', 'Uruguay',
                    'Uzbekistan'],
            'v' : ['Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam'],
            'w' : ['Wake Island(United States)', 'Wallis and Futuna(France)',
                    'Western Sahara'],
            'y' : ['Yemen'],
            'z' : ['Zambia', 'Zimbabwe']
        }

    return countries[char.lower()]

