Alphas.py
======

Play with alphabets.

This module is for fun. It will try to do straight forward things which can be done with the alphabets.

### Usage

#### Import

```
from Alphas import core, crypt, fun, numsys
```

#### Core functions

```
>>>
>>> Alphas.core.alph(0,23)
'abcdefghijklmnopqrstuvw'
>>>
>>> Alphas.core.ualph(0,23)
'ABCDEFGHIJKLMNOPQRSTUVW'
>>>
>>> Alphas.core.alist(4,20)
['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
>>>
>>> Alphas.core.ualist(4,20)
['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
>>>
>>> Alphas.core.dic(0,2,6)
{'f': 0, 'c': 0, 'd': 0, 'e': 0}
>>>
>>> Alphas.core.udic(0,2,6)
{'E': 0, 'D': 0, 'C': 0, 'F': 0}
>>>
>>> Alphas.core.ascii(5,10)
{'i': 105, 'g': 103, 'h': 104, 'f': 102, 'j': 106}
>>>
>>> Alphas.core.uascii(5,10)
{'I': 73, 'G': 71, 'H': 72, 'F': 70, 'J': 74}
>>>
>>> Alphas.core.vowel()
['a', 'e', 'i', 'o', 'u']
>>>
>>> Alphas.core.uvowel()
['A', 'E', 'I', 'O', 'U']
>>>
>>> ac.consonants()
['q', 'j', 'r', 'z', 't', 'f', 'c', 'n', 's', 'y', 'b', 'h', 'w', 'm', 'v', 'g', 'x', 'l', 'k', 'd', 'p']
>>>
>>> ac.uconsonants()
['S', 'X', 'Y', 'C', 'N', 'L', 'K', 'B', 'F', 'W', 'H', 'J', 'M', 'T', 'G', 'P', 'V', 'D', 'Q', 'Z', 'R']
>>>
>>> Alphas.core.perm(0,3)
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
>>>
>>> Alphas.core.uperm(1,4)
['BCD', 'BDC', 'CBD', 'CDB', 'DBC', 'DCB']
>>>
>>> Alphas.core.cyclic(0,5)
['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd']
>>>
>>> Alphas.core.ucyclic(0,5)
['ABCDE', 'BCDEA', 'CDEAB', 'DEABC', 'EABCD']
>>>
```

#### Crypt functions

```
>>>
>>> Alphas.crypt.freqal("This module is for fun. It will try to do straight forward things which can be done with the alphabets.")
{'d': 4, 'i': 8, 'v': 0, 'p': 1, 'u': 2, 'y': 1, 'a': 5, 'b': 2, 'x': 0, 'o': 6, 'j': 0, 'q': 0, 'c': 2, 'e': 5, 'g': 2, 'h': 8, 'k': 0, 'z': 0, 'f': 3, 'n': 4, 'm': 1, 'w': 4, 'r': 5, 's': 5, 't': 10, 'l': 4}
>>>
>>> Alphas.crypt.rot(13,2,6)
{'c': 'p', 'd': 'q', 'f': 's', 'e': 'r'}
>>>
>>> Alphas.crypt.urot(13,2,6)
{'C': 'P', 'E': 'R', 'D': 'Q', 'F': 'S'}
>>>
```

#### NumSys functions

```
>>>
>>> Alphas.numsys.binary('b')
'1100010'
>>>
>>> Alphas.numsys.binary('B')
'1000010'
>>>
>>> Alphas.numsys.bi(0,4)
{'c': '1100011', 'd': '1100100', 'a': '1100001', 'b': '1100010'}
>>>
>>> Alphas.numsys.ubi(0,4)
{'C': '1000011', 'A': '1000001', 'D': '1000100', 'B': '1000010'}
>>>
>>> Alphas.numsys.octal('Z')
'132'
>>>
>>> Alphas.numsys.octal('z')
'172'
>>>
>>> Alphas.numsys.oct(20,26)
{'z': '172', 'y': '171', 'v': '166', 'u': '165', 'w': '167', 'x': '170'}
>>>
>>> Alphas.numsys.uoct(20,26)
{'Y': '131', 'W': '127', 'U': '125', 'V': '126', 'X': '130', 'Z': '132'}
>>>
>>> Alphas.numsys.hexadecimal('S')
'53'
>>>
>>> Alphas.numsys.hexadecimal('s')
'73'
>>>
>>> Alphas.numsys.hex(2,7)
{'c': '63', 'd': '64', 'g': '67', 'f': '66', 'e': '65'}
>>>
>>> Alphas.numsys.uhex(2,7)
{'C': '43', 'G': '47', 'E': '45', 'D': '44', 'F': '46'}
>>>
```

#### Fun functions

```
>>>
>>> Alphas.fun.braille(3,5)
{'d': [[1, 1], [0, 1], [0, 0]], 'e': [[1, 0], [0, 1], [0, 0]]}
>>>
>>> Alphas.fun.morse('S')
['...', 'di-di-dit']
>>>
>>> Alphas.fun.morse('Z')
['__..', 'dah-dah-di-dit']
>>>
>>> Alphas.fun.nato('A')
'Alfa'
>>>
>>> Alphas.fun.nato('d')
'Delta'
>>>
>>> Alphas.fun.pronun('e')
{'e': '/ˈiː/'}
>>>
>>> Alphas.fun.pronun('z')
{'izzard': '/ˈɪzərd/', 'zee': '/ˈziː/', 'zed': '/ˈzɛd/'}
>>>
>>> Alphas.fun.song()
A
B
C
D
E
F
G
H
I
J
K
LMNO
P
Q
R
S
T
U
V
W
X
Y
and
Z
Now I know my ABCs
Next time, won't you sing with me?
>>>
>>> Alphas.fun.lovesong()
A, you're adorable
B, you're so beautiful
C, you're a cutie full of charms
D, you're a darling
And E, you're exciting
And F, you're a feather in my arms
G, you look good to me
H, you're so heavenly
I, you're the one I idolize
J, we're like Jack and Jill
K, you're so kissable
L, is the love light in your eyes
M, N, O, P
I could go on all day
Q, R, S, T
Alphabetically speaking: "You're OK"
U, made my life complete
V, means you're very sweet
W, X, Y, Z
It's fun to wander through the alphabet with you to tell you what you mean to me.
>>>
>>> Alphas.fun.country('A')
['Abkhazia', 'Afghanistan', 'Akrotiri and Dhekelia(United Kingdom)', 'Albania', 'Algeria', 'American Samoa(United States)', 'Andorra', 'Angola', 'Anguilla(United Kingdom)', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba(Netherlands)', 'Ashmore and Cartier Islands(Australia)', 'Australia', 'Austria', 'Azerbaijan']
>>>
>>> Alphas.fun.country('Z')
['Zambia', 'Zimbabwe']
>>>
```

You can suggest more...