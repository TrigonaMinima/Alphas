import string


def alph(start=0, end=26):
    """
    alphas.alph([start, [end]]) -> str

    Returns a string of alphabets in lowercase from start till end. By default the start
    is 0 and end is 26.
    """
    return string.ascii_lowercase[start:end]


def ualph(start=0, end=26):
    """
    alphas.ualph([start, [end]]) -> str

    Returns a string of alphabets in uppercase from start till end. By default the start
    is 0 and end is 26.
    """
    return string.ascii_uppercase[start:end]


def alphlist(start=0, end=26):
    """
    alphas.alphlist([start, [end]]) -> list

    Returns a list of alphabets in lowercase from start till end. By default the start
    is 0 and end is 26.
    """
    return list(alph(start, end))


def ualphlist(start=0, end=26):
    """
    alphas.ualphlist([start, [end]]) -> list

    Returns a list of alphabets in uppercase from start till end. By default the start
    is 0 and end is 26.
    """
    return list(ualph(start, end))


def dicalph(value='', start=0, end=26):
    """
    alphas.dicalph([value, [start, [end]]]) -> dict

    Returns a dict of alphabets (key is lowercase alphabet and value is 'value') from
    start till end. Value is by default '', but can be anything. Every dict key will
    correspond to the same value. By default the start is 0 and end is 26.
    """
    d = {}
    for a in alphlist(start, end):
      d[a] = value

    return d


def udicalph(value='', start=0, end=26):
    """
    alphas.dicalph([value, [start, [end]]]) -> dict

    Returns a dict of alphabets (key is uppercase alphabet and value is 'value') from
    start till end. Value is by default '', but can be anything. Every dict key will
    correspond to the same value. By default the start is 0 and end is 26.
    """
    d = {}
    for a in ualphlist(start, end):
      d[a] = value

    return d


def dict_bi(start=0,end=26):
    """
    alphas.dict_bi([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet) and their ascii
    codes in binary as the value.
    """
    bi = {}
    for a in alphlist(start,end):
      bi[a] = "{0:b}".format(ord(a))
    return bi


def udict_bi(start=0,end=26):
    """
    alphas.udict_bi([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet) and their ascii
    codes in binary as the value.
    """
    bi = {}
    for a in ualphlist(start,end):
      bi[a] = "{0:b}".format(ord(a))
    return bi


def dict_oct(start=0,end=26):
    """
    alphas.dict_oct([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet) and their ascii
    codes in octal as the value.
    """
    octa = {}
    for a in alphlist(start,end):
      octa[a] = "{0:o}".format(ord(a))
    return octa


def udict_oct(start=0,end=26):
    """
    alphas.udict_oct([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet) and their ascii
    codes in octal as the value.
    """
    octa = {}
    for a in ualphlist(start,end):
      octa[a] = "{0:o}".format(ord(a))
    return octa


def dict_hex(start=0,end=26):
    """
    alphas.dict_hex([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet) and their ascii
    codes in hexadecimal as the value.
    """    
    hexa = {}
    for a in alphlist(start,end):
      hexa[a] = "{0:x}".format(ord(a))
    return hexa


def udict_hex(start=0,end=26):
    """
    alphas.udict_hex([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet) and their ascii
    codes in hexadecimal as the value.
    """    
    hexa = {}
    for a in ualphlist(start,end):
      hexa[a] = "{0:x}".format(ord(a))
    return hexa
    
    
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
    freq = dicalph(0)
    for i in text:
        freq[i] += 1

    return freq
    
    
def rotalpha(value=13, start=0, end=26):
    """
    alphas.rotalpha([value, [start, [end]]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet and value is 
    alphabet obtained after rotation) from start till end.Value is by default
    13, but can be anything.By default the start is 0 and end is 26.
    """
    d = {}
    for a in alphlist(start, end):
        if (value + start < 26):
          d[a] = alph(start+value,start+value+1)
        else :
          d[a] = alph(start+value-26,start+value-26+1)   
        start += 1  
    return d
    

def urotalpha(value=13, start=0, end=26):
    """
    alphas.urotalpha([value, [start, [end]]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet and value is 
    alphabet obtained after rotation) from start till end.Value is by default
    13, but can be anything.By default the start is 0 and end is 26.
    """
    d = {}
    for a in ualphlist(start, end):
        if (value + start < 26):
          d[a] = ualph(start+value,start+value+1)
        else :
          d[a] = ualph(start+value-26,start+value-26+1)    
        start += 1  
    return d
  
    
#if __name__ == '__main__':
#   print alph()
#   print ualph()
#   print alphlist()
#   print dicalph()
#   print dict_bi()
#   print dict_oct()
#   print dict_hex()
#   print rotalpha()

