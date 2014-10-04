def binary(char):
    """
    alphas.bi(char) -> int

    Returns binary value of any alphabet.
    """
    return "{0:b}".format(ord(a))


def bi(start=0,end=26):
    """
    alphas.bi([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet) and their ascii
    codes in binary as the value.
    """
    bi = {}
    for a in alphlist(start,end):
        bi[a] = binary(a)
    return bi


def ubi(start=0,end=26):
    """
    alphas.ubi([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet) and their ascii
    codes in binary as the value.
    """
    bi = {}
    for a in ualphlist(start,end):
        bi[a] = binary(a)
    return bi


def octal(char):
    """
    alphas.octal(char) -> int

    Returns binary value of any alphabet.
    """
    return "{0:o}".format(ord(a))


def oct(start=0,end=26):
    """
    alphas.oct([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet) and their ascii
    codes in octal as the value.
    """
    octa = {}
    for a in alphlist(start,end):
        octa[a] = octal(a)
    return octa


def uoct(start=0,end=26):
    """
    alphas.uoct([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet) and their ascii
    codes in octal as the value.
    """
    octa = {}
    for a in ualphlist(start,end):
        octa[a] = octal(a)
    return octa


def hexadecimal(char):
    """
    alphas.hexa(char) -> int

    Returns binary value of any alphabet.
    """
    return "{0:x}".format(ord(a))


def hex(start=0,end=26):
    """
    alphas.hex([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is lowercase alphabet) and their ascii
    codes in hexadecimal as the value.
    """
    hexa = {}
    for a in alphlist(start,end):
        hexa[a] = hexadecimal(a)
    return hexa


def uhex(start=0,end=26):
    """
    alphas.uhex([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is uppercase alphabet) and their ascii
    codes in hexadecimal as the value.
    """
    hexa = {}
    for a in ualphlist(start,end):
        hexa[a] = hexadecimal(a)
    return hexa