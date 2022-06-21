```python
input('Eingabe: ')
```

    Eingabe:  123





    '123'




```python
import sys
```


```python
sys.argv
```




    ['/opt/mambaforge/envs/python310/lib/python3.10/site-packages/ipykernel_launcher.py',
     '-f',
     '/home/pya_trainer_master/.local/share/jupyter/runtime/kernel-16ccb638-154e-44ce-b35a-1360abc23154.json']




```python
fobj = open('data.txt', 'w')
```


```python
fobj
```




    <_io.TextIOWrapper name='data.txt' mode='w' encoding='UTF-8'>




```python
fobj = open('data.txt', 'w', encoding='UTF-8')
```


```python
fobj.write('Zeile 1\nZeile 2\n\nZeile 4\n')
```




    25




```python
fobj.write("""Zeile 5
Zeile 6

Zeile 8
Zeile 9
""")
```




    33




```python
fobj.close()
```


```python
%less data.txt
```


    Zeile 1
    Zeile 2
    
    Zeile 4
    Zeile 5
    Zeile 6
    
    Zeile 8
    Zeile 9




```python
with open('data.txt') as fobj:
    print(fobj.closed)
    print(fobj.closed)
print(fobj.closed)
```

    False
    False
    True



```python
with open('data.txt') as fobj:
    data = fobj.read()
```


```python
data
```




    'Zeile 1\nZeile 2\n\nZeile 4\nZeile 5\nZeile 6\n\nZeile 8\nZeile 9\n'




```python
print(data)
```

    Zeile 1
    Zeile 2
    
    Zeile 4
    Zeile 5
    Zeile 6
    
    Zeile 8
    Zeile 9
    



```python
with open('data.txt') as fobj:
    data_lines = fobj.readlines()
```


```python
data_lines
```




    ['Zeile 1\n',
     'Zeile 2\n',
     '\n',
     'Zeile 4\n',
     'Zeile 5\n',
     'Zeile 6\n',
     '\n',
     'Zeile 8\n',
     'Zeile 9\n']




```python
with open('data.txt') as fobj:
    for line in fobj:
        print(line, end='')
```

    Zeile 1
    Zeile 2
    
    Zeile 4
    Zeile 5
    Zeile 6
    
    Zeile 8
    Zeile 9



```python
line
```




    'Zeile 9\n'




```python
line.split()
```




    ['Zeile', '9']




```python
line.split()[-1]
```




    '9'




```python
int(line.split()[-1])
```




    9




```python
sum_ = 0
with open('data.txt') as fobj:
    for line in fobj:
        sum_ += int(line.split()[-1])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    /tmp/ipykernel_250760/378792113.py in <module>
          2 with open('data.txt') as fobj:
          3     for line in fobj:
    ----> 4         sum_ += int(line.split()[-1])
    

    IndexError: list index out of range



```python
line
```




    '\n'




```python
int(line.split()[-1])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    /tmp/ipykernel_250760/4069142819.py in <module>
    ----> 1 int(line.split()[-1])
    

    IndexError: list index out of range



```python
line.split()[-1]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    /tmp/ipykernel_250760/1786856253.py in <module>
    ----> 1 line.split()[-1]
    

    IndexError: list index out of range



```python
line.split()
```




    []




```python
line.strip()
```




    ''




```python
sum_ = 0
with open('data.txt') as fobj:
    for line in fobj:
        if line.strip():
            sum_ += int(line.split()[-1])
```


```python
sum_
```




    35




```python
with open('data.txt') as fobj:
    sum_ = sum(int(line.split()[-1]) for line in fobj if line.strip())
```


```python
sum_
```




    35




```python
import pandas as pd
```


```python
pd.read_csv?
```


```python
import pickle
```


```python
L = list(range(2, 11))
```


```python
L
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
pickle.dumps(L)
```




    b'\x80\x04\x95\x17\x00\x00\x00\x00\x00\x00\x00]\x94(K\x02K\x03K\x04K\x05K\x06K\x07K\x08K\tK\ne.'




```python
p = pickle.dumps(L)
```


```python
pickle.loads(p)
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
with open('liste.pcl', 'wb') as fobj:
    pickle.dump(L, fobj)
```


```python
with open('liste.pcl', 'rb') as fobj:
    L2 = pickle.load(fobj)
```


```python
L2
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
pickle.dumps?
```


    [0;31mSignature:[0m [0mpickle[0m[0;34m.[0m[0mdumps[0m[0;34m([0m[0mobj[0m[0;34m,[0m [0mprotocol[0m[0;34m=[0m[0;32mNone[0m[0;34m,[0m [0;34m*[0m[0;34m,[0m [0mfix_imports[0m[0;34m=[0m[0;32mTrue[0m[0;34m,[0m [0mbuffer_callback[0m[0;34m=[0m[0;32mNone[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Return the pickled representation of the object as a bytes object.
    
    The optional *protocol* argument tells the pickler to use the given
    protocol; supported protocols are 0, 1, 2, 3, 4 and 5.  The default
    protocol is 4. It was introduced in Python 3.4, and is incompatible
    with previous versions.
    
    Specifying a negative protocol version selects the highest protocol
    version supported.  The higher the protocol used, the more recent the
    version of Python needed to read the pickle produced.
    
    If *fix_imports* is True and *protocol* is less than 3, pickle will
    try to map the new Python 3 names to the old module names used in
    Python 2, so that the pickle data stream is readable with Python 2.
    
    If *buffer_callback* is None (the default), buffer views are serialized
    into *file* as part of the pickle stream.  It is an error if
    *buffer_callback* is not None and *protocol* is None or smaller than 5.
    [0;31mType:[0m      builtin_function_or_method




```python
import shelve
```


```python
db = shelve.open('db2')
```


```python
db
```




    <shelve.DbfilenameShelf at 0x7f0114f14910>




```python
dict(db)
```




    {}




```python
db['a'] = L
```


```python
dict(db)
```




    {'a': [2, 3, 4, 5, 6, 7, 8, 9, 10]}




```python
db['a']
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
db
```




    <shelve.DbfilenameShelf at 0x7f0114f14910>




```python

```
