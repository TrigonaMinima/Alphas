def freqal(text):
    """
    alphas.freqal(text) -> dict

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
    alphas.rot([rotv, [start, [end]]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet and value is
    rotated alphabet) from start till end. Rot value is by default 13, but can
    be anything. By default the start is 0 and end is 26.
    """
    d = {}
    for a in alphlist(start, end):
        if (value + start < 26):
          d[a] = alph(start+value,start+value+1)
        else :
          d[a] = alph(start+value-26,start+value-26+1)
        start += 1
    return d


def urot(rotv=13, start=0, end=26):
    """
    alphas.urot([rotv, [start, [end]]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet and value is
    rotated alphabet) from start till end. Rot value is by default 13, but can
    be anything. By default the start is 0 and end is 26.
    """
    d = {}
    for a in ualphlist(start, end):
        if (value + start < 26):
          d[a] = ualph(start+value,start+value+1)
        else :
          d[a] = ualph(start+value-26,start+value-26+1)
        start += 1
    return d