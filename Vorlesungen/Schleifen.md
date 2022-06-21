# `for`-Schleife


```python
for x in [1, 2, 3]:
    print(x)
```

    1
    2
    3



```python
for c in 'abc':
    print(c)
```

    a
    b
    c



```python
for x in 1:
    print(x)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_36007/3543620882.py in <module>
    ----> 1 for x in 1:
          2     print(x)


    TypeError: 'int' object is not iterable



```python
for x in range(10):
    print(x)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



```python
range(10)
```




    range(0, 10)




```python
for x in range(10):
    print(x, end=' ')
```

    0 1 2 3 4 5 6 7 8 9 


```python
print?
```


    [0;31mDocstring:[0m
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    [0;31mType:[0m      builtin_function_or_method




```python
print(1, 2, 3)
```

    1 2 3



```python
print(1, 2, 3, sep=', ')
```

    1, 2, 3



```python
for x in range(2, 10):
    print(x, end=' ')
```

    2 3 4 5 6 7 8 9 


```python
for x in range(2, 10, 2):
    print(x, end=' ')
```

    2 4 6 8 


```python
range?
```


    [0;31mInit signature:[0m [0mrange[0m[0;34m([0m[0mself[0m[0;34m,[0m [0;34m/[0m[0;34m,[0m [0;34m*[0m[0margs[0m[0;34m,[0m [0;34m**[0m[0mkwargs[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m     
    range(stop) -> range object
    range(start, stop[, step]) -> range object
    
    Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
    [0;31mType:[0m           type
    [0;31mSubclasses:[0m     



# `while`-Schleife


```python
x = 0
while x < 10:
    print(x, end=' ')
    x += 1  # x = x + 1
```

    0 1 2 3 4 5 6 7 8 9 

Endlosschleife:

```python
while True:
    pass
```


```python
for x in range(10):
    if x == 5:
        break
    print(x, end=' ')
```

    0 1 2 3 4 


```python
for x in range(10):
    if x == 5:
        continue
    print(x, end=' ')
```

    0 1 2 3 4 6 7 8 9 


```python
10 % 2
```




    0




```python
9 % 2
```




    1




```python
divmod(10, 2)
```




    (5, 0)




```python
divmod(9, 2)
```




    (4, 1)




```python
10 ** 5
```




    100000




```python
pow(10, 5)
```




    100000




```python
pow?
```


    [0;31mSignature:[0m [0mpow[0m[0;34m([0m[0mbase[0m[0;34m,[0m [0mexp[0m[0;34m,[0m [0mmod[0m[0;34m=[0m[0;32mNone[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.
    [0;31mType:[0m      builtin_function_or_method




```python
pow(34, 0.5)
```




    5.830951894845301




```python
import math
```


```python
math.sqrt(34)
```




    5.830951894845301




```python
34 ** 0.5
```




    5.830951894845301




```python

```
