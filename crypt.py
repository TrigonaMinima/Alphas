from core import *

def freqal(text):
    """
    crypt.freqal(text) -> dict

    Returns a dictionary with alphabets as keys and their occurrence in the text
    as the value.
    """
    text = text.lower()
    extra = '1234567890~`!@#$%^&*()-=_+|}{[]:\";\'\\<>,.?/ '
    for i in extra:
        text = text.replace(i, '')
    freq = dic(0)
    for i in text:
        freq[i] += 1

    return freq


def rot(rotv=13, start=0, end=26):
    """
    crypt.rot([rotv, [start, [end]]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet and value is
    rotated alphabet) from start till end. Rot value is by default 13, but can
    be anything. By default the start is 0 and end is 26.
    """
    d = {}
    for a in alphlist(start, end):
        if (rotv + start < 26):
          d[a] = alph(start+rotv,start+rotv+1)
        else :
          d[a] = alph(start+rotv-26,start+rotv-26+1)
        start += 1
    return d


def urot(rotv=13, start=0, end=26):
    """
    crypt.urot([rotv, [start, [end]]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet and value is
    rotated alphabet) from start till end. Rot value is by default 13, but can
    be anything. By default the start is 0 and end is 26.
    """
    d = {}
    for a in ualphlist(start, end):
        if (rotv + start < 26):
          d[a] = ualph(start+rotv,start+rotv+1)
        else :
          d[a] = ualph(start+rotv-26,start+rotv-26+1)
        start += 1
    return d   
def braille(start=0, end=26):
    """
    crypt.braille([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is alphabet) and value is its braille
    Note : Braille of uppercase and lowercase alphabets is same.
    """
    letters = {'a' : [[1, 0],
                  [0, 0],
                  [0, 0]],
          
           'b' : [[1, 0],
                  [1, 0],
                  [0, 0]],
          
           'c' : [[1, 1],
                  [0, 0],
                  [0, 0]],
          
           'd' : [[1, 1],
                  [0, 1],
                  [0, 0]],
          
           'e' : [[1, 0],
                  [0, 1],
                  [0, 0]],

           'f' : [[1, 1],
                  [1, 0],
                  [0, 0]],

           'g' : [[1, 1],
                  [1, 1],
                  [0, 0]],

           'h' : [[1, 0],
                  [1, 1],
                  [0, 0]],

           'i' : [[0, 1],
                  [1, 0],
                  [0, 0]],

           'j' : [[0, 1],
                  [1, 1],
                  [0, 0]],

           'k' : [[1, 0],
                  [0, 0],
                  [1, 0]],

           'l' : [[1, 0],
                  [1, 0],
                  [1, 0]],

           'm' : [[1, 1],
                  [0, 0],
                  [1, 0]],

           'n' : [[1, 1],
                  [0, 1],
                  [1, 0]],

           'o' : [[1, 0],
                  [0, 1],
                  [1, 0]],

           'p' : [[1, 1],
                  [1, 0],
                  [1, 0]],

           'q' : [[1, 1],
                  [1, 1],
                  [1, 0]],

           'r' : [[1, 0],
                  [1, 1],
                  [1, 0]],

           's' : [[0, 1],
                  [1, 0],
                  [1, 0]],
          
           't' : [[0, 1],
                  [1, 1],
                  [1, 0]],

           'u' : [[1, 0],
                  [0, 0],
                  [1, 1]],

           'v' : [[1, 0],
                  [1, 0],
                  [1, 1]],

           'w' : [[0, 1],
                  [1, 1],
                  [0, 1]],

           'x' : [[1, 1],
                  [0, 0],
                  [1, 1]],

           'y' : [[1, 1],
                  [0, 1],
                  [1, 1]],

           'z' : [[1, 0],
                  [0, 1],
                  [1, 1]]}
    d = dic(0,start,end)
    for i in d:
        d[i] = letters[i]  
    return d