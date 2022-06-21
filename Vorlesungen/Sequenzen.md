```python
s = 'abcdefghijklm'
```


```python
s
```




    'abcdefghijklm'




```python
s[0]
```




    'a'




```python
s[1]
```




    'b'




```python
s[-1]
```




    'm'




```python
s[len(s) - 1]
```




    'm'




```python
'a' in s
```




    True




```python
'abc' in s
```




    True




```python
'ac' in s
```




    False




```python
'ac' not in s
```




    True




```python
s + s
```




    'abcdefghijklmabcdefghijklm'




```python
s * 3
```




    'abcdefghijklmabcdefghijklmabcdefghijklm'




```python
'#' * 80
```




    '################################################################################'




```python
s[2:4]
```




    'cd'




```python
s
```




    'abcdefghijklm'




```python
s[2:8]
```




    'cdefgh'




```python
s[2:8:2]
```




    'ceg'




```python
s[::2]
```




    'acegikm'




```python
s[1::2]
```




    'bdfhjl'




```python
s[::-1]
```




    'mlkjihgfedcba'




```python
s[2:8:-1]
```




    ''




```python
s[8:2:-1]
```




    'ihgfed'




```python
s[2:8][::-1]
```




    'hgfedc'




```python
s[:4]
```




    'abcd'




```python
s[4:]
```




    'efghijklm'




```python
s[:4] + s[4:] == s
```




    True




```python
assert 1 == 1
```


```python
assert 1 == 2, 'nein'
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    /tmp/ipykernel_51910/3213508889.py in <module>
    ----> 1 assert 1 == 2, 'nein'
    

    AssertionError: nein



```python
for n in range(20):
    print(f'{n:3d} {s[:n]:13s} {s[n:]}')
    assert s[:n] + s[n:] == s
```

      0               abcdefghijklm
      1 a             bcdefghijklm
      2 ab            cdefghijklm
      3 abc           defghijklm
      4 abcd          efghijklm
      5 abcde         fghijklm
      6 abcdef        ghijklm
      7 abcdefg       hijklm
      8 abcdefgh      ijklm
      9 abcdefghi     jklm
     10 abcdefghij    klm
     11 abcdefghijk   lm
     12 abcdefghijkl  m
     13 abcdefghijklm 
     14 abcdefghijklm 
     15 abcdefghijklm 
     16 abcdefghijklm 
     17 abcdefghijklm 
     18 abcdefghijklm 
     19 abcdefghijklm 


Wir machen weiter.


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
a = 10
```


```python
f'{a}'
```




    '10'




```python
str(a)
```




    '10'




```python
f'{a:07d}'
```




    '0000010'




```python
f'{a:07o}'
```




    '0000012'




```python
f'{a:07x}'
```




    '000000a'




```python
s[15]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    /tmp/ipykernel_51910/2880158974.py in <module>
    ----> 1 s[15]
    

    IndexError: string index out of range



```python
s[15:18]
```




    ''




```python
s[:1000]
```




    'abcdefghijklm'




```python
'{a:07x}'
```




    '{a:07x}'




```python
f'{a:07x}'
```




    '000000a'




```python
a
```




    10




```python
f'{a:d}'
```




    '10'




```python
f'{a:.2f}'
```




    '10.00'




```python
len(s)
```




    13




```python
min(s)
```




    'a'




```python
max(s)
```




    'm'




```python
s.count('e')
```




    1




```python
s2 = 'gferarefdre'
```


```python
s2.count('e')
```




    3




```python
s2.count('e', 3)
```




    2




```python
s2.count('e', 3, 5)
```




    0




```python
s2.count?
```


    [0;31mDocstring:[0m
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.
    [0;31mType:[0m      builtin_function_or_method




```python
s2.index('e')
```




    2




```python
s2.index('e', 3)
```




    6




```python
s2.index('e', 3, 5)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_51910/1216506605.py in <module>
    ----> 1 s2.index('e', 3, 5)
    

    ValueError: substring not found



```python
t = (1, 2, 3)
```


```python
t
```




    (1, 2, 3)




```python
print(t)
```

    (1, 2, 3)



```python
print(*t)
```

    1 2 3



```python
print(t[0], t[1], t[2])
```

    1 2 3



```python
tuple()
```




    ()




```python
()
```




    ()




```python
list()
```




    []




```python
tuple(range(10))
```




    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)




```python
list(range(10))
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
list(range(3, 15))
```




    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]




```python
t = ('ab', 2, 3, 44, 234, 32.233, 'sdf', 122.002)
```


```python
%pprint
```

    Pretty printing has been turned OFF



```python
t * 3
```




    ('ab', 2, 3, 44, 234, 32.233, 'sdf', 122.002, 'ab', 2, 3, 44, 234, 32.233, 'sdf', 122.002, 'ab', 2, 3, 44, 234, 32.233, 'sdf', 122.002)




```python
t + t + t == 3* t
```




    True




```python
t[::-1]
```




    (122.002, 'sdf', 32.233, 234, 44, 3, 2, 'ab')




```python
t[::2]
```




    ('ab', 3, 234, 'sdf')




```python
3 in t
```




    True




```python

```
