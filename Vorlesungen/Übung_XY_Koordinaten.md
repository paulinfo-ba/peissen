# Übung - Einlesen und Arbeit mit X-Y- Koordinaten

1. Schreiben Sie eine Funktion, die die Werte aus der Datei `coords.txt` in zwei
   Listen mit Zahlen einliest. 
   Das ist der Inhalt von `coords.txt`:


```python
%less coords.txt
```


    X, Y
    0.07330604878866975, 0.8014226821067756
    0.1661575819631842, 1.800580523229894
    0.6995403090391857, 2.9428426511704133
    3.739693717843958, 3.273789345607889
    4.6548452940121825, 3.2432474181215083
    5.800609928703754, 2.2899099772482145
    2.8739261867333927, 6.851536185480562
    7.213831740018356, 6.9884182899511025
    5.326744862838446, 2.47894007512006
    6.4738431697340655, 8.064819056138258
    9.391058372638053, 4.65542320269743
    1.6948694982714723, 3.5560225045761187
    1.5140093076206513, 3.1884934811256436
    4.430058552698293, 2.25747312715163
    10.852231279914546, 3.781204549788254
    0.8270875691175572, 2.845477430116926
    2.751993939849164, 15.630578767457608
    0.950355329431521, 15.883654177194524
    3.2673577026468132, 17.848028970597163
    15.357127440374532, 12.3861418864545




```python
%ls
```

    coords.txt  Übung_XY_Koordinaten.ipynb



```python
with open('coords.txt') as fobj:
    lines = fobj.readlines()
```


```python
file = open('coords.txt','r')
X = []
Y = []
file.readline()
for row in file:
    sp = row.split(",")
    X.append(sp[0])
    Y.append(sp[1])
```


```python
Y
```




    [' 0.8014226821067756\n',
     ' 1.800580523229894\n',
     ' 2.9428426511704133\n',
     ' 3.273789345607889\n',
     ' 3.2432474181215083\n',
     ' 2.2899099772482145\n',
     ' 6.851536185480562\n',
     ' 6.9884182899511025\n',
     ' 2.47894007512006\n',
     ' 8.064819056138258\n',
     ' 4.65542320269743\n',
     ' 3.5560225045761187\n',
     ' 3.1884934811256436\n',
     ' 2.25747312715163\n',
     ' 3.781204549788254\n',
     ' 2.845477430116926\n',
     ' 15.630578767457608\n',
     ' 15.883654177194524\n',
     ' 17.848028970597163\n',
     ' 12.3861418864545\n']




```python
import csv
xs = []
ys = []
with open('coords.txt', newline="\n") as coordsfile:
    next(coordsfile)
    coords = csv.reader(coordsfile)
    for row in coords:
        xs.append(row[0])
        ys.append(row[1])
    
print(xs)
print(ys)
```

    ['0.07330604878866975', '0.1661575819631842', '0.6995403090391857', '3.739693717843958', '4.6548452940121825', '5.800609928703754', '2.8739261867333927', '7.213831740018356', '5.326744862838446', '6.4738431697340655', '9.391058372638053', '1.6948694982714723', '1.5140093076206513', '4.430058552698293', '10.852231279914546', '0.8270875691175572', '2.751993939849164', '0.950355329431521', '3.2673577026468132', '15.357127440374532']
    [' 0.8014226821067756', ' 1.800580523229894', ' 2.9428426511704133', ' 3.273789345607889', ' 3.2432474181215083', ' 2.2899099772482145', ' 6.851536185480562', ' 6.9884182899511025', ' 2.47894007512006', ' 8.064819056138258', ' 4.65542320269743', ' 3.5560225045761187', ' 3.1884934811256436', ' 2.25747312715163', ' 3.781204549788254', ' 2.845477430116926', ' 15.630578767457608', ' 15.883654177194524', ' 17.848028970597163', ' 12.3861418864545']



```python
fname = 'coords.txt'
xs = []
ys = []
with open(fname) as fobj:
    next(fobj)
    for line in fobj:
        x, y = line.split(',')
        xs.append(float(x))
        ys.append(float(y))
```


```python
def read_coords(file_name):
    """Read csv file with X and Y coordinates.
    
    Returns list of floats for X and Y."""
    xs = []
    ys = []
    with open(file_name) as fobj:
        next(fobj)
        for line in fobj:
            x, y, *_ = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    return xs, ys
        
xs, ys = read_coords('coords.txt')
```


```python
read_coords?
```


    [0;31mSignature:[0m [0mread_coords[0m[0;34m([0m[0mfile_name[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Read csv file with X and Y coordinates.
    
    Returns list of floats for X and Y.
    [0;31mFile:[0m      /tmp/ipykernel_325954/4110430604.py
    [0;31mType:[0m      function




```python
xs[:5]
```




    [0.07330604878866975,
     0.1661575819631842,
     0.6995403090391857,
     3.739693717843958,
     4.6548452940121825]




```python
ys[:5]
```




    [0.8014226821067756,
     1.800580523229894,
     2.9428426511704133,
     3.273789345607889,
     3.2432474181215083]



Der Beginn der Liste mit den X-Werten soll so aussehen:


```python
xs[:5]
```




    [0.07330604878866975,
     0.1661575819631842,
     0.6995403090391857,
     3.739693717843958,
     4.6548452940121825]



Der Beginn der Liste mit den y-Werten soll so aussehen:


```python
ys[:5]
```




    [0.8014226821067756,
     1.800580523229894,
     2.9428426511704133,
     3.273789345607889,
     3.2432474181215083]



2. Schreiben Sie eine Funktion, die die Werte aus der Datei `coords.txt` in ein
   Dictionary mit den Buchstaben in der ersten Zeile als Schlüssel und allen
   Zahlen in je eine List als Werte einliest.
   

Das Ergebnis soll so aussehen:

Returns dict of list of floats with `X` and `Y` as keys.


```python
def read_as_dict(file_name):
    """Read csv file with X and Y coordinates.
    
    Returns dict of lists with floats.
    Keys are the names in first line.
    
    Example:
    
    file header: X, Y
    result: {'X': [1.5, 2.5, 3.5], 'Y': [4.5, 5.5, 6.5]}    
    """
    data = {}
    with open(file_name) as fobj:
        keys = [x.strip() for x in next(fobj).split(',')]
        for key in keys:
            data[key] = []
        for line in fobj:
            for key, value in zip(keys, line.split(',')):
                data[key].append(float(value))
    return data

data = read_as_dict('coords.txt')
```


```python
keys
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    /tmp/ipykernel_325954/3396956383.py in <module>
    ----> 1 keys
    

    NameError: name 'keys' is not defined



```python
data
```




    {'X': [0.07330604878866975,
      0.1661575819631842,
      0.6995403090391857,
      3.739693717843958,
      4.6548452940121825,
      5.800609928703754,
      2.8739261867333927,
      7.213831740018356,
      5.326744862838446,
      6.4738431697340655,
      9.391058372638053,
      1.6948694982714723,
      1.5140093076206513,
      4.430058552698293,
      10.852231279914546,
      0.8270875691175572,
      2.751993939849164,
      0.950355329431521,
      3.2673577026468132,
      15.357127440374532],
     'Y': [0.8014226821067756,
      1.800580523229894,
      2.9428426511704133,
      3.273789345607889,
      3.2432474181215083,
      2.2899099772482145,
      6.851536185480562,
      6.9884182899511025,
      2.47894007512006,
      8.064819056138258,
      4.65542320269743,
      3.5560225045761187,
      3.1884934811256436,
      2.25747312715163,
      3.781204549788254,
      2.845477430116926,
      15.630578767457608,
      15.883654177194524,
      17.848028970597163,
      12.3861418864545]}



3. Schreiben Sie eine Funktion, die die beiden Summen der Werte der Spalten
   X und Y ermittelt:
   
   
(a) für die Daten in den beiden Listen aus Aufgabe 1 (sum_lists)


(b) für die Daten im Dictionary aus Aufgabe 2 (sum_dict)  

 Dieser Ausdruck soll wahr sein:   


```python
sum_lists(xs, ys) == sum_dict(data) == (88.05864783223778, 120.76800430133447)
```


```python
def sum_list(xs, ys):
    return sum(xs), sum(ys)
```


```python
sum_list(xs, ys)
```




    (88.05864783223778, 120.76800430133447)




```python
def sum_dict(data):
    return sum(data['X']), sum(data['Y'])
```


```python
sum_dict(data)
```




    (88.05864783223778, 120.76800430133447)




```python
def sum_dict2(data):
    res = {}
    for key, value in data.items():
        res[key] = sum(value)
    return res
```


```python
sum_dict2(data)
```




    {'X': 88.05864783223778, 'Y': 120.76800430133447}




```python
def sum_dict3(data):
    return {key: sum(value) for key, value in data.items()}
```


```python
sum_dict3(data)
```




    {'X': 88.05864783223778, 'Y': 120.76800430133447}



4. Speichern Sie alle Funktionen in einem Modul und importieren Sie einzelne
   Funktionen in ein Notebook und rufen Sie diese auf.
   
   
Alle Funktionen sollen "schöne" und "vollständige" Funktionen sein.

5. Schreiben Sie eine Klasse `Coord`, die Werte für `x` und `y` zum 
   Initialisierungszeitpunkt übernimmt und als Instanzattribute setzt.
   Berechnen Sie den Abstand zum Nullpunkt (Quadratwurzel aus den Quadraten der beiden         
   Koordinatenwerte) und setzen Sie diesen berechneten Wert als Attribut `dist`.
   Erstellen Sie eine Instanz dieser Klasse mit den Werten `2` und `3` für `x`und `y`.
   Der Wert für `dist` sollte ca. `3.6` betragen


```python
from math import sqrt


class Coord:
    """Class for usage with x and y coordinates to calculate distances to 0,0 """
    x = 0
    y = 0
    dist = 0

    def __init__(self, xin=0, yin=0):
        """Constructor which calculates the distance as well"""
        self.x = xin
        self.y = yin
        self.dist = sqrt(xin**2 + yin**2)
```


```python
c = Coord()
```


```python
c
```




    <__main__.Coord at 0x7f3cc2679820>




```python
c.dist
```




    0.0




```python
coord = Coord(2, 3)
```


```python
coord.x
```




    2




```python
coord.dist
```




    3.605551275463989




```python
coord
```




    <__main__.Coord at 0x7f3cc271b4c0>




```python
import math
```


```python
math.hypot?
```


    [0;31mDocstring:[0m
    hypot(*coordinates) -> value
    
    Multidimensional Euclidean distance from the origin to a point.
    
    Roughly equivalent to:
        sqrt(sum(x**2 for x in coordinates))
    
    For a two dimensional point (x, y), gives the hypotenuse
    using the Pythagorean theorem:  sqrt(x*x + y*y).
    
    For example, the hypotenuse of a 3/4/5 right triangle is:
    
        >>> hypot(3.0, 4.0)
        5.0
    [0;31mType:[0m      builtin_function_or_method



6. Fügen Sie Ihrer Klasse eine Funktion `__repr__` hinzu, die die
   Repräsentation einer Instanz mit den Werten `x=2`, und `y=3` 
   so aussehen lassen: `Coord(2, 3)`


```python
from math import hypot


class Coord:
    """Class for usage with x and y coordinates to calculate distances to 0,0 """


    def __init__(self, x, y):
        """Constructor which calculates the distance as well"""
        self.x = x
        self.y = y
        self.dist = hypot(x, x)
        
    def __repr__(self):
        return f'Coord({self.x!r}, {self.y!r})'
```


```python
Coord(2, 3)
```




    Coord(2, 3)




```python
class CoordChild(Coord):
    pass
```


```python
CoordChild(2, 3)
```




    Coord(2, 3)




```python
class Coord:
    """Class for usage with x and y coordinates to calculate distances to 0,0 """


    def __init__(self, x, y):
        """Constructor which calculates the distance as well"""
        self.x = x
        self.y = y
        self.dist = hypot(x, x)
        
    def __repr__(self):
        return f'{self.__class__.__name__}({self.x!r}, {self.y!r})'
```


```python
class CoordChild(Coord):
    pass
```


```python
CoordChild(2, 3)
```




    CoordChild(2, 3)



7. Erzeugen Sie ein Liste von Instanzen von `Coord`.
   Nutzen Sie dazu die aus der Datei eingelesenen Werte Koordinaten. 

8. Fügen Sie Ihrer Klasse ein Methode `__add__` hinzu, 
   so dass dieses Ergebnis entsteht:


```python
coord1 = Coord(2, 3)
coord2 = Coord(7, 2)
coord1 + coord2from math import sqrt


class Coord:
    """Class for usage with x and y coordinates to calculate distances to 0,0 """
    x = 0
    y = 0
    dist = 0

    def __init__(self, xin, yin):
        """Constructor which calculates the distance as well"""
        self.x = xin
        self.y = yin
        self.dist = sqrt(xin**2 + yin**2)

    def __repr__(self):
        """String representation showing x and y"""
        return f"Coord({self.x}, {self.y})"

    def __add__(self, target):
        """Addition by adding values of x and y of both objects if both are
        Coord else add target to self"""
        if type(target) == type(self):
            return Coord(self.x + target.x, self.y + target.y)
        else:
            return Coord(self.x + target, self.y + target)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_329700/4006411628.py in <module>
          1 coord1 = Coord(2, 3)
          2 coord2 = Coord(7, 2)
    ----> 3 coord1 + coord2
    

    TypeError: unsupported operand type(s) for +: 'Coord' and 'Coord'



```python
from math import sqrt


class Coord:
    """Class for usage with x and y coordinates to calculate distances to 0,0 """

    def __init__(self, xin, yin):
        """Constructor which calculates the distance as well"""
        self.x = xin
        self.y = yin
        self.dist = sqrt(xin**2 + yin**2)

    def __repr__(self):
        """String representation showing x and y"""
        return f"Coord({self.x}, {self.y})"

    def __add__(self, target):
        """Addition by adding values of x and y of both objects if both are
        Coord else add target to self"""
        if type(target) == type(self):
            return Coord(self.x + target.x, self.y + target.y)
        else:
            return Coord(self.x + target, self.y + target)
```


```python
c1 = Coord(1, 2)
c2 = Coord(4, 5)
```


```python
c1 + c2
```




    Coord(5, 7)




```python
c1 + 100
```




    Coord(101, 102)




```python
class CoordChild(Coord):
    pass
```


```python
cc1 = CoordChild(3, 4)
```


```python
c1 + cc1
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_329700/596158639.py in <module>
    ----> 1 c1 + cc1
    

    /tmp/ipykernel_329700/2429863352.py in __add__(self, target)
         21             return Coord(self.x + target.x, self.y + target.y)
         22         else:
    ---> 23             return Coord(self.x + target, self.y + target)
    

    TypeError: unsupported operand type(s) for +: 'int' and 'CoordChild'



```python

class Coord:
    """Class for usage with x and y coordinates to calculate distances to 0,0 """

    def __init__(self, xin, yin):
        """Constructor which calculates the distance as well"""
        self.x = xin
        self.y = yin
        self.dist = sqrt(xin**2 + yin**2)

    def __repr__(self):
        """String representation showing x and y"""
        return f"Coord({self.x}, {self.y})"

    def __add__(self, target):
        """Addition by adding values of x and y of both objects if both are
        Coord else add target to self"""
        if isinstance(target, self.__class__) or isinstance(self, target.__class__):
            return Coord(self.x + target.x, self.y + target.y)
        else:
            return Coord(self.x + target, self.y + target)
```


```python
class CoordChild(Coord):
    pass
```


```python
c1 = Coord(10, 20)
cc1 = CoordChild(3, 4)
```


```python
c1 + cc1
```




    Coord(13, 24)




```python
cc1 + c1
```




    Coord(13, 24)




```python

```


```python

class Coord:
    """Class for usage with x and y coordinates to calculate distances to 0,0 """

    def __init__(self, xin, yin):
        """Constructor which calculates the distance as well"""
        self.x = xin
        self.y = yin
        self.dist = sqrt(xin**2 + yin**2)

    def __repr__(self):
        """String representation showing x and y"""
        return f"Coord({self.x}, {self.y})"

    def __add__(self, target):
        """Addition by adding values of x and y of both objects if both are
        Coord else add target to self"""
        return Coord(self.x + target.x, self.y + target.y)
```


```python
sum
```




    <function sum(iterable, /, start=0)>




```python

```
