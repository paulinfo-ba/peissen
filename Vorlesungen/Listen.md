```python
L = list(range(2, 11))
```


```python
L
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
L[3]
```




    5




```python
L[3] = 100
```


```python
L
```




    [2, 3, 4, 100, 6, 7, 8, 9, 10]




```python
L[5:7]
```




    [7, 8]




```python
L[5:7] = [100, 200, 300, 400, 500]
```


```python
L
```




    [2, 3, 4, 100, 6, 100, 200, 300, 400, 500, 9, 10]




```python
L[4:4]
```




    []




```python
L[4:4] = [123]
```


```python
L
```




    [2, 3, 4, 100, 123, 6, 100, 200, 300, 400, 500, 9, 10]




```python
L.insert(4, 567)
```


```python
L
```




    [2, 3, 4, 100, 567, 123, 6, 100, 200, 300, 400, 500, 9, 10]




```python
L.insert?
```


    [0;31mSignature:[0m [0mL[0m[0;34m.[0m[0minsert[0m[0;34m([0m[0mindex[0m[0;34m,[0m [0mobject[0m[0;34m,[0m [0;34m/[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m Insert object before index.
    [0;31mType:[0m      builtin_function_or_method




```python
len
```




    <function len(obj, /)>




```python
L[::2]
```




    [2, 4, 567, 6, 200, 400, 9]




```python
len(L[::2])
```




    7




```python
[34] * 7
```




    [34, 34, 34, 34, 34, 34, 34]




```python
L[::2] = len(L[::2]) * [34]
```


```python
L
```




    [34, 3, 34, 100, 34, 123, 34, 100, 34, 300, 34, 500, 34, 10]




```python
del L[4]
```


```python
L
```




    [34, 3, 34, 100, 123, 34, 100, 34, 300, 34, 500, 34, 10]




```python
del L[5:7]
```


```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10]




```python
L.append(15)
```


```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15]




```python
L.append([1, 2, 3])
```


```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3]]




```python
L[-1]
```




    [1, 2, 3]




```python
L[-1][1]
```




    2




```python
L.append(L)
```


```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], [...]]




```python
L[-1]
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], [...]]




```python
L[-1][-1]
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], [...]]




```python
del L[-1]
```


```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3]]




```python
L.extend([1, 2, 3])
```


```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], 1, 2, 3]




```python
L.extend('abc')
```


```python
%pprint
```

    Pretty printing has been turned OFF



```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], 1, 2, 3, 'a', 'b', 'c']




```python
L.append('abc')
```


```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], 1, 2, 3, 'a', 'b', 'c', 'abc']




```python
L.clear?
```


    [0;31mSignature:[0m [0mL[0m[0;34m.[0m[0mclear[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m Remove all items from list.
    [0;31mType:[0m      builtin_function_or_method




```python
L.pop()
```




    'abc'




```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], 1, 2, 3, 'a', 'b', 'c']




```python
res = L[-1]
del L[-1]
res
```




    'c'




```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], 1, 2, 3, 'a', 'b']




```python
L.pop?
```


    [0;31mSignature:[0m [0mL[0m[0;34m.[0m[0mpop[0m[0;34m([0m[0mindex[0m[0;34m=[0m[0;34m-[0m[0;36m1[0m[0;34m,[0m [0;34m/[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Remove and return item at index (default last).
    
    Raises IndexError if list is empty or index is out of range.
    [0;31mType:[0m      builtin_function_or_method




```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], 1, 2, 3, 'a', 'b']




```python
L.remove('a')
```


```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], 1, 2, 3, 'b']




```python
L.remove('a')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_66268/1239804139.py in <module>
    ----> 1 L.remove('a')
    

    ValueError: list.remove(x): x not in list



```python
L.remove?
```


    [0;31mSignature:[0m [0mL[0m[0;34m.[0m[0mremove[0m[0;34m([0m[0mvalue[0m[0;34m,[0m [0;34m/[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.
    [0;31mType:[0m      builtin_function_or_method




```python
reversed(L)
```




    <list_reverseiterator object at 0x7f43f20661d0>




```python
list(reversed(L))
```




    ['b', 3, 2, 1, [1, 2, 3], 15, 10, 34, 500, 34, 300, 34, 123, 100, 34, 3, 34]




```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], 1, 2, 3, 'b']




```python
L[::-1]
```




    ['b', 3, 2, 1, [1, 2, 3], 15, 10, 34, 500, 34, 300, 34, 123, 100, 34, 3, 34]




```python
L
```




    [34, 3, 34, 100, 123, 34, 300, 34, 500, 34, 10, 15, [1, 2, 3], 1, 2, 3, 'b']




```python
L.reverse()
```


```python
None
```


```python
L
```




    ['b', 3, 2, 1, [1, 2, 3], 15, 10, 34, 500, 34, 300, 34, 123, 100, 34, 3, 34]




```python
sorted(L)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_66268/4164961932.py in <module>
    ----> 1 sorted(L)
    

    TypeError: '<' not supported between instances of 'int' and 'str'



```python
del L[0]
```


```python
sorted(L)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_66268/4164961932.py in <module>
    ----> 1 sorted(L)
    

    TypeError: '<' not supported between instances of 'list' and 'int'



```python
L
```




    [3, 2, 1, [1, 2, 3], 15, 10, 34, 500, 34, 300, 34, 123, 100, 34, 3, 34]




```python
L.remove([1, 2, 3])
```


```python
sorted(L)
```




    [1, 2, 3, 3, 10, 15, 34, 34, 34, 34, 34, 100, 123, 300, 500]




```python
L
```




    [3, 2, 1, 15, 10, 34, 500, 34, 300, 34, 123, 100, 34, 3, 34]




```python
L.sort()
```


```python
L
```




    [1, 2, 3, 3, 10, 15, 34, 34, 34, 34, 34, 100, 123, 300, 500]




```python
sorted?
```


    [0;31mSignature:[0m [0msorted[0m[0;34m([0m[0miterable[0m[0;34m,[0m [0;34m/[0m[0;34m,[0m [0;34m*[0m[0;34m,[0m [0mkey[0m[0;34m=[0m[0;32mNone[0m[0;34m,[0m [0mreverse[0m[0;34m=[0m[0;32mFalse[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
    [0;31mType:[0m      builtin_function_or_method




```python
unsorted = 'ffgGvgXcbrx'
```


```python
sorted(unsorted)
```




    ['G', 'X', 'b', 'c', 'f', 'f', 'g', 'g', 'r', 'v', 'x']




```python
sorted?
```


    [0;31mSignature:[0m [0msorted[0m[0;34m([0m[0miterable[0m[0;34m,[0m [0;34m/[0m[0;34m,[0m [0;34m*[0m[0;34m,[0m [0mkey[0m[0;34m=[0m[0;32mNone[0m[0;34m,[0m [0mreverse[0m[0;34m=[0m[0;32mFalse[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
    [0;31mType:[0m      builtin_function_or_method




```python
str.casefold?
```


    [0;31mSignature:[0m [0mstr[0m[0;34m.[0m[0mcasefold[0m[0;34m([0m[0mself[0m[0;34m,[0m [0;34m/[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m Return a version of the string suitable for caseless comparisons.
    [0;31mType:[0m      method_descriptor




```python
s = 'A'
```


```python
s.lower()
```




    'a'




```python
s.casefold()
```




    'a'




```python
sorted(unsorted, key=str.casefold)
```




    ['b', 'c', 'f', 'f', 'g', 'G', 'g', 'r', 'v', 'X', 'x']




```python
str.casefold
```




    <method 'casefold' of 'str' objects>




```python
unsorted
```




    'ffgGvgXcbrx'




```python
def my_casefold(value):
    print(value)
    return value.casefold()
```


```python
sorted(unsorted, key=my_casefold)
```

    f
    f
    g
    G
    v
    g
    X
    c
    b
    r
    x





    ['b', 'c', 'f', 'f', 'g', 'G', 'g', 'r', 'v', 'X', 'x']




```python
zip('abc', 'xyz')
```




    <zip object at 0x7f43f213cbc0>




```python
list(zip('abc', 'xyz'))
```




    [('a', 'x'), ('b', 'y'), ('c', 'z')]




```python
for x1, x2 in zip('abc', 'xyz'):
    print(x1, x2)
```

    a x
    b y
    c z



```python
for x in zip('abc', 'xyz'):
    print(x)
```

    ('a', 'x')
    ('b', 'y')
    ('c', 'z')



```python
a, b = (10, 20)
```


```python
a
```




    10




```python
b
```




    20




```python
for x1, x2, x3 in zip('abc', 'xyz', [10, 20, 30]):
    print(x1, x2, x3)
```

    a x 10
    b y 20
    c z 30



```python
for x1, x2, x3 in zip('abcdefg', 'xyz', [10, 20, 30]):
    print(x1, x2, x3)
```

    a x 10
    b y 20
    c z 30



```python
for x1, x2, x3 in zip('abcdefg', 'xyz', [10, 20, 30], strict=True):
    print(x1, x2, x3)
```

    a x 10
    b y 20
    c z 30



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_66268/1363465188.py in <module>
    ----> 1 for x1, x2, x3 in zip('abcdefg', 'xyz', [10, 20, 30], strict=True):
          2     print(x1, x2, x3)


    ValueError: zip() argument 2 is shorter than argument 1



```python
from itertools import zip_longest
```


```python
for x1, x2, x3 in zip_longest('abcdefg', 'xyz', [10, 20, 30]):
    print(x1, x2, x3)
```

    a x 10
    b y 20
    c z 30
    d None None
    e None None
    f None None
    g None None



```python
for x1, x2, x3 in zip_longest('abcdefg', 'xyz', [10, 20, 30], fillvalue=999):
    print(x1, x2, x3)
```

    a x 10
    b y 20
    c z 30
    d 999 999
    e 999 999
    f 999 999
    g 999 999



```python
for index, value in enumerate('abc'):
    print(index, value)
```

    0 a
    1 b
    2 c



```python
for index, value in enumerate('abc', start=12):
    print(index, value)
```

    12 a
    13 b
    14 c


# List Comprehension


```python
L
```




    [1, 2, 3, 3, 10, 15, 34, 34, 34, 34, 34, 100, 123, 300, 500]




```python
[x + 100 for x in L]
```




    [101, 102, 103, 103, 110, 115, 134, 134, 134, 134, 134, 200, 223, 400, 600]




```python
res = []
for x in L:
    res.append(x + 100)
res
```




    [101, 102, 103, 103, 110, 115, 134, 134, 134, 134, 134, 200, 223, 400, 600]




```python
[x + 100 for x in L if x > 10]
```




    [115, 134, 134, 134, 134, 134, 200, 223, 400, 600]




```python
res = []
for x in L:
    if x > 10:
        res.append(x + 100)
res
```




    [115, 134, 134, 134, 134, 134, 200, 223, 400, 600]



# Übungen


```python
inte_lis = list(range(12, 32))
inte_lis[0] = 999
print(inte_lis)
```

    [999, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]



```python
inte_lis
```




    [999, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]




```python
del inte_lis[2:7]
inte_lis
```




    [999, 13, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]




```python
inte_lis[3:6] = range(8)
```


```python
inte_lis
```




    [999, 13, 19, 0, 1, 2, 3, 4, 5, 6, 7, 23, 24, 25, 26, 27, 28, 29, 30, 31]




```python
for x in range(100, 501, 100):
    inte_lis.append(x)
```


```python
inte_lis
```




    [999, 13, 19, 0, 1, 2, 3, 4, 5, 6, 7, 23, 24, 25, 26, 27, 28, 29, 30, 31, 100, 200, 300, 400, 500]




```python
inte_lis.extend(range(100, 501, 100))
```


```python
inte_lis
```




    [999, 13, 19, 0, 1, 2, 3, 4, 5, 6, 7, 23, 24, 25, 26, 27, 28, 29, 30, 31, 100, 200, 300, 400, 500, 100, 200, 300, 400, 500]




```python
inte_lis.pop()
```




    500




```python
inte_lis[:] = inte_lis[:-1]
```


```python
inte_lis
```




    [999, 13, 19, 0, 1, 2, 3, 4, 5, 6, 7, 23, 24, 25, 26, 27, 28, 29, 30, 31, 100, 200, 300, 400, 500, 100, 200, 300]




```python
inte_lis[-1:] = []
```


```python
inte_lis
```




    [999, 13, 19, 0, 1, 2, 3, 4, 5, 6, 7, 23, 24, 25, 26, 27, 28, 29, 30, 31, 100, 200, 300, 400, 500, 100, 200]




```python
import random

shufflist = inte_lis
random.shuffle(shufflist)
def evenator(elem):
    return elem % 2
print('______ Nr 8: ________________')
print(shufflist)
```

    ______ Nr 8: ________________
    [100, 30, 1, 500, 29, 27, 6, 200, 28, 26, 7, 2, 400, 300, 0, 5, 4, 19, 13, 24, 200, 23, 999, 3, 31, 25, 100]



```python
shufflist.sort(key=evenator)
print(shufflist)

```

    [100, 30, 500, 6, 200, 28, 26, 2, 400, 300, 0, 4, 24, 200, 100, 1, 29, 27, 7, 5, 19, 13, 23, 999, 3, 31, 25]



```python
def evenator2(elem):
    return elem % 2, elem
```


```python
sorted(shufflist, key=evenator2)
```




    [0, 2, 4, 6, 24, 26, 28, 30, 100, 100, 200, 200, 300, 400, 500, 1, 3, 5, 7, 13, 19, 23, 25, 27, 29, 31, 999]




```python
evenator2(10)
```




    (0, 10)




```python
evenator2(11)
```




    (1, 11)




```python
evenator2(17)
```




    (1, 17)




```python

```
