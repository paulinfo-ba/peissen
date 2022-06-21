```python
1 / 0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    /tmp/ipykernel_236236/1455669704.py in <module>
    ----> 1 1 / 0
    

    ZeroDivisionError: division by zero



```python
a = 1
b = 0
```


```python
try:
    a / b
except ZeroDivisionError:
    print('geht nicht')
```

    geht nicht



```python
try:
    a / b
except ZeroDivisionError as err:
    print('geht nicht')
    e = err
```

    geht nicht



```python
e
```




    ZeroDivisionError('division by zero')




```python
raise e
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    /tmp/ipykernel_236236/1934655291.py in <module>
    ----> 1 raise e
    

    /tmp/ipykernel_236236/3291130715.py in <module>
          1 try:
    ----> 2     a / b
          3 except ZeroDivisionError as err:
          4     print('geht nicht')
          5     e = err


    ZeroDivisionError: division by zero



```python
%xmode Plain
```

    Exception reporting mode: Plain



```python
raise e
```


    Traceback (most recent call last):


      File "/tmp/ipykernel_236236/1934655291.py", line 1, in <module>
        raise e


      File "/opt/mambaforge/envs/python310/lib/python3.10/site-packages/IPython/core/interactiveshell.py", line 3457, in run_code
        exec(code_obj, self.user_global_ns, self.user_ns)


      File "/tmp/ipykernel_236236/1934655291.py", line 1, in <module>
        raise e


      File "/tmp/ipykernel_236236/3291130715.py", line 2, in <module>
        a / b


    ZeroDivisionError: division by zero




```python
%xmode?
```


    [0;31mDocstring:[0m
    Switch modes for the exception handlers.
    
    Valid modes: Plain, Context, Verbose, and Minimal.
    
    If called without arguments, acts as a toggle.
    
    When in verbose mode the value --show (and --hide) 
    will respectively show (or hide) frames with ``__tracebackhide__ =
    True`` value set.
    [0;31mFile:[0m      /opt/mambaforge/envs/python310/lib/python3.10/site-packages/IPython/core/magics/basic.py




```python
%xmode Minimal
```

    Exception reporting mode: Minimal



```python
raise e
```


    ZeroDivisionError: division by zero




```python
%xmode
```

    Exception reporting mode: Plain



```python
%xmode
```

    Exception reporting mode: Context



```python
%xmode
```

    Exception reporting mode: Verbose



```python
raise e
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    /tmp/ipykernel_236236/1934655291.py in <module>
    ----> 1 raise e
            global e = ZeroDivisionError('division by zero')


        [... skipping hidden 1 frame]


    /tmp/ipykernel_236236/1934655291.py in <module>
    ----> 1 raise e
            global e = ZeroDivisionError('division by zero')


        [... skipping hidden 1 frame]


    /tmp/ipykernel_236236/1934655291.py in <module>
    ----> 1 raise e
            global e = ZeroDivisionError('division by zero')


        [... skipping hidden 1 frame]


    /tmp/ipykernel_236236/1934655291.py in <module>
    ----> 1 raise e
            global e = ZeroDivisionError('division by zero')


    /tmp/ipykernel_236236/3291130715.py in <module>
          1 try:
    ----> 2     a / b
            global a = 1
            global b = 0
          3 except ZeroDivisionError as err:
          4     print('geht nicht')
          5     e = err


    ZeroDivisionError: division by zero



```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('geht nicht')
    finally:
        print('immer')
```


```python
divide(1, 0)
```

    geht nicht
    immer



```python
divide(1, 10)
```

    immer





    0.1




```python
isinstance(e, ZeroDivisionError)
```




    True




```python
isinstance(1, int)
```




    True




```python
type(1)
```




    int




```python
isinstance(True, int)
```




    True




```python
type(True)
```




    bool




```python
bool.mro()
```




    [bool, int, object]




```python
True + True
```




    2




```python
isinstance(e, Exception)
```




    True




```python
ZeroDivisionError.mro()
```




    [ZeroDivisionError, ArithmeticError, Exception, BaseException, object]




```python
xyz
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    /tmp/ipykernel_236236/2282940932.py in <module>
    ----> 1 xyz
            global xyz = undefined


    NameError: name 'xyz' is not defined



```python
a = 1
b = 10

try:
    a / b
    xyz
except ZeroDivisionError as err:
    print('geht nicht', err)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    /tmp/ipykernel_236236/485565005.py in <module>
          4 try:
          5     a / b
    ----> 6     xyz
            global xyz = undefined
          7 except ZeroDivisionError as err:
          8     print('geht nicht', err)


    NameError: name 'xyz' is not defined



```python
a = 1
b = 10

try:
    a / b
    xyz
except (ZeroDivisionError, NameError) as err:
    print('geht nicht', err)
```

    geht nicht name 'xyz' is not defined



```python
a = 1
b = 0

try:
    a / b
    xyz
except ZeroDivisionError:
    print('zero')
except NameError:
    print('name')
```

    zero



```python
class MyException(Exception):
    pass
```


```python
raise MyException('von mir')
```


    ---------------------------------------------------------------------------

    MyException                               Traceback (most recent call last)

    /tmp/ipykernel_236236/2738277468.py in <module>
    ----> 1 raise MyException('von mir')
            global MyException = <class '__main__.MyException'>


    MyException: von mir



```python
dict.pop?
```


    [0;31mDocstring:[0m
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    
    If the key is not found, return the default if given; otherwise,
    raise a KeyError.
    [0;31mType:[0m      method_descriptor




```python

```
