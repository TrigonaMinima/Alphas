import core

def braille(start=0, end=26):
    """
    fun.braille([start, [end]]) -> dict

    Returns a dictionary of alphabets (key is alphabet) and value is its braille
    Note : Braille of uppercase and lowercase alphabets is same.
    """
    letters = {
            'a' : [[1, 0], [0, 0], [0, 0]],

           'b' : [[1, 0], [1, 0], [0, 0]],

           'c' : [[1, 1], [0, 0], [0, 0]],

           'd' : [[1, 1], [0, 1], [0, 0]],

           'e' : [[1, 0], [0, 1], [0, 0]],

           'f' : [[1, 1], [1, 0], [0, 0]],

           'g' : [[1, 1], [1, 1], [0, 0]],

           'h' : [[1, 0], [1, 1], [0, 0]],

           'i' : [[0, 1], [1, 0], [0, 0]],

           'j' : [[0, 1], [1, 1], [0, 0]],

           'k' : [[1, 0], [0, 0], [1, 0]],

           'l' : [[1, 0], [1, 0], [1, 0]],

           'm' : [[1, 1], [0, 0], [1, 0]],

           'n' : [[1, 1], [0, 1], [1, 0]],

           'o' : [[1, 0], [0, 1], [1, 0]],

           'p' : [[1, 1], [1, 0], [1, 0]],

           'q' : [[1, 1], [1, 1], [1, 0]],

           'r' : [[1, 0], [1, 1], [1, 0]],

           's' : [[0, 1], [1, 0], [1, 0]],

           't' : [[0, 1], [1, 1], [1, 0]],

           'u' : [[1, 0], [0, 0], [1, 1]],

           'v' : [[1, 0], [1, 0], [1, 1]],

           'w' : [[0, 1], [1, 1], [0, 1]],

           'x' : [[1, 1], [0, 0], [1, 1]],

           'y' : [[1, 1], [0, 1], [1, 1]],

           'z' : [[1, 0], [0, 1], [1, 1]]
    }

    d = core.dic(0,start,end)
    for i in d:
        d[i] = letters[i]
    return d


def lipsum():
    """
    Returns filler text, lorem ipsum.
    """
    lipsum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed \
                    do eiusmod tempor incididunt ut labore et dolore magna \
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation \
                    ullamco laboris nisi ut aliquip ex ea commodo consequat. \
                    Duis aute irure dolor in reprehenderit in voluptate velit \
                    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint\
                     occaecat cupidatat non proident, sunt in culpa qui officia \
                     deserunt mollit anim id est laborum."
    return lipsum
