import string


def alph(start=0, end=-1):
    """
    alphas.alph([start, [end]]) -> str

    Returns a string of alphabets in lowercase from start till end. By default the start
    is 0 and end is 26.
    """
    return string.ascii_lowercase[start:end]


def ualph(start=0, end=-1):
    """
    alphas.ualph([start, [end]]) -> str

    Returns a string of alphabets in uppercase from start till end. By default the start
    is 0 and end is 26.
    """
    return string.ascii_uppercase[start:end]


def alphlist(start=0, end=-1):
    """
    alphas.alphlist([start, [end]]) -> list

    Returns a list of alphabets in lowercase from start till end. By default the start
    is 0 and end is 26.
    """
    return list(alph(start, end))


def ualphlist(start=0, end=-1):
    """
    alphas.uAlphlist([start, [end]]) -> list

    Returns a list of alphabets in uppercase from start till end. By default the start
    is 0 and end is 26.
    """
    return list(uAlph(start, end))


def dicalph(value='', start=0, end=-1):
    """
    alphas.dicAlph([value, [start, [end]]]) -> dict

    Returns a dict of alphabets (key is lowercase alphabet and value is 'value') from
    start till end. Value is by default '', but can be anything. Every dict key will
    correspond to the same value. By default the start is 0 and end is 26.
    """
    d = {}
    for a in alphlist(start, end):
      d[a] = value

    return d


def udicalph(value='', start=0, end=-1):
    """
    alphas.dicAlph([value, [start, [end]]]) -> dict

    Returns a dict of alphabets (key is uppercase alphabet and value is 'value') from
    start till end. Value is by default '', but can be anything. Every dict key will
    correspond to the same value. By default the start is 0 and end is 26.
    """
    d = {}
    for a in uAlphlist(start, end):
      d[a] = value

    return d


def dict_bi():
  bi = {}
  for a in alphlist():
    bi[a] = "{0:b}".format(ord(a))
  return bi


def dict_oct():
  octa = {}
  for a in alphlist():
    octa[a] = "{0:o}".format(ord(a))
  return octa


def dict_hex():
  hexa = {}
  for a in alphlist():
    hexa[a] = "{0:x}".format(ord(a))
  return hexa


# if __name__ == '__main__':
#   print loweralph()
#   print upperalph()
#   print alphlist()
#   print dicalpha()
#   print dict_bi()
#   print dict_oct()
#   print dict_hex()

