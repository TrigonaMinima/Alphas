import core

def permu(s):
    """
    algo.permu(s) -> list

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
    algo.permalgo([start,[end]]) -> list

    Returns a list containing all the permutations of the string of alphabets (lowercase) from start to end
    By default start is 0 and end is 26.
    """
    return permu(core.alph(start, end))


def upermalgo(start=0, end=26):
    """
    algo.upermalgo([start,[end]]) -> list

    Returns a list containing all the permutations of the string of alphabets (uppercase) from start to end
    By default start is 0 and end is 26.
    """
    return permu(core.ualph(start,end))
