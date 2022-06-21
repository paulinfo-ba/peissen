```python
%ls
```

    Anweisungen.ipynb     Iteratoren.ipynb    [0m[01;34madmin[0m/        [01;34mlistmath[0m/
    Ausnahmen.ipynb       Klassen.ipynb       data.txt      [01;34mmaterials[0m/
    Bibliothek.ipynb      Listen.ipynb        db            pylintrc
    Datenypen.ipynb       Mengen.ipynb        db2.dat       [01;36mshared[0m@
    Dictionarys.ipynb     Organisation.ipynb  db2.dir       source.zip
    Einführung.ipynb      Schleifen.ipynb     erstes.py     wordle_alpha0.2.py
    Entscheidungen.ipynb  Sequenzen.ipynb     [01;34mgeneratoren[0m/  wordle_alpha_0_3.py
    Funktionen.ipynb      Syntax.ipynb        [01;34mio[0m/           übung4_1_1.py
    IO.ipynb              [01;34m__pycache__[0m/        liste.pcl     übung4_1_2.py



```python
L1 = list(range(10, 20))
L2 = list(range(110, 120))
```


```python
L1
```




    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]




```python
L2
```




    [110, 111, 112, 113, 114, 115, 116, 117, 118, 119]




```python
%pprint
```

    Pretty printing has been turned OFF



```python
L1 + L2
```




    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]




```python
[x + y for x, y in zip(L1, L2)]
```




    [120, 122, 124, 126, 128, 130, 132, 134, 136, 138]




```python
L1
```




    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]




```python
L2
```




    [110, 111, 112, 113, 114, 115, 116, 117, 118, 119]




```python
!tree listmath/
```

    [01;34mlistmath/[00m
    ├── __init__.py
    ├── [01;34mcmath[00m
    │   ├── __init__.py
    │   ├── arithmetics.py
    │   └── trigonometrics.py
    └── [01;34mmath[00m
        ├── __init__.py
        ├── arithmetics.py
        └── trigonometrics.py
    
    2 directories, 7 files


* Verzeichnis mit `__init__.py` --> Paket
* Datei `*.py` --> Modul


```python
import listmath.math.arithmetics
```


```python
listmath.math.arithmetics.add(L1, L2)
```




    [120, 122, 124, 126, 128, 130, 132, 134, 136, 138]




```python
import listmath.math.arithmetics as arit
```


```python
arit.add(L1, L2)
```




    [120, 122, 124, 126, 128, 130, 132, 134, 136, 138]




```python
from listmath.math.arithmetics import add
```


```python
add is arit.add
```




    True




```python
listmath.math.arithmetics
```




    <module 'listmath.math.arithmetics' from '/home/pya_trainer_master/data/listmath/math/arithmetics.py'>




```python
import listmath.math
```


```python
listmath.math
```




    <module 'listmath.math' from '/home/pya_trainer_master/data/listmath/math/__init__.py'>




```python
import pandas as pd
```


```python
pd
```




    <module 'pandas' from '/opt/mambaforge/envs/python310/lib/python3.10/site-packages/pandas/__init__.py'>




```python
!tree -I __pycache__ /opt/mambaforge/envs/python310/lib/python3.10/site-packages/pandas
```


```python
pd
```




    <module 'pandas' from '/opt/mambaforge/envs/python310/lib/python3.10/site-packages/pandas/__init__.py'>




```python
%less /opt/mambaforge/envs/python310/lib/python3.10/site-packages/pandas/__init__.py
```


```python
pd.read_csv
```




    <function read_csv at 0x7f2988e0b130>




```python
pd.read_csv.__module__
```




    'pandas.io.parsers.readers'




```python
len(dir(pd))
```




    142



S o nicht:

```python
from listmath.math.arithmetics import *
from listmath.cmath.arithmetics import *
```


```python
import listmath.math.arithmetics as arit
import listmath.cmath.arithmetics as carit
```


```python
arit.add
```




    <function add at 0x7f29f7edb400>




```python
carit.a
```
