```python
L1 = [1, 2, 3]
L2 = [1, 2, 3]
```


```python
L1 == L2
```




    True




```python
id(L1)
```




    140420198984832




```python
id(L2)
```




    140420198984576




```python
L3 = L2
```


```python
L3
```




    [1, 2, 3]




```python
L3 == L2
```




    True




```python
L3 is L2
```




    True




```python
L1 is L2
```




    False




```python
L3[1] = 100
```


```python
L3
```




    [1, 100, 3]




```python
L2
```




    [1, 100, 3]




```python
id(L2)
```




    140420198984576




```python
id(L3)
```




    140420198984576




```python
L3 = 5
```


```python
L3
```




    5




```python
L2
```




    [1, 100, 3]




```python
int('5')
```




    5




```python
L4 = L2.copy()
```


```python
L5 = L2[:]
```


```python
L2.copy?
```


    [0;31mSignature:[0m [0mL2[0m[0;34m.[0m[0mcopy[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m Return a shallow copy of the list.
    [0;31mType:[0m      builtin_function_or_method




```python
import copy
```


```python
copy?
```


    [0;31mType:[0m        module
    [0;31mString form:[0m <module 'copy' from '/opt/mambaforge/envs/python310/lib/python3.10/copy.py'>
    [0;31mFile:[0m        /opt/mambaforge/envs/python310/lib/python3.10/copy.py
    [0;31mDocstring:[0m  
    Generic (shallow and deep) copying operations.
    
    Interface summary:
    
            import copy
    
            x = copy.copy(y)        # make a shallow copy of y
            x = copy.deepcopy(y)    # make a deep copy of y
    
    For module specific errors, copy.Error is raised.
    
    The difference between shallow and deep copying is only relevant for
    compound objects (objects that contain other objects, like lists or
    class instances).
    
    - A shallow copy constructs a new compound object and then (to the
      extent possible) inserts *the same objects* into it that the
      original contains.
    
    - A deep copy constructs a new compound object and then, recursively,
      inserts *copies* into it of the objects found in the original.
    
    Two problems often exist with deep copy operations that don't exist
    with shallow copy operations:
    
     a) recursive objects (compound objects that, directly or indirectly,
        contain a reference to themselves) may cause a recursive loop
    
     b) because deep copy copies *everything* it may copy too much, e.g.
        administrative data structures that should be shared even between
        copies
    
    Python's deep copy operation avoids these problems by:
    
     a) keeping a table of objects already copied during the current
        copying pass
    
     b) letting user-defined classes override the copying operation or the
        set of components copied
    
    This version does not copy types like module, class, function, method,
    nor stack trace, stack frame, nor file, socket, window, nor any
    similar types.
    
    Classes can use the same interfaces to control copying that they use
    to control pickling: they can define methods called __getinitargs__(),
    __getstate__() and __setstate__().  See the documentation for module
    "pickle" for information on these methods.




```python
import sys
```


```python
sys.getrefcount(L2)
```




    29




```python
sys.getrefcount(4)
```




    700




```python
sys.getrefcount(0)
```




    6102




```python
sys.getrefcount(1000)
```




    3




```python
sys.getsizeof(3)
```




    28




```python
sys.getsizeof(10**100)
```




    72




```python
sys.getsizeof(10**1_000)
```




    468




```python
sys.getsizeof(1.0)
```




    24




```python
isinstance(1, int)
```




    True




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
float.mro()
```




    [float, object]




```python
repr(L1)
```




    '[1, 2, 3]'




```python
L1
```




    [1, 2, 3]




```python
str(L1)
```




    '[1, 2, 3]'




```python
str('a')
```




    'a'




```python

```


```python
repr('a')
```




    "'a'"




```python
eval("'a'")
```




    'a'




```python
eval('1 + 1')
```




    2




```python
L5 = list('abc')
```


```python
L5
```




    ['a', 'b', 'c']




```python
a_2 = 234
```


```python
2_x =46
```


      File "/tmp/ipykernel_286425/1689454396.py", line 1
        2_x =46
         ^
    SyntaxError: invalid decimal literal




```python
_
```




    ['a', 'b', 'c']




```python
for x in range(3):
    print('Hallo')
```

    Hallo
    Hallo
    Hallo



```python
for _ in range(3):
    print('Hallo')
```

    Hallo
    Hallo
    Hallo



```python
über = 34
```


```python
über
```




    34




```python
π = 3.14
```


```python
π
```




    3.14




```python
for = 45
```


      File "/tmp/ipykernel_286425/4052195488.py", line 1
        for = 45
            ^
    SyntaxError: invalid syntax




```python
sum
```




    <function sum(iterable, /, start=0)>




```python
sum = 0
```


```python
sum
```




    0




```python
del sum
```


```python
sum
```




    <function sum(iterable, /, start=0)>




```python
import keyword
```


```python
keyword.kwlist
```




    ['False',
     'None',
     'True',
     'and',
     'as',
     'assert',
     'async',
     'await',
     'break',
     'class',
     'continue',
     'def',
     'del',
     'elif',
     'else',
     'except',
     'finally',
     'for',
     'from',
     'global',
     'if',
     'import',
     'in',
     'is',
     'lambda',
     'nonlocal',
     'not',
     'or',
     'pass',
     'raise',
     'return',
     'try',
     'while',
     'with',
     'yield']




```python
L = [3, 1, 6, 5, 1, 8, 9, 10]
```


```python
sorted(L)
```




    [1, 1, 3, 5, 6, 8, 9, 10]




```python
def even_first(value):
    return value % 2
```


```python
sorted(L, key=even_first)
```




    [6, 8, 10, 3, 1, 5, 1, 9]




```python
sorted(L, key=lambda value: value % 2)
```




    [6, 8, 10, 3, 1, 5, 1, 9]




```python
snake_case = 100
```


```python
class CamelCase:
    pass
```


```python
CONST = 1000
```


```python
import sys
```


```python
_intern = 100
```


```python
int_ = 100
```


```python
id
```




    <function id(obj, /)>




```python
id_ = 1
```


```python
id_
```




    1




```python
sum_ = 0
```


```python
for_ = 12
```


```python
class A:
    
    def _intern(self):
        pass
    
    def __geheim(self):
        pass
```


```python
a = A()
```


```python
a._intern
```




    <bound method A._intern of <__main__.A object at 0x7fb609229600>>




```python
a._A__geheim
```




    <bound method A.__geheim of <__main__.A object at 0x7fb609229600>>




```python
A.__dict__
```




    mappingproxy({'__module__': '__main__',
                  '_intern': <function __main__.A._intern(self)>,
                  '_A__geheim': <function __main__.A.__geheim(self)>,
                  '__dict__': <attribute '__dict__' of 'A' objects>,
                  '__weakref__': <attribute '__weakref__' of 'A' objects>,
                  '__doc__': None})




```python

```
