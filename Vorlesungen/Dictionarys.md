```python
d = {'a': 100, 'b': 200, 'c': 300}
```


```python
d
```




    {'a': 100, 'b': 200, 'c': 300}




```python
d['c']
```




    300




```python
d[(1, 2, 3)] = 500
```


```python
d
```




    {'a': 100, 'b': 200, 'c': 300, (1, 2, 3): 500}




```python
d[[1, 2, 3]] = 500
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_93472/189324564.py in <module>
    ----> 1 d[[1, 2, 3]] = 500
    

    TypeError: unhashable type: 'list'



```python
del d['a']
```


```python
d
```




    {'b': 200, 'c': 300, (1, 2, 3): 500}




```python
d['b'] = 20000
```


```python
d
```




    {'b': 20000, 'c': 300, (1, 2, 3): 500}




```python
d['a'] = 100
```


```python
d
```




    {'b': 20000, 'c': 300, (1, 2, 3): 500, 'a': 100}




```python
'a' in d
```




    True




```python
300 in d
```




    False




```python
d
```




    {'b': 20000, 'c': 300, (1, 2, 3): 500, 'a': 100}




```python
d.keys()
```




    dict_keys(['b', 'c', (1, 2, 3), 'a'])




```python
d.values()
```




    dict_values([20000, 300, 500, 100])




```python
d.items()
```




    dict_items([('b', 20000), ('c', 300), ((1, 2, 3), 500), ('a', 100)])




```python
k = d.keys()
```


```python
k
```




    dict_keys(['b', 'c', (1, 2, 3), 'a'])




```python
d['e'] = 208
```


```python
d
```




    {'b': 20000, 'c': 300, (1, 2, 3): 500, 'a': 100, 'e': 208}




```python
k
```




    dict_keys(['b', 'c', (1, 2, 3), 'a', 'e'])




```python
L = list(k)
```


```python
L
```




    ['b', 'c', (1, 2, 3), 'a', 'e']




```python
neu = {'a': 3000, 'x': 4000}
```


```python
d2 = d.copy()
```


```python
d2
```




    {'b': 20000, 'c': 300, (1, 2, 3): 500, 'a': 100, 'e': 208}




```python
d.update(neu)
```


```python
d
```




    {'b': 20000, 'c': 300, (1, 2, 3): 500, 'a': 3000, 'e': 208, 'x': 4000}




```python
d2
```




    {'b': 20000, 'c': 300, (1, 2, 3): 500, 'a': 100, 'e': 208}




```python
for k, v in neu.items():
    d2[k] = v
```


```python
d2
```




    {'b': 20000, 'c': 300, (1, 2, 3): 500, 'a': 3000, 'e': 208, 'x': 4000}




```python
d.clear?
```


    [0;31mDocstring:[0m D.clear() -> None.  Remove all items from D.
    [0;31mType:[0m      builtin_function_or_method




```python
dict()
```




    {}




```python
dict.fromkeys('abc')
```




    {'a': None, 'b': None, 'c': None}




```python
dict.fromkeys('abc', 42)
```




    {'a': 42, 'b': 42, 'c': 42}




```python
v = 42
res = {}
for k in 'abc':
    res[k] = v
```


```python
res
```




    {'a': 42, 'b': 42, 'c': 42}




```python
d3 = dict.fromkeys('abc', [])
```


```python
d3
```




    {'a': [], 'b': [], 'c': []}




```python
d3['a'].append(10)
```


```python
d3
```




    {'a': [10], 'b': [10], 'c': [10]}




```python
v = []
d4 = {}
for k in 'abc':
    d4[k] = v
```


```python
d4
```




    {'a': [], 'b': [], 'c': []}




```python
d4['a'].append(10)
```


```python
d4
```




    {'a': [10], 'b': [10], 'c': [10]}




```python
d5 = {}
for k in 'abc':
    d5[k] = []
```


```python
d5
```




    {'a': [], 'b': [], 'c': []}




```python
d5['a'].append(10)
```


```python
d5
```




    {'a': [10], 'b': [], 'c': []}




```python
d['a']
```




    3000




```python
d.get('a')
```




    3000




```python
d['ä']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    /tmp/ipykernel_93472/2074335098.py in <module>
    ----> 1 d['ä']
    

    KeyError: 'ä'



```python
d.get('ä')
```


```python
d.get('ä', 999)
```




    999




```python
d.get?
```


    [0;31mSignature:[0m [0md[0m[0;34m.[0m[0mget[0m[0;34m([0m[0mkey[0m[0;34m,[0m [0mdefault[0m[0;34m=[0m[0;32mNone[0m[0;34m,[0m [0;34m/[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m Return the value for key if key is in the dictionary, else default.
    [0;31mType:[0m      builtin_function_or_method




```python
d
```




    {'b': 20000, 'c': 300, (1, 2, 3): 500, 'a': 3000, 'e': 208, 'x': 4000}




```python
d.setdefault('a')
```




    3000




```python
d.setdefault('ä', 999)
```




    999




```python
d
```




    {'b': 20000,
     'c': 300,
     (1, 2, 3): 500,
     'a': 3000,
     'e': 208,
     'x': 4000,
     'ä': 999}




```python
key = 'ü'
default = 56
if key in d:
    res = d[key]
else:
    res = default
```


```python
res
```




    56




```python
d
```




    {'b': 20000,
     'c': 300,
     (1, 2, 3): 500,
     'a': 3000,
     'e': 208,
     'x': 4000,
     'ä': 999}




```python
key = 'ü'
default = 56
if key in d:
    res = d[key]
else:
    res = default
    d[key] = default
```


```python
d
```




    {'b': 20000,
     'c': 300,
     (1, 2, 3): 500,
     'a': 3000,
     'e': 208,
     'x': 4000,
     'ä': 999,
     'ü': 56}




```python
d.pop('ü')
```




    56




```python
d
```




    {'b': 20000,
     'c': 300,
     (1, 2, 3): 500,
     'a': 3000,
     'e': 208,
     'x': 4000,
     'ä': 999}




```python
d.popitem()
```




    ('ä', 999)




```python
d.popitem?
```


    [0;31mSignature:[0m [0md[0m[0;34m.[0m[0mpopitem[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Remove and return a (key, value) pair as a 2-tuple.
    
    Pairs are returned in LIFO (last-in, first-out) order.
    Raises KeyError if the dict is empty.
    [0;31mType:[0m      builtin_function_or_method




```python
dict()
```




    {}




```python
dict([('a', 100), ('b', 200), ('c', 300)])
```




    {'a': 100, 'b': 200, 'c': 300}




```python
keys = 'abc'
values = [100, 200, 300]
```


```python
dict(zip(keys, values))
```




    {'a': 100, 'b': 200, 'c': 300}




```python
{x: 42 for x in 'abc'}
```




    {'a': 42, 'b': 42, 'c': 42}




```python
{x.upper(): 42 for x in 'abc'}
```




    {'A': 42, 'B': 42, 'C': 42}




```python
{k: v for k, v in zip(keys, values)}
```




    {'a': 100, 'b': 200, 'c': 300}




```python
%timeit 1 + 1
```

    13.9 ns ± 0.51 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)



```python
import timeit
```


```python
start = timeit.default_timer()
```


```python
timeit.default_timer() - start
```




    0.1858399889897555




```python
n = 100000000
```


```python
start = timeit.default_timer()
for _ in range(n):
    1 + 1
(timeit.default_timer() - start) / n
```




    4.921665701782331e-08



# Übungen


```python
name = "Erika Mustermann"
dic = {
    "Max Mustermann": "+49 157 55 55 555",
    "Karl Lauterbach": "+49 176 11 11 111",
    "Olaf Scholz": "+ 49 177 33 33 333",
    name: "+49 178 22 22 222"
}

if name in dic:
    print(name, "is part of dictionary")

print(list(dic.values()))

print(list(dic.keys()))
```

    Erika Mustermann is part of dictionary
    ['+49 157 55 55 555', '+49 176 11 11 111', '+ 49 177 33 33 333', '+49 178 22 22 222']
    ['Max Mustermann', 'Karl Lauterbach', 'Olaf Scholz', 'Erika Mustermann']



```python
name = "Klabautermann"
print(dic.get(name))
print(dic.get(name, 0))

print(dic.setdefault(name, 0))
print(dic)
```

    None
    0
    0
    {'Max Mustermann': '+49 157 55 55 555', 'Karl Lauterbach': '+49 176 11 11 111', 'Olaf Scholz': '+ 49 177 33 33 333', 'Erika Mustermann': '+49 178 22 22 222', 'Klabautermann': 0}



```python
new_entries = {
    "Christian Lindner": "+49 155 99 99 999",
    "Robert Habek": "+49 176 12 34 567",
    "Karl Lauterbach": "+49 176 11 11 117",
}

new_dic = dic.copy()
another_dic = dic.copy()

for name, number in new_entries.items():
    new_dic[name] = number

print('Schleife')
print(new_dic)

print()
print('Update')
another_dic.update(new_entries)

print(another_dic)
```

    Schleife
    {'Max Mustermann': '+49 157 55 55 555', 'Karl Lauterbach': '+49 176 11 11 117', 'Olaf Scholz': '+ 49 177 33 33 333', 'Erika Mustermann': '+49 178 22 22 222', 'Klabautermann': 0, 'Christian Lindner': '+49 155 99 99 999', 'Robert Habek': '+49 176 12 34 567'}
    
    Update
    {'Max Mustermann': '+49 157 55 55 555', 'Karl Lauterbach': '+49 176 11 11 117', 'Olaf Scholz': '+ 49 177 33 33 333', 'Erika Mustermann': '+49 178 22 22 222', 'Klabautermann': 0, 'Christian Lindner': '+49 155 99 99 999', 'Robert Habek': '+49 176 12 34 567'}



```python
print(dic.pop(name))
print(dic.popitem())
```

    +49 176 11 11 111
    ('Klabautermann', 0)



```python
name
```




    'Karl Lauterbach'




```python
%pprint
```

    Pretty printing has been turned OFF



```python
for exp in range(1, 7):
    n = 10**exp
    L = list(range(n))
    target = 'target'
    L[len(L) // 2] = target
    d = dict.fromkeys(L)
    tl = %timeit -o -q target in L
    td = %timeit -o -q target in d
    ratio = tl.average / td.average
    print(f'{n:8d}: {ratio:.2f}')
```

          10: 2.33
         100: 16.78
        1000: 128.00
       10000: 1522.96
      100000: 15796.30
     1000000: 153288.98



```python
tl.average / td.average
```




    2.4595047774566026




```python
1 / 2
```




    0.5




```python
1 // 2
```




    0




```python
n = 10
L = list(range(n))
target = 'target'
L[len(L) // 2] = target
L
```




    [0, 1, 2, 3, 4, 'target', 6, 7, 8, 9]




```python
d = dict.fromkeys(L)
d
```




    {0: None, 1: None, 2: None, 3: None, 4: None, 'target': None, 6: None, 7: None, 8: None, 9: None}




```python

```
