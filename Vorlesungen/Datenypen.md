# Einfache Datentypen


```python
type(1)
```




    int




```python
10**10
```




    10000000000




```python
10**100
```




    10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000




```python
import sys
```


```python
sys.maxsize
```




    9223372036854775807




```python
2**63 - 1
```




    9223372036854775807




```python
type(4.5)
```




    float




```python
sys.float_info
```




    sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)




```python
1e16 + 1
```




    1e+16




```python
1e15 + 1
```




    1000000000000001.0




```python
2 + 6j
```




    (2+6j)




```python
2 + 6j + 10 + 4j
```




    (12+10j)




```python
None
```


```python
print(None)
```

    None



```python
bool(0)
```




    False




```python
bool(4)
```




    True




```python
bool('')
```




    False




```python
bool(' ')
```




    True




```python
a = 0

if a:
    print('ja')
```

# Kollektionen

## Sequenzen


```python
L = [1, 2, 3]
t = (1, 2, 3)
s = 'abc'
```


```python
L[0]
```




    1




```python
t[1]
```




    2




```python
s[2]
```




    'c'




```python
L[10]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    /tmp/ipykernel_46173/1656812641.py in <module>
    ----> 1 L[10]
    

    IndexError: list index out of range


## Dictionarys


```python
d = {'a': 100, 'b': 200, 'c': 300}
```


```python
d
```




    {'a': 100, 'b': 200, 'c': 300}




```python
d['a']
```




    100




```python
d[0]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    /tmp/ipykernel_46173/1089268471.py in <module>
    ----> 1 d[0]
    

    KeyError: 0


## Mengen / Sets

## Klassen


```python
10 % 2
```




    0




```python
11 % 2
```




    1




```python

```
