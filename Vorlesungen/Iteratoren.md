```python
L = list(range(2, 11))
```


```python
L
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
reversed(L)
```




    <list_reverseiterator at 0x7fefcbbd2d70>




```python
for x in reversed(L):
    print(x, end=' ')
```

    10 9 8 7 6 5 4 3 2 


```python
for x in L[::-1]:
    print(x, end=' ')
```

    10 9 8 7 6 5 4 3 2 


```python
r = reversed(L)
```


```python
for x in r:
    print(x, end=' ')
```

    10 9 8 7 6 5 4 3 2 


```python
for x in r:
    print(x, end=' ')
```


```python
r = reversed(L)
```


```python
list(r)
```




    [10, 9, 8, 7, 6, 5, 4, 3, 2]




```python
list(r)
```




    []




```python
r = reversed(L)
```


```python
next(r)
```




    10




```python
next(r)
```




    9




```python
list(r)
```




    [8, 7, 6, 5, 4, 3, 2]




```python
next(r)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    /tmp/ipykernel_164997/4134984757.py in <module>
    ----> 1 next(r)
    

    StopIteration: 



```python
next(r, 999)
```




    999




```python
next?
```


    [0;31mDocstring:[0m
    next(iterator[, default])
    
    Return the next item from the iterator. If default is given and the iterator
    is exhausted, it is returned instead of raising StopIteration.
    [0;31mType:[0m      builtin_function_or_method




```python
z = zip('abc', 'xyz')
```


```python
next(z)
```




    ('a', 'x')




```python
e = enumerate('abc')
```


```python
next(e)
```




    (0, 'a')



# Generatorausdrücke


```python
[x + 100 for x in L]
```




    [102, 103, 104, 105, 106, 107, 108, 109, 110]




```python
L
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
(x + 100 for x in L)
```




    <generator object <genexpr> at 0x7fefcb6c0120>




```python
g = (x + 100 for x in L)
```


```python
list(g)
```




    [102, 103, 104, 105, 106, 107, 108, 109, 110]




```python
list(g)
```




    []




```python
g = (x + 100 for x in L)
```


```python
next(g)
```




    102




```python
next(g)
```




    103




```python
list(g)
```




    [104, 105, 106, 107, 108, 109, 110]




```python
list(x + 100 for x in L)
```




    [102, 103, 104, 105, 106, 107, 108, 109, 110]




```python
sum(x + 100 for x in L)
```




    954



# Generatorfunktionen 


```python
def simple():
    print('Start')
    yield 1
    print('nach 1')
    yield 2
    print('nach 2')
    yield 3
    print('nach 3')
```


```python
s = simple()
```


```python
s
```




    <generator object simple at 0x7fefcb6c0660>




```python
next(s)
```

    Start





    1




```python
next(s)
```

    nach 1





    2




```python
next(s)
```

    nach 2





    3




```python
next(s)
```

    nach 3



    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    /tmp/ipykernel_164997/1977886155.py in <module>
    ----> 1 next(s)
    

    StopIteration: 



```python
list(simple())
```

    Start
    nach 1
    nach 2
    nach 3





    [1, 2, 3]




```python
def endless(start=0, step=1):
    value = start
    while True:
        yield value
        value += step
```


```python
endless
```




    <function __main__.endless(start=0, step=1)>




```python
e = endless()
```


```python
next(e)
```




    0




```python
next(e)
```




    1




```python
next(e)
```




    2




```python
r10 = range(10)
```


```python
next(r10)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_164997/3776637743.py in <module>
    ----> 1 next(r10)
    

    TypeError: 'range' object is not an iterator



```python
list(r10)
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
list(r10)
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
range(10**100)
```




    range(0, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)




```python

```
