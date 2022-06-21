```python
s1 = {3, 3, 1, 2, 3, 4, 5, 4, 3, 2, 1}
```


```python
s1
```




    {1, 2, 3, 4, 5}




```python
{'d', 10, 3, 2, 1, 50, 'a'}
```




    {1, 10, 2, 3, 50, 'a', 'd'}




```python
s2 = set([4, 6, 7, 8, 5, 4, 5, 6])
```


```python
s2
```




    {4, 5, 6, 7, 8}




```python
s1.intersection(s2)
```




    {4, 5}




```python
s1 & s2
```




    {4, 5}




```python
s1 - s2
```




    {1, 2, 3}




```python
s2 - s1
```




    {6, 7, 8}




```python
1 in s1
```




    True




```python
L = [3, 4, 5, 6, 1, 2, 3, 4, 5, 4, 3]
```


```python
list(set(L))
```




    [1, 2, 3, 4, 5, 6]




```python
res = []
seen = set()
for x in L:
    if x not in seen:
        seen.add(x)
        res.append(x)
```


```python
res
```




    [3, 4, 5, 6, 1, 2]




```python
L
```




    [3, 4, 5, 6, 1, 2, 3, 4, 5, 4, 3]




```python
s1.union(s2)
```




    {1, 2, 3, 4, 5, 6, 7, 8}




```python
s1 | s2
```




    {1, 2, 3, 4, 5, 6, 7, 8}




```python
s3 = {1, 3}
```


```python
s3 <= s1
```




    True




```python
s1.issuperset(s3)
```




    True




```python
s1.add?
```


    [0;31mDocstring:[0m
    Add an element to a set.
    
    This has no effect if the element is already present.
    [0;31mType:[0m      builtin_function_or_method




```python
s1.remove?
```


    [0;31mDocstring:[0m
    Remove an element from a set; it must be a member.
    
    If the element is not a member, raise a KeyError.
    [0;31mType:[0m      builtin_function_or_method




```python
s1.discard?
```


    [0;31mDocstring:[0m
    Remove an element from a set if it is a member.
    
    If the element is not a member, do nothing.
    [0;31mType:[0m      builtin_function_or_method




```python
fz = frozenset(s1)
```


```python
fz
```




    frozenset({1, 2, 3, 4, 5})




```python
ms = set(dir(s1))
mf = set(dir(fz))
```


```python
ms - mf
```




    {'__iand__',
     '__ior__',
     '__isub__',
     '__ixor__',
     'add',
     'clear',
     'difference_update',
     'discard',
     'intersection_update',
     'pop',
     'remove',
     'symmetric_difference_update',
     'update'}




```python
mf - ms
```




    set()




```python
d1 = {'a': 100, 'b': 200}
d2 = {'b': 300, 'c': 400}
```


```python
d1.keys() & d2.keys()
```




    {'b'}




```python
d1.keys() - d2.keys()
```




    {'a'}




```python
dir(fz)
```




    ['__and__',
     '__class__',
     '__class_getitem__',
     '__contains__',
     '__delattr__',
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
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__ne__',
     '__new__',
     '__or__',
     '__rand__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__ror__',
     '__rsub__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__xor__',
     'copy',
     'difference',
     'intersection',
     'isdisjoint',
     'issubset',
     'issuperset',
     'symmetric_difference',
     'union']




```python
fz?
```


    [0;31mType:[0m        frozenset
    [0;31mString form:[0m frozenset({1, 2, 3, 4, 5})
    [0;31mLength:[0m      5
    [0;31mDocstring:[0m  
    frozenset() -> empty frozenset object
    frozenset(iterable) -> frozenset object
    
    Build an immutable unordered collection of unique elements.




```python
s1.add?
```


    [0;31mDocstring:[0m
    Add an element to a set.
    
    This has no effect if the element is already present.
    [0;31mType:[0m      builtin_function_or_method




```python
id(fz)
```




    140203830601856



# Übungen


```python
for exp in range(1, 7):
    n = 10**exp
    L = list(range(n))
    target = 'target'
    L[len(L) // 2] = target
    d = dict.fromkeys(L)
    s = set(L)
    tl = %timeit -o -q target in L
    td = %timeit -o -q target in d
    ts = %timeit -o -q target in s
    ratio = tl.average / td.average
    ratio2 = td.average / ts.average
    print(f'{n:8d}: {ratio:.2f} {ratio2:.2f}')
```

          10: 2.16 1.11
         100: 14.26 1.03
        1000: 129.79 1.07
       10000: 1226.77 1.22
      100000: 13313.19 1.11
     1000000: 134373.75 1.02



```python

```
