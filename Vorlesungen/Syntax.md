# Kommentare


```python
# Kommentar
```


```python
1 + 1  # Kommentar
```




    2



# Einrückungen


```python
for x in [1, 2, 3]:
    print(x)
print('Ende')
```

    1
    2
    3
    Ende


# Zeilenumbrüche


```python
't1' 't2' 't3'
```




    't1t2t3'




```python
't1' \
't2' \
't3'
```




    't1t2t3'




```python
('t1'
 't2'
 't3')
```




    't1t2t3'




```python
[1,
 2,
 3]
```




    [1, 2, 3]



# Groß- und Kleinschreibung


```python
a = 1
A = 10
```


```python
a
```




    1




```python
A
```




    10



# Strings


```python
'abc'
```




    'abc'




```python
"abc"
```




    'abc'




```python
'Sie sagte: "Hallo!".'
```




    'Sie sagte: "Hallo!".'




```python
"Sie sagte: "Hallo!"."
```


      File "/tmp/ipykernel_5756/4208958009.py", line 1
        "Sie sagte: "Hallo!"."
                     ^
    SyntaxError: invalid syntax




```python
"Sie sagte: \"Hallo!\"."
```




    'Sie sagte: "Hallo!".'




```python
s = """Zeile 1
Zeile 2

Zeile 4
"""
```


```python
s
```




    'Zeile 1\nZeile 2\n\nZeile 4\n'




```python
print(s)
```

    Zeile 1
    Zeile 2
    
    Zeile 4
    



```python
a = 200
```


```python
f'Text mit {a}'
```




    'Text mit 200'




```python
ord('9')
```




    57




```python
chr(57)
```




    '9'




```python
ord?
```


    [0;31mSignature:[0m [0mord[0m[0;34m([0m[0mc[0m[0;34m,[0m [0;34m/[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m Return the Unicode code point for a one-character string.
    [0;31mType:[0m      builtin_function_or_method




```python
chr?
```


    [0;31mSignature:[0m [0mchr[0m[0;34m([0m[0mi[0m[0;34m,[0m [0;34m/[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
    [0;31mType:[0m      builtin_function_or_method




```python

```
