```python
a = 5
b = 6
```


```python
a < b
```




    True




```python
True
```




    True




```python
if a < b:
    print('kleiner')
```

    kleiner



```python
a = 50
b = 50
if a < b:  # 1
    print('kleiner')
elif a > b:  # 0, 1, 2, 3 ... n
    print('größer')
else:  # 0, 1
    print('gleich')
```

    gleich



```python
a < b
```




    False




```python
a = 5
b = 6
```


```python
10 if a < b else 100
```




    10




```python
res1 = 10 if a < b else 100
```


```python
if a < b:
    res2 = 10
else:
    res2 = 100
```


```python
res1 == res2
```




    True




```python
10 <= 50 <= 100
```




    True




```python
u = 10
o = 100
w = 50
```


```python
u <= w <= o
```




    True




```python
(u <= w) and (w <= o)
```




    True




```python
True and True
```




    True




```python
True and False
```




    False




```python
False and True
```




    False




```python
False and False
```




    False




```python
False or False
```




    False




```python
False or True
```




    True




```python
True or False
```




    True




```python
True or True
```




    True




```python
1 == 1
```




    True




```python
1 != 2
```




    True




```python
a is a
```




    True




```python
not True
```




    False




```python
not not True
```




    True




```python
'a' in 'abc'
```




    True




```python
'a' not in 'abc'
```




    False




```python
input('Eingabe: ')
```

    Eingabe:  210





    '210'




```python
eingabe = input('Eingabe: ')
```

    Eingabe:  210



```python
eingabe
```




    '210'




```python
eingabe * 2
```




    '210210'




```python
int(eingabe)
```




    210




```python
float(eingabe)
```




    210.0




```python
zahl = float(input('Eingabe: '))
```

    Eingabe:  500



```python
zahl
```




    500.0




```python
a = 4
b = 5
c = 6
```


```python
snake_case = 10
```


```python
class CamelCase:
    pass
```


```python

```
