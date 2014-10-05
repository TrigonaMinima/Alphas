import string
from itertools import permutations


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


def alist(start=0, end=26):
    """
    alphas.alist([start, [end]]) -> list

    Returns a list of alphabets in lowercase from start till end. By default the start
    is 0 and end is 26.
    """
    return list(alph(start, end))


def ualist(start=0, end=26):
    """
    alphas.ualist([start, [end]]) -> list

    Returns a list of alphabets in uppercase from start till end. By default the start
    is 0 and end is 26.
    """
    return list(ualph(start, end))


def dic(value='', start=0, end=26):
    """
    alphas.dic([value, [start, [end]]]) -> dict

    Returns a dict of alphabets (key is lowercase alphabet and value is 'value') from
    start till end. Value is by default '', but can be anything. Every dict key will
    correspond to the same value. By default the start is 0 and end is 26.
    """
    d = {}
    for a in alist(start, end):
        d[a] = value

    return d


def udic(value='', start=0, end=26):
    """
    alphas.udic([value, [start, [end]]]) -> dict

    Returns a dict of alphabets (key is uppercase alphabet and value is 'value') from
    start till end. Value is by default '', but can be anything. Every dict key will
    correspond to the same value. By default the start is 0 and end is 26.
    """
    d = {}
    for a in ualist(start, end):
        d[a] = value

    return d


def ascii(start=0, end=26):
    """
    alphas.ascii([start, [end]]) -> dict

    Returns a dict of alphabets (key is lowerercase alphabet and value is ascii value) from
    start till end. By default the start is 0 and end is 26.
    """
    asci = {}
    for i in alph():
        asci[i] = ord(i)
    return asci


def uascii(start=0, end=26):
    """
    alphas.uascii([start, [end]]) -> dict

    Returns a dict of alphabets (key is uppercase alphabet and value is ascii value) from
    start till end. By default the start is 0 and end is 26.
    """
    asci = {}
    for i in ualph():
        asci[i] = ord(i)
    return asci


def vowel():
    """
    core.vowel() -> list

    Returns lowercase lowercase vowels.
    """
    return ['a', 'e', 'i', 'o', 'u']


def uvowel():
    """
    core.uvowel() -> list

    Returns lowercase uppercase vowels.
    """
    return ['A', 'E', 'I', 'O', 'U']


def consonants():
    """
    core.consonants() -> list

    Returns all the lowercase consonants.
    """
    return list(set(alist()) - set(vowel())).sort()


def uconsonants():
    """
    core.uconsonants() -> list

    Returns all the uppercase consonants.
    """
    return list(set(ualist()) - set(uvowel())).sort()


# check #
def permalpha(start=0, end=20):
    """
    alphas.permalpha([start, [end]]) -> list

    Returns a list of permutations of alphabets (lowercase) from start
    till end.By default the start is 0 and end is 26.
    """
    perms = [''.join(p) for p in permutations(alph(start,end))]
    return perms


def upermalpha(start=0, end=20):
    """
    alphas.upermalpha([start, [end]]) -> list

    Returns a list of permutations of alphabets (uppercase) from start
    till end.By default the start is 0 and end is 26.
    """
    perms = [''.join(p) for p in permutations(ualph(start,end))]
    return perms


def lexicographically_next_perm(a):
    """
    alphas.lexicographically_next_perm(a) -> boolean

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
    alphas.lex([start, [end]]) -> prints list

    Generates all the lexicographically next permutations of alphabets (lowercase)
    from start till end.By default the start is 0 and end is 26.
    '''
    li = alist(start, end)
    print(li)
    while lexicographically_next_perm(li):
        print(li)


def ulex(start=0, end=20):
    '''
    alphas.ulex([start, [end]]) -> prints list

    Generates all the lexicographically next permutations of alphabets (uppercase)
    from start till end.By default the start is 0 and end is 26.
    '''
    li = ualist(start, end)
    print(li)
    while lexicographically_next_perm(li):
        print(li)


#if __name__ == '__main__':
#   print alph()
#   print ualph()
#   print alist()
#   print dic()
#   print bi()
#   print oct()
#   print hex()
#   print rotalpha()
#   print upermalpha(0,4)
#   ulex(2,7)
