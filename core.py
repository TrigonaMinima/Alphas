import string


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


def alist(start=0, end=26):
    """
    core.alist([start, [end]]) -> list

    Returns a list of alphabets in lowercase from start till end. By default the start
    is 0 and end is 26.
    """
    return list(alph(start, end))


def ualist(start=0, end=26):
    """
    core.ualist([start, [end]]) -> list

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
    for a in alist(start, end):
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
    for a in ualist(start, end):
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


def permu(s):
    """
    core.permu(s) -> list

    Returns a list of all permutations of a string.
    """
    res = []
    if len(s) == 1:
        res = [s]
    else:
        for i in range(len(s)):
            c = s[i]
            for perm in permu(s[:i] + s[i+1:]):
                res += [c + perm]

    return res


def permalgo(start=0, end=26):
    """
    core.permalgo([start, [end]]) -> list

    Returns a list containing all the permutations of the string of alphabets (lowercase) from start to end.
    By default start is 0 and end is 26.
    """
    return permu(alph(start, end))


def upermalgo(start=0, end=26):
    """
    core.upermalgo([start, [end]]) -> list

    Returns a list containing all the permutations of the string of alphabets (uppercase) from start to end.
    By default start is 0 and end is 26.
    """
    return permu(ualph(start,end))


def cyclic_rot(start=0, end=26):
    """
    core.cyclic_rot([start, [end]]) -> list

    Returns a list containing all the cyclic rotations of the string of alphabets (lowercase) from start to end.
    By default start is 0 and end is 26. 
    """
    cyclic = []
    a = alph(start, end)
    for i in range(0,len(a)):
        cyclic.append(a[i:]+a[:i])
    return cyclic


def ucyclic_rot(start=0, end=26):
    """
    core.ucyclic_rot([start, [end]]) -> list

    Returns a list containing all the cyclic rotations of the string of alphabets (uppercase) from start to end.
    By default start is 0 and end is 26. 
    """
    cyclic = []
    a = ualph(start, end)
    for i in range(0,len(a)):
        cyclic.append(a[i:]+a[:i])
    return cyclic
    

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
#   print ulex(2,7)
