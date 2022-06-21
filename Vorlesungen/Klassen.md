```python
class Auto:
    """
    Ein einfaches Auto.

    Kann nur fahren.
    """

    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe
        self.km_stand = 0

    def fahre(self, km):
        """Erhöhe `km_stand` um `km`. """
        self.km_stand += km  # x += 1 --> x = x + 1
```


```python
a1 = Auto('VW', 'rot')
```


```python
a1.marke
```




    'VW'




```python
a1.farbe
```




    'rot'




```python
a1.km_stand
```




    0




```python
a1.fahre(10)
```


```python
a1.km_stand
```




    10




```python
a1.fahre(15)
```


```python
a1.km_stand
```




    25




```python
a2 = Auto('BMW', 'schwarz')
```


```python
a2.marke
```




    'BMW'




```python
a2.km_stand
```




    0




```python
a2.fahre(35)
```


```python
a2.km_stand
```




    35




```python
a1.__dict__
```




    {'marke': 'VW', 'farbe': 'rot', 'km_stand': 25}




```python
dir(a1)
```




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'fahre',
     'farbe',
     'km_stand',
     'marke']




```python
a1.fahre
```




    <bound method Auto.fahre of <__main__.Auto object at 0x7fdd8a5c89d0>>




```python
Auto.__dict__
```




    mappingproxy({'__module__': '__main__',
                  '__doc__': '\n    Ein einfaches Auto.\n\n    Kann nur fahren.\n    ',
                  '__init__': <function __main__.Auto.__init__(self, marke, farbe)>,
                  'fahre': <function __main__.Auto.fahre(self, km)>,
                  '__dict__': <attribute '__dict__' of 'Auto' objects>,
                  '__weakref__': <attribute '__weakref__' of 'Auto' objects>})




```python
Auto?
```


    [0;31mInit signature:[0m [0mAuto[0m[0;34m([0m[0mmarke[0m[0;34m,[0m [0mfarbe[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m     
    Ein einfaches Auto.
    
    Kann nur fahren.
    [0;31mType:[0m           type
    [0;31mSubclasses:[0m     




```python
Auto.__doc__
```




    '\n    Ein einfaches Auto.\n\n    Kann nur fahren.\n    '




```python
Auto.fahre
```




    <function __main__.Auto.fahre(self, km)>




```python
a1.fahre
```




    <bound method Auto.fahre of <__main__.Auto object at 0x7fdd8a5c89d0>>




```python
a1.fahre(10)
```


```python
Auto.fahre(a1, 10)
```


```python
a1.km_stand
```




    45




```python
import random


class EinfachesAuto:
    """
    Ein einfaches Auto mit Vorgabefraben.

    Kann nur fahren.
    """

    vorgabe_farben = ['gelb', 'braun', 'pink']

    def __init__(self, marke, farbe=None):
        self.marke = marke
        if farbe is None:
            self.farbe = random.choice(self.vorgabe_farben)
        else:
            self.farbe = farbe
        self.km_stand = 0

    def fahre(self, km):
        """Erhöhe `km_stand` um `km`. """
        self.km_stand += km  # x += 1 --> x = x + 1
```


```python
e1 = EinfachesAuto('Skoda')
```


```python
e1.farbe
```




    'gelb'




```python
e1.__dict__
```




    {'marke': 'Skoda', 'farbe': 'gelb', 'km_stand': 0}




```python
EinfachesAuto.__dict__
```




    mappingproxy({'__module__': '__main__',
                  '__doc__': '\n    Ein einfaches Auto mit Vorgabefraben.\n\n    Kann nur fahren.\n    ',
                  'vorgabe_farben': ['gelb', 'braun', 'pink'],
                  '__init__': <function __main__.EinfachesAuto.__init__(self, marke, farbe=None)>,
                  'fahre': <function __main__.EinfachesAuto.fahre(self, km)>,
                  '__dict__': <attribute '__dict__' of 'EinfachesAuto' objects>,
                  '__weakref__': <attribute '__weakref__' of 'EinfachesAuto' objects>})




```python
e1.vorgabe_farben = ['silber', 'gold', 'platin']
```


```python
e1.vorgabe_farben
```




    ['silber', 'gold', 'platin']




```python
e1.__dict__
```




    {'marke': 'Skoda',
     'farbe': 'gelb',
     'km_stand': 0,
     'vorgabe_farben': ['silber', 'gold', 'platin']}




```python
from string import ascii_uppercase

autos = [EinfachesAuto(marke) for marke in ascii_uppercase]
```


```python
for auto in autos:
    print(auto.marke, auto.farbe)
```

    A pink
    B gelb
    C gelb
    D pink
    E pink
    F pink
    G braun
    H braun
    I braun
    J pink
    K gelb
    L pink
    M gelb
    N braun
    O gelb
    P gelb
    Q gelb
    R gelb
    S braun
    T pink
    U braun
    V pink
    W braun
    X gelb
    Y gelb
    Z gelb



```python
type(Auto)
```




    type




```python
type(int)
```




    type




```python
type(list)
```




    type




```python
[1, 2, 3]
```




    [1, 2, 3]



# Vererbung


```python
class BetriebsAuto:
    """
    Ein einfaches Auto.

    Kann nur fahren.
    """

    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe
        self.km_stand = 0
        self.fahrten = []

    def fahre(self, km):
        """Erhöhe `km_stand` um `km`. """
        self.km_stand += km
        self.fahrten.append(km)
```


```python
b1 = BetriebsAuto('VW', 'rot')
```


```python
b1.fahrten
```




    []




```python
b1.fahre(10)
```


```python
b1.km_stand
```




    10




```python
b1.fahrten
```




    [10]




```python
b1.fahre(20)
```


```python
b1.km_stand
```




    30




```python
b1.fahrten
```




    [10, 20]




```python
b1.km_stand == sum(b1.fahrten)
```




    True




```python
class LKW(BetriebsAuto):

    def fahre(self, km):
        self.km_stand += km * 2
        self.fahrten.append(km * 2)
```


```python
L1 = LKW('MAN', 'grün')
```


```python
L1.fahrten
```




    []




```python
L1.fahre(10)
```


```python
L1.km_stand
```




    20




```python
L1.fahrten
```




    [20]




```python
LKW.mro()
```




    [__main__.LKW, __main__.BetriebsAuto, object]




```python
LKW.mro?
```


    [0;31mSignature:[0m [0mLKW[0m[0;34m.[0m[0mmro[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m Return a type's method resolution order.
    [0;31mType:[0m      builtin_function_or_method




```python
class BessererLKW(BetriebsAuto):

    def fahre(self, km):
        super().fahre(km * 2)
```


```python
L2 = BessererLKW('Scania', 'weiß')
```


```python
L2.km_stand
```




    0




```python
L2.fahre(10)
```


```python
L2.km_stand
```




    20




```python
class Zugmaschine(BetriebsAuto):
    
    def __init__(self, marke, farbe, anhaenger=None):
        super().__init__(marke, farbe)
        self.anhaenger = anhaenger
```


```python
class A:
    
    def _intern(self):
        pass
    
    def __geheim(self):
        pass
```


```python
a = A()
```


```python
a._intern
```




    <bound method A._intern of <__main__.A object at 0x7fdd8a905ed0>>




```python
a._A__geheim
```




    <bound method A.__geheim of <__main__.A object at 0x7fdd8a905ed0>>



# Operatorüberladung


```python
class AddierbaresAuto:
    """
    Ein einfaches Auto.

    Kann nur fahren.
    """

    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe
        self.km_stand = 0

    def fahre(self, km):
        """Erhöhe `km_stand` um `km`. """
        self.km_stand += km

    def __add__(self, other):
        return AddierbaresAuto(self.marke + other.marke,
                               self.farbe + other.farbe)
```


```python
aa1 = AddierbaresAuto('VW', 'rot')
aa2 = AddierbaresAuto('BMW', 'schwarz')
```


```python
aa3 = aa1 + aa2
```


```python
aa3.marke
```




    'VWBMW'




```python
aa3.farbe
```




    'rotschwarz'




```python
aa4 = aa1.__add__(aa2)
```


```python
aa4.farbe
```




    'rotschwarz'




```python
z = 10
```


```python
z.__add__(6)
```




    16




```python
z + 6
```




    16




```python
def add(a, b):
    return a + b
```


```python
add(aa1, aa2)
```




    <__main__.AddierbaresAuto at 0x7fdd8a6f2a10>




```python
sum([aa1, aa2], AddierbaresAuto('', ''))
```




    <__main__.AddierbaresAuto at 0x7fdd8a6f3f40>




```python
sum?
```


    [0;31mSignature:[0m [0msum[0m[0;34m([0m[0miterable[0m[0;34m,[0m [0;34m/[0m[0;34m,[0m [0mstart[0m[0;34m=[0m[0;36m0[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
    [0;31mType:[0m      builtin_function_or_method




```python
list()
```




    []




```python
type(list)
```




    type




```python
list()
```




    []




```python
type(add)
```




    function




```python
callable(add)
```




    True




```python
callable(list)
```




    True




```python
class Counter:

    def __init__(self):
        self.counter = 0

    def __call__(self, a, b):
        self.counter += 1
        return a + b
```


```python
add2 = Counter()
```


```python
type(add2)
```




    __main__.Counter




```python
callable(add2)
```




    True




```python
add2.counter

```




    0




```python
add2(4, 5)
```




    9




```python
add2.counter
```




    1




```python
add(3, 4)
```




    7




```python
add.__call__(2, 3)
```




    5




```python
aa1
```




    <__main__.AddierbaresAuto at 0x7fdd8a3c35b0>




```python
class AddierbaresAutoRepr:
    """
    Ein einfaches Auto.

    Kann nur fahren.
    """

    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe
        self.km_stand = 0

    def fahre(self, km):
        """Erhöhe `km_stand` um `km`. """
        self.km_stand += km

    def __add__(self, other):
        return AddierbaresAuto(self.marke + other.marke,
                               self.farbe + other.farbe)
    def __repr__(self):
        return f'AddierbaresAutoRepr({self.marke!r}, {self.farbe!r})'
```


```python
ar = AddierbaresAutoRepr('VW', 'rot')
```


```python
ar
```




    AddierbaresAutoRepr('VW', 'rot')




```python
s = 'a'
```


```python
s
```




    'a'




```python
repr(s)
```




    "'a'"




```python
repr(1)
```




    '1'




```python
class AddierbaresAutoReprKind(AddierbaresAutoRepr):
    pass
```


```python
AddierbaresAutoReprKind('VW', 'rot')
```




    AddierbaresAutoRepr('VW', 'rot')




```python
class AddierbaresAutoReprBesser:
    """
    Ein einfaches Auto.

    Kann nur fahren.
    """

    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe
        self.km_stand = 0

    def fahre(self, km):
        """Erhöhe `km_stand` um `km`. """
        self.km_stand += km

    def __add__(self, other):
        return AddierbaresAuto(self.marke + other.marke,
                               self.farbe + other.farbe)
    def __repr__(self):
        return f'{self.__class__.__name__}({self.marke!r}, {self.farbe!r})'
```


```python
class AddierbaresAutoReprBesserKind(AddierbaresAutoReprBesser):
    pass
```


```python
AddierbaresAutoReprBesserKind('VW', 'rot')
```




    AddierbaresAutoReprBesserKind('VW', 'rot')




```python
# 13.2.1
class Person:
    def __init__(self, name, location):
        self.name = name
        self.location = location

# 13.2.2
    def goto(self, location):
        print(f"{self.name} went from {self.location} to {location}")
        self.location = location

# 13.4.1
    def __rshift__(self, location):
        self.goto(location)


# 13.2.3
person1 = Person("Anton", "Aurich")
person1.goto("Amberg-Sulzbach")
person2 = Person("Bernd", "Berlin")
person2.goto("Bergheim")


# 13.3.1
class LimitedPerson(Person):
    # 13.3.2
    excluded_locations = ["Berlin", "Munich", "Frankfurt"]

    def goto(self, location):
        if location is str and location not in self.excluded_locations:
            super().goto(location)
        else:
            print(f"{self.name} is not allowed to go to {location}")


person3 = LimitedPerson("Erich", "Erfurt")
person3.goto("Berlin")

person4 = LimitedPerson("Frank", "Frankfurt")

# 13.4.1
person5 = Person("August", "Augsburg")
person5 >> "Amsterdam"
person6 = LimitedPerson("Emil", "Einbeck")
person6 >> "Munich"
```

    Anton went from Aurich to Amberg-Sulzbach
    Bernd went from Berlin to Bergheim
    Erich is not allowed to go to Berlin
    August went from Augsburg to Amsterdam
    Emil is not allowed to go to Munich



```python
person3 >> 'Berlin'
```

    Erich is not allowed to go to Berlin



```python
s = """
print("")
print("Willkommen bei wordle_alpha!")
print("Mir war langweilig, frag nicht.")
print("")
print("Errate ein zufälliges Wort mit fünf (5) Buchstaben.")
print("Das Wort enthält jeden Buchstaben höchstens ein (1) mal,")
print("also kein Buchstabe ist doppelt im Wort.")
print("Du hast sechs (6) Versuche.")
print("Das Programm wird dir Feedback zu deinen Tipps geben.")
print("+ = Der Buchstabe befindet sich an der richtigen Stelle")
print("~ = Der Buchstabe befindet sich im Wort, aber an der falschen Stelle")
print("- = Der Buchstabe befindet sich nicht im Wort")
print("Viel Spaß :)")
print("")
print("(ﾉ◕ヮ◕)ﾉ*❤:♡ﾟ ✧ﾟ･:✧❤ヽ(◕ヮ◕ヽ)")
"""

```


```python
print(s.replace('print("', '').replace('")', ''))
```

    
    
    Willkommen bei wordle_alpha!
    Mir war langweilig, frag nicht.
    
    Errate ein zufälliges Wort mit fünf (5) Buchstaben.
    Das Wort enthält jeden Buchstaben höchstens ein (1) mal,
    also kein Buchstabe ist doppelt im Wort.
    Du hast sechs (6) Versuche.
    Das Programm wird dir Feedback zu deinen Tipps geben.
    + = Der Buchstabe befindet sich an der richtigen Stelle
    ~ = Der Buchstabe befindet sich im Wort, aber an der falschen Stelle
    - = Der Buchstabe befindet sich nicht im Wort
    Viel Spaß :)
    
    (ﾉ◕ヮ◕)ﾉ*❤:♡ﾟ ✧ﾟ･:✧❤ヽ(◕ヮ◕ヽ)
    



```python
s = """
print("")
            print("┐(ﾟ～ﾟ)┌")
            print("")
            print("Das Wort enthält jeden Buchstaben höchstens ein (1) mal,")
            print("also kein Buchstabe ist doppelt im Wort.")
            print("Du hast sechs (6) Versuche.")
            print("Das Programm wird dir Feedback zu deinen Tipps geben.")
            print("+ = Der Buchstabe befindet sich an der richtigen Stelle")
            print("~ = Der Buchstabe befindet sich im Wort, aber an der falschen Stelle")
            print("- = Der Buchstabe befindet sich nicht im Wort")
            print("")
"""
```


```python
x = s.replace('print("', '').replace('")', '')
```


```python
import textwrap
```


```python
print(textwrap.dedent(x))
```

    
    
    ┐(ﾟ～ﾟ)┌
    
    Das Wort enthält jeden Buchstaben höchstens ein (1) mal,
    also kein Buchstabe ist doppelt im Wort.
    Du hast sechs (6) Versuche.
    Das Programm wird dir Feedback zu deinen Tipps geben.
    + = Der Buchstabe befindet sich an der richtigen Stelle
    ~ = Der Buchstabe befindet sich im Wort, aber an der falschen Stelle
    - = Der Buchstabe befindet sich nicht im Wort
    
    



```python
w = 'tisch'
```


```python
len(w) == 5
```




    True




```python
len(set(w)) == len(w)
```




    True




```python
word = 'ampel'
target = 'apfel'
```


```python
res = []
for w, t in zip(word, target):
    if w == t:
        res.append('+')
    elif w in target:
        res.append('~')
    else:
        res.append('-')
```


```python
res
```




    ['+', '-', '~', '+', '+']




```python
a = ['|']
for w, z in zip(word, res):
    a.extend([z, w, z, '|'])
```


```python
print(''.join(a))
```

    |+a+|-m-|~p~|+e+|+l+|



```python
ls *.py
```

    erstes.py  wordle_alpha0.2.py  wordle_alpha0.3.py  übung4_1_1.py  übung4_1_2.py



```python
m = 'wordle_alpha0.3'
```


```python
m.isidentifier()
```




    False




```python
import wordle_alpha_0_3 as w
```


```python
w.wordCheck?
```


    [0;31mSignature:[0m [0mw[0m[0;34m.[0m[0mwordCheck[0m[0;34m([0m[0mwarray[0m[0;34m,[0m [0mtarray[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m <no docstring>
    [0;31mFile:[0m      ~/data/wordle_alpha_0_3.py
    [0;31mType:[0m      function




```python
w.welcome?
```


    [0;31mSignature:[0m
    [0mw[0m[0;34m.[0m[0mwelcome[0m[0;34m([0m[0;34m[0m
    [0;34m[0m    [0mtext[0m[0;34m=[0m[0;34m'\nWillkommen bei wordle_alpha!\nMir war langweilig, frag nicht.\n\nErrate ein zufälliges Wort mit fünf (5) Buchstaben.\nDas Wort enthält jeden Buchstaben höchstens ein (1) mal,\nalso kein Buchstabe ist doppelt im Wort.\nDu hast sechs (6) Versuche.\nDas Programm wird dir Feedback zu deinen Tipps geben.\n+ = Der Buchstabe befindet sich an der richtigen Stelle\n~ = Der Buchstabe befindet sich im Wort, aber an der falschen Stelle\n- = Der Buchstabe befindet sich nicht im Wort\nViel Spaß :)\n\n(ﾉ◕ヮ◕)ﾉ*❤:♡ﾟ ✧ﾟ･:✧❤ヽ(◕ヮ◕ヽ)\n'[0m[0;34m,[0m[0;34m[0m
    [0;34m[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m Show welcome message.
    [0;31mFile:[0m      ~/data/wordle_alpha_0_3.py
    [0;31mType:[0m      function




```python

```
