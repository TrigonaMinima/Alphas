import string
from itertools import permutations


def alph(start=0, end=26):
    """
    core.alph([start, [end]]) -> str

    Returns a string of alphabets in lowercase from start till end. By default the start
    is 0 and end is 26.
    """
    return string.ascii_lowercase[start:end]


def ualph(start=0, end=26):
    """
    core.ualph([start, [end]]) -> str

    Returns a string of alphabets in uppercase from start till end. By default the start
    is 0 and end is 26.
    """
    return string.ascii_uppercase[start:end]


def alphlist(start=0, end=26):
    """
    core.alphlist([start, [end]]) -> list

    Returns a list of alphabets in lowercase from start till end. By default the start
    is 0 and end is 26.
    """
    return list(alph(start, end))


def ualphlist(start=0, end=26):
    """
    core.ualphlist([start, [end]]) -> list

    Returns a list of alphabets in uppercase from start till end. By default the start
    is 0 and end is 26.
    """
    return list(ualph(start, end))


def dic(value='', start=0, end=26):
    """
    core.dic([value, [start, [end]]]) -> dict

    Returns a dict of alphabets (key is lowercase alphabet and value is 'value') from
    start till end. Value is by default '', but can be anything. Every dict key will
    correspond to the same value. By default the start is 0 and end is 26.
    """
    d = {}
    for a in alphlist(start, end):
        d[a] = value

    return d


def udic(value='', start=0, end=26):
    """
    core.udic([value, [start, [end]]]) -> dict

    Returns a dict of alphabets (key is uppercase alphabet and value is 'value') from
    start till end. Value is by default '', but can be anything. Every dict key will
    correspond to the same value. By default the start is 0 and end is 26.
    """
    d = {}
    for a in ualphlist(start, end):
        d[a] = value

    return d


def ascii(start=0, end=26):
    """
    core.ascii([start, [end]]) -> dict

    Returns a dict of alphabets (key is lowerercase alphabet and value is ascii value) from
    start till end. By default the start is 0 and end is 26.
    """
    asci = {}
    for i in alph():
        asci[i] = ord(i)
    return asci


def uascii(start=0, end=26):
    """
    core.uascii([start, [end]]) -> dict

    Returns a dict of alphabets (key is uppercase alphabet and value is ascii value) from
    start till end. By default the start is 0 and end is 26.
    """
    asci = {}
    for i in ualph():
        asci[i] = ord(i)
    return asci


# check #
def permalpha(start=0, end=20):
    """
    core.permalpha([start, [end]]) -> list

    Returns a list of permutations of alphabets (lowercase) from start
    till end.By default the start is 0 and end is 26.
    """
    perms = [''.join(p) for p in permutations(alph(start,end))]
    return perms


def upermalpha(start=0, end=20):
    """
    core.upermalpha([start, [end]]) -> list

    Returns a list of permutations of alphabets (uppercase) from start
    till end.By default the start is 0 and end is 26.
    """
    perms = [''.join(p) for p in permutations(ualph(start,end))]
    return perms


def lexicographically_next_perm(a):
    """
    core.lexicographically_next_perm(a) -> boolean

    Generates the lexicographically next permutation.

    Input: a permutation, called "a". This method modifies
    "a" in place. Returns True if we could generate a next
    permutation. Returns False if it was the last permutation
    lexicographically.
    """
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i+1]):
        i -= 1
    if i < 0:
        return False
    # else
    j = len(a) - 1
    while not (a[j] > a[i]):
        j -= 1
    a[i], a[j] = a[j], a[i]        # swap
    a[i+1:] = reversed(a[i+1:])    # reverse elements from position i+1 till the end of the sequence
    return True


def lex(start=0, end=20):
    '''
    core.lex([start, [end]]) -> prints list

    Generates all the lexicographically next permutations of alphabets (lowercase)
    from start till end.By default the start is 0 and end is 26.
    '''
    li = alphlist(start, end)
    print(li)
    while lexicographically_next_perm(li):
        print(li)


def ulex(start=0, end=20):
    '''
    core.ulex([start, [end]]) -> prints list

    Generates all the lexicographically next permutations of alphabets (uppercase)
    from start till end.By default the start is 0 and end is 26.
    '''
    li = ualphlist(start, end)
    print(li)
    while lexicographically_next_perm(li):
        print(li)


#if __name__ == '__main__':
#   print alph()
#   print ualph()
#   print alphlist()
#   print dic()
#   print bi()
#   print oct()
#   print hex()
#   print rotalpha()
#   print upermalpha(0,4)
#   ulex(2,7)
