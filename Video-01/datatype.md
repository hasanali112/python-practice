# Data type

- Number : 123, 3.14, 3+4j, 0b11, Decimal(), Fraction(), 0o37, 0x2d

- String : 'spam', "Bob's", b'a\x01c', u'sp\c4m'

- Boolean : True, False

- List : [1, 2, 3], ['a', 'b', 'c'], [1, 'a', 'b', 'c']

- Tuple : (1, 2, 3), ('a', 'b', 'c'), (1, 'a', 'b', 'c')

- Set : {1, 2, 3}, {'a', 'b', 'c'}

- Dictionary : {1: 'a', 2: 'b', 3: 'c'}, {'a': 1, 'b': 2, 'c': 3}

- None: None(empty reference)
- Functions, modules, classes

- Advanced: Decorators, Generators, Iterators, MetaProgramming.

video

Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun 6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

> > > 12+12
> > > 24
> > > 2.5 \* 5
> > > 12.5
> > > 2 ** 4
> > > 16
> > > 2 ** 100
> > > 1267650600228229401496703205376
> > > import math
> > > math.pi
> > > 3.141592653589793
> > > import random
> > > random.random
> > > <built-in method random of Random object at 0x00000206CF366BE0>
> > > random.random()
> > > 0.2601421743308905
> > > username = "chaiaouycode"
> > > len(username)
> > > 12
> > > username[0]
> > > 'c'
> > > dir(username)
> > > ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
> > > mylist =[123, "chai", 3.14]
> > > mylist
> > > [123, 'chai', 3.14]
> > > len(mylist)
> > > 3
> > > mylist[0]
> > > 123
> > > mylist[-1]
> > > 3.14
> > > mydD={"one":"lemon tea", "two":"ginger", "superman":"naagraj"}
> > > myD
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > NameError: name 'myD' is not defined. Did you mean: 'mydD'?
> > > mydD
> > > {'one': 'lemon tea', 'two': 'ginger', 'superman': 'naagraj'}
> > > mydD["superman"]
> > > 'naagraj'
> > > myTup=(1,2,4)
> > > myTup[0]
> > > 1
