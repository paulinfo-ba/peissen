```python
def add(a, b):
    """Add two objects.

    A simple test function.
    `a` and `b` can any objects that work with `+``.
    """
    return a + b
```


```python
add(10, 20)
```




    30




```python
add('abc', 'xyz')
```




    'abcxyz'




```python
add([1, 2, 3], [4, 5, 6])
```




    [1, 2, 3, 4, 5, 6]




```python
add('abc', 12)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_140915/3849109216.py in <module>
    ----> 1 add('abc', 12)
    

    /tmp/ipykernel_140915/1362581339.py in add(a, b)
          5     `a` and `b` can any objects that work with `+``.
          6     """
    ----> 7     return a + b
    

    TypeError: can only concatenate str (not "int") to str



```python
add(12, 'abc')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_140915/1276505118.py in <module>
    ----> 1 add(12, 'abc')
    

    /tmp/ipykernel_140915/1362581339.py in add(a, b)
          5     `a` and `b` can any objects that work with `+``.
          6     """
    ----> 7     return a + b
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'



```python
add?
```


    [0;31mSignature:[0m [0madd[0m[0;34m([0m[0ma[0m[0;34m,[0m [0mb[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Add two objects.
    
    A simple test function.
    `a` and `b` can any objects that work with `+``.
    [0;31mFile:[0m      /tmp/ipykernel_140915/1362581339.py
    [0;31mType:[0m      function




```python
def show(text):
    print('Ausgabe:', text)
```


```python
show('Hallo')
```

    Ausgabe: Hallo



```python
add(3, 4)
```




    7




```python
import sys
```


```python
sys.stdout
```




    <ipykernel.iostream.OutStream at 0x7fb2152d8f70>




```python
def show(text):
    print('Ausgabe:', text)
    return
```


```python
def show(text):
    print('Ausgabe:', text)
    return None
```


```python
add(a=2, b=3)
```




    5




```python
add(2, 3)
```




    5




```python
add(a='abc', b='xyz')
```




    'abcxyz'




```python
add(b='xyz', a='abc')
```




    'abcxyz'




```python
add('abc', 'xyz')
```




    'abcxyz'




```python
add('xyz', 'abc')
```




    'xyzabc'




```python
def add_optional(a, b=0):
    return a + b
```


```python
add_optional(2, 3)
```




    5




```python
add_optional(2)
```




    2




```python
add(2)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_140915/2614823102.py in <module>
    ----> 1 add(2)
    

    TypeError: add() missing 1 required positional argument: 'b'



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
for x in range(10):
    print(x, end=' ')
```

    0 1 2 3 4 5 6 7 8 9 


```python
print(1, 2, 3)
```

    1 2 3



```python
print(1, 2, 3, sep='#')
```

    1#2#3



```python
add('abc', b='xyz')
```




    'abcxyz'




```python
add(b='xyz', 'abc')
```


      File "/tmp/ipykernel_140915/2878996043.py", line 1
        add(b='xyz', 'abc')
                          ^
    SyntaxError: positional argument follows keyword argument




```python
add('xyz', a='abc')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_140915/876329656.py in <module>
    ----> 1 add('xyz', a='abc')
    

    TypeError: add() got multiple values for argument 'a'



```python
add_optional('abc', 'xyz')
```




    'abcxyz'




```python
add_optional('abc')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_140915/4260202809.py in <module>
    ----> 1 add_optional('abc')
    

    /tmp/ipykernel_140915/251977376.py in add_optional(a, b)
          1 def add_optional(a, b=0):
    ----> 2     return a + b
    

    TypeError: can only concatenate str (not "int") to str



```python
def add_optional_better(a, b=None):
    if b is None:
        return a
    return a + b
```


```python
add_optional_better('abc')
```




    'abc'




```python
add_optional_better(2, 3)
```




    5




```python
def func(*args):
    print(args)
```


```python
func()
```

    ()



```python
func(10)
```

    (10,)



```python
[10]
```




    [10]




```python
(10)
```




    10




```python
(1 + 2) * 3
```




    9




```python
1 + 2 * 3
```




    7




```python
((((((10))))))
```




    10




```python
func(10, 20)
```

    (10, 20)



```python
def func(**kwargs):
    print(kwargs)
```


```python
func()
```

    {}



```python
func(a=1)
```

    {'a': 1}



```python
func(a=1, b=2)
```

    {'a': 1, 'b': 2}



```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)
```


```python
func()
```

    ()
    {}



```python
func(100, 200, 300, x=10, y=20, z=30)
```

    (100, 200, 300)
    {'x': 10, 'y': 20, 'z': 30}



```python
def call_func(func, *args, **kwargs):
    print(args)
    print(kwargs)
    return func(*args, **kwargs)
```


```python
call_func(add, 2, 3)
```

    (2, 3)
    {}





    5




```python
call_func(add, 2, b=3)
```

    (2,)
    {'b': 3}





    5




```python
call_func(add, a=2, b=3)
```

    ()
    {'a': 2, 'b': 3}





    5




```python
L = list(range(2, 11))
```


```python
L
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
print(L)
```

    [2, 3, 4, 5, 6, 7, 8, 9, 10]



```python
str(L)
```




    '[2, 3, 4, 5, 6, 7, 8, 9, 10]'




```python
print(L[0], L[1], L[2])
```

    2 3 4



```python
print(*L)
```

    2 3 4 5 6 7 8 9 10



```python
print('abc')
```

    abc



```python
print(*'abc')
```

    a b c



```python
print(*'abc', sep='-')
```

    a-b-c



```python
print(*L)
```

    2 3 4 5 6 7 8 9 10



```python
opt = {'sep': ', '}
```


```python
print(*L, **opt)
```

    2, 3, 4, 5, 6, 7, 8, 9, 10



```python
print(*L, sep=', ')
```

    2, 3, 4, 5, 6, 7, 8, 9, 10



```python
def f1():
    return 1


def f2():
    return 2
```


```python
fd = {'a': f1, 'b': f2}
```


```python
fd
```




    {'a': <function __main__.f1()>, 'b': <function __main__.f2()>}




```python
L
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
fd['a']
```




    <function __main__.f1()>




```python
fd['a']()
```




    1




```python
def read_txt(file_name):
    return 'txt'

def read_csv(file_name):
    return 'csv'

def read_xlsx(file_name):
    return 'xlsx'
```


```python
readers = {
    'txt': read_txt,
    'csv': read_csv,
    'xlsx': read_xlsx,
}
```


```python
def read(file_name, readers=readers):
    name, ext = file_name.split('.')
    return readers[ext](file_name)
```


```python
file_name = 'data.txt'
read(file_name)
```




    'txt'




```python
read('data.xlsx')
```




    'xlsx'




```python
def zwei():
    return 10, 20
```


```python
a, b = zwei()
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
zwei()
```




    (10, 20)




```python
10, 20
```




    (10, 20)




```python
res = zwei()
```


```python
res[0]
```




    10




```python
res[1]
```




    20




```python
def limit10(value):
    if value > 10:
        return 10
    return value
```


```python
limit10(12)
```




    10




```python
limit10(4)
```




    4




```python

```
