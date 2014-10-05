from Alphas import core


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
    freq = core.dic(0)
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
    for a in core.alist(start, end):
        if (rotv + start < 26):
          d[a] = core.alph(start+rotv,start+rotv+1)
        else :
          d[a] = core.alph(start+rotv-26,start+rotv-26+1)
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
    for a in core.ualist(start, end):
        if (rotv + start < 26):
          d[a] = core.ualph(start+rotv,start+rotv+1)
        else :
          d[a] = core.ualph(start+rotv-26,start+rotv-26+1)
        start += 1
    return d