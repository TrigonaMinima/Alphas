from Alphas import core

def binary(char):
    """
    numsys.binary(char) -> int

    Returns binary value of any alphabet.
    """
    return "{0:b}".format(ord(char))


def bi(start=0,end=26):
    """
    numsys.bi([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet) and their ascii
    codes in binary as the value.
    """
    bi = {}
    for a in core.alist(start,end):
        bi[a] = binary(a)
    return bi


def ubi(start=0,end=26):
    """
    numsys.ubi([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet) and their ascii
    codes in binary as the value.
    """
    bi = {}
    for a in core.ualist(start,end):
        bi[a] = binary(a)
    return bi


def octal(char):
    """
    numsys.octal(char) -> int

    Returns octal value of any alphabet.
    """
    return "{0:o}".format(ord(char))


def oct(start=0,end=26):
    """
    numsys.oct([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet) and their ascii
    codes in octal as the value.
    """
    octa = {}
    for a in core.alist(start,end):
        octa[a] = octal(a)
    return octa


def uoct(start=0,end=26):
    """
    numsys.uoct([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet) and their ascii
    codes in octal as the value.
    """
    octa = {}
    for a in core.ualist(start,end):
        octa[a] = octal(a)
    return octa


def hexadecimal(char):
    """
    numsys.hexa(char) -> int

    Returns hexadecimal value of any alphabet.
    """
    return "{0:x}".format(ord(char))


def hex(start=0,end=26):
    """
    numsys.hex([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet) and their ascii
    codes in hexadecimal as the value.
    """
    hexa = {}
    for a in core.alist(start,end):
        hexa[a] = hexadecimal(a)
    return hexa


def uhex(start=0,end=26):
    """
    numsys.uhex([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet) and their ascii
    codes in hexadecimal as the value.
    """
    hexa = {}
    for a in core.ualist(start,end):
        hexa[a] = hexadecimal(a)
    return hexa