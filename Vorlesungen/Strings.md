# String-Methoden


```python
s = 'Das ist ein Text!'
```


```python
sm = set(dir(s))
tm = set(dir(()))
```


```python
sm - tm
```




    {'__mod__',
     '__rmod__',
     'capitalize',
     'casefold',
     'center',
     'encode',
     'endswith',
     'expandtabs',
     'find',
     'format',
     'format_map',
     'isalnum',
     'isalpha',
     'isascii',
     'isdecimal',
     'isdigit',
     'isidentifier',
     'islower',
     'isnumeric',
     'isprintable',
     'isspace',
     'istitle',
     'isupper',
     'join',
     'ljust',
     'lower',
     'lstrip',
     'maketrans',
     'partition',
     'removeprefix',
     'removesuffix',
     'replace',
     'rfind',
     'rindex',
     'rjust',
     'rpartition',
     'rsplit',
     'rstrip',
     'split',
     'splitlines',
     'startswith',
     'strip',
     'swapcase',
     'title',
     'translate',
     'upper',
     'zfill'}




```python
tm - sm
```




    {'__class_getitem__'}




```python
s.upper()
```




    'DAS IST EIN TEXT!'




```python
s.lower()
```




    'das ist ein text!'




```python
s.swapcase()
```




    'dAS IST EIN tEXT!'




```python
s.title()
```




    'Das Ist Ein Text!'




```python
s.center(40)
```




    '           Das ist ein Text!            '




```python
s.center(40, '#')
```




    '###########Das ist ein Text!############'




```python
s.ljust(40, '#')
```




    'Das ist ein Text!#######################'




```python
s.rjust(40, '#')
```




    '#######################Das ist ein Text!'




```python
s.rjust(4, '#')
```




    'Das ist ein Text!'




```python
s.startswith('D')
```




    True




```python
s.startswith('Das')
```




    True




```python
s.startswith(s)
```




    True




```python
s.startswith?
```


    [0;31mDocstring:[0m
    S.startswith(prefix[, start[, end]]) -> bool
    
    Return True if S starts with the specified prefix, False otherwise.
    With optional start, test S beginning at that position.
    With optional end, stop comparing S at that position.
    prefix can also be a tuple of strings to try.
    [0;31mType:[0m      builtin_function_or_method




```python
s.endswith(s)
```




    True




```python
s.endswith('!')
```




    True




```python
suffix = 'Text!'
```


```python
s.endswith(suffix)
```




    True




```python
s[-len(suffix):] == suffix
```




    True




```python
s.isalnum?
```


    [0;31mSignature:[0m [0ms[0m[0;34m.[0m[0misalnum[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Return True if the string is an alpha-numeric string, False otherwise.
    
    A string is alpha-numeric if all characters in the string are alpha-numeric and
    there is at least one character in the string.
    [0;31mType:[0m      builtin_function_or_method




```python
s.isidentifier?
```


    [0;31mSignature:[0m [0ms[0m[0;34m.[0m[0misidentifier[0m[0;34m([0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Return True if the string is a valid Python identifier, False otherwise.
    
    Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
    such as "def" or "class".
    [0;31mType:[0m      builtin_function_or_method




```python
'x1'.isidentifier()
```




    True




```python
'1x'.isidentifier()
```




    False




```python
s.isspace()
```




    False




```python
'  \t\n\r\f\v'.isspace()
```




    True




```python
L = ['A', 'B', 'C']
```


```python
''.join(L)
```




    'ABC'




```python
sum(L)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_292022/3114702962.py in <module>
    ----> 1 sum(L)
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'



```python
sum(L, '')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_292022/1339549055.py in <module>
    ----> 1 sum(L, '')
    

    TypeError: sum() can't sum strings [use ''.join(seq) instead]



```python
'#'.join(L)
```




    'A#B#C'




```python
s.split()
```




    ['Das', 'ist', 'ein', 'Text!']




```python
' '.join(s.split())
```




    'Das ist ein Text!'




```python
s2 = 'Das ist   ein \t Text!'
```


```python
' '.join(s2.split())
```




    'Das ist ein Text!'




```python
s2
```




    'Das ist   ein \t Text!'




```python
print(s2)
```

    Das ist   ein 	 Text!



```python
s3 = '   Das ist   ein \t Text!\r\n'
```


```python
s3
```




    '   Das ist   ein \t Text!\r\n'




```python
print(s3)
```

       Das ist   ein 	 Text!
    



```python
s3.strip()
```




    'Das ist   ein \t Text!'




```python
s3.lstrip()
```




    'Das ist   ein \t Text!\r\n'




```python
s3.rstrip()
```




    '   Das ist   ein \t Text!'




```python
s.split()
```




    ['Das', 'ist', 'ein', 'Text!']




```python
s.split(None, 2)
```




    ['Das', 'ist', 'ein Text!']




```python
s.rsplit(None, 2)
```




    ['Das ist', 'ein', 'Text!']




```python
s.split('i', 1)
```




    ['Das ', 'st ein Text!']




```python
s.split?
```


    [0;31mSignature:[0m [0ms[0m[0;34m.[0m[0msplit[0m[0;34m([0m[0msep[0m[0;34m=[0m[0;32mNone[0m[0;34m,[0m [0mmaxsplit[0m[0;34m=[0m[0;34m-[0m[0;36m1[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Return a list of the words in the string, using sep as the delimiter string.
    
    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.
    [0;31mType:[0m      builtin_function_or_method




```python
s.replace('e', 'E')
```




    'Das ist Ein TExt!'




```python
s
```




    'Das ist ein Text!'




```python
s.zfill(40)
```




    '00000000000000000000000Das ist ein Text!'




```python
s.find('e')
```




    8




```python
s.index('e')
```




    8




```python
s.find('ä')
```




    -1




```python
s.index('ä')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /tmp/ipykernel_292022/3896155054.py in <module>
    ----> 1 s.index('ä')
    

    ValueError: substring not found



```python
import re
```


```python
re?
```


    [0;31mType:[0m        module
    [0;31mString form:[0m <module 're' from '/opt/mambaforge/envs/python310/lib/python3.10/re.py'>
    [0;31mFile:[0m        /opt/mambaforge/envs/python310/lib/python3.10/re.py
    [0;31mDocstring:[0m  
    Support for regular expressions (RE).
    
    This module provides regular expression matching operations similar to
    those found in Perl.  It supports both 8-bit and Unicode strings; both
    the pattern and the strings being processed can contain null bytes and
    characters outside the US ASCII range.
    
    Regular expressions can contain both special and ordinary characters.
    Most ordinary characters, like "A", "a", or "0", are the simplest
    regular expressions; they simply match themselves.  You can
    concatenate ordinary characters, so last matches the string 'last'.
    
    The special characters are:
        "."      Matches any character except a newline.
        "^"      Matches the start of the string.
        "$"      Matches the end of the string or just before the newline at
                 the end of the string.
        "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                 Greedy means that it will match as many repetitions as possible.
        "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
        "?"      Matches 0 or 1 (greedy) of the preceding RE.
        *?,+?,?? Non-greedy versions of the previous three special characters.
        {m,n}    Matches from m to n repetitions of the preceding RE.
        {m,n}?   Non-greedy version of the above.
        "\\"     Either escapes special characters or signals a special sequence.
        []       Indicates a set of characters.
                 A "^" as the first character indicates a complementing set.
        "|"      A|B, creates an RE that will match either A or B.
        (...)    Matches the RE inside the parentheses.
                 The contents can be retrieved or matched later in the string.
        (?aiLmsux) The letters set the corresponding flags defined below.
        (?:...)  Non-grouping version of regular parentheses.
        (?P<name>...) The substring matched by the group is accessible by name.
        (?P=name)     Matches the text matched earlier by the group named name.
        (?#...)  A comment; ignored.
        (?=...)  Matches if ... matches next, but doesn't consume the string.
        (?!...)  Matches if ... doesn't match next.
        (?<=...) Matches if preceded by ... (must be fixed length).
        (?<!...) Matches if not preceded by ... (must be fixed length).
        (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                           the (optional) no pattern otherwise.
    
    The special sequences consist of "\\" and a character from the list
    below.  If the ordinary character is not on the list, then the
    resulting RE will match the second character.
        \number  Matches the contents of the group of the same number.
        \A       Matches only at the start of the string.
        \Z       Matches only at the end of the string.
        \b       Matches the empty string, but only at the start or end of a word.
        \B       Matches the empty string, but not at the start or end of a word.
        \d       Matches any decimal digit; equivalent to the set [0-9] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode digits.
        \D       Matches any non-digit character; equivalent to [^\d].
        \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode whitespace characters.
        \S       Matches any non-whitespace character; equivalent to [^\s].
        \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
                 in bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the
                 range of Unicode alphanumeric characters (letters plus digits
                 plus underscore).
                 With LOCALE, it will match the set [0-9_] plus characters defined
                 as letters for the current locale.
        \W       Matches the complement of \w.
        \\       Matches a literal backslash.
    
    This module exports the following functions:
        match     Match a regular expression pattern to the beginning of a string.
        fullmatch Match a regular expression pattern to all of a string.
        search    Search a string for the presence of a pattern.
        sub       Substitute occurrences of a pattern found in a string.
        subn      Same as sub, but also return the number of substitutions made.
        split     Split a string by the occurrences of a pattern.
        findall   Find all occurrences of a pattern in a string.
        finditer  Return an iterator yielding a Match object for each match.
        compile   Compile a pattern into a Pattern object.
        purge     Clear the regular expression cache.
        escape    Backslash all non-alphanumerics in a string.
    
    Each function other than purge and escape can take an optional 'flags' argument
    consisting of one or more of the following module constants, joined by "|".
    A, L, and U are mutually exclusive.
        A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
                       match the corresponding ASCII character categories
                       (rather than the whole Unicode categories, which is the
                       default).
                       For bytes patterns, this flag is the only available
                       behaviour and needn't be specified.
        I  IGNORECASE  Perform case-insensitive matching.
        L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
        M  MULTILINE   "^" matches the beginning of lines (after a newline)
                       as well as the string.
                       "$" matches the end of lines (before a newline) as well
                       as the end of the string.
        S  DOTALL      "." matches any character at all, including the newline.
        X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
        U  UNICODE     For compatibility only. Ignored for string patterns (it
                       is the default), and forbidden for bytes patterns.
    
    This module also defines an exception 'error'.



# Formatierung

## `f`-String


```python
a = 100
b = 45.78672435
c = s
```


```python
f'{a} {b} {c}'
```




    '100 45.78672435 Das ist ein Text!'




```python
f'{a} {b:f} {c}'
```




    '100 45.786724 Das ist ein Text!'




```python
f'{a:07d} {b:5.2f} {c}'
```




    '0000100 45.79 Das ist ein Text!'




```python
round(2.5)
```




    2




```python
round(3.5)
```




    4




```python
a.__round__?
```


    [0;31mDocstring:[0m
    Rounding an Integral returns itself.
    
    Rounding with an ndigits argument also returns an integer.
    [0;31mType:[0m      builtin_function_or_method




```python
f'{a:07d} {b:5.2f} {c:>25s}'
```




    '0000100 45.79         Das ist ein Text!'




```python
L = list(range(2, 11))
```


```python
L
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]




```python
f'{L[2]} {L[2:4]} {sum(L)}'
```




    '4 [4, 5] 54'



## `.format()`


```python
'{a:07d} {b:5.2f} {c:>25s}'.format(a=a, b=b, c=c)
```




    '0000100 45.79         Das ist ein Text!'




```python
'{a:07d} {b:5.2f} {c:>25s}'.format(**locals())
```




    '0000100 45.79         Das ist ein Text!'




```python
def add(x, y):
    return x + y
```


```python
add('abc', 'xyz')
```




    'abcxyz'




```python
add(x='abc', y='xyz')
```




    'abcxyz'




```python
x='abc'
y='xyz'
```


```python
add(**{'x': 'abc', 'y': 'xyz'})
```




    'abcxyz'




```python
add(**locals())
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_292022/1709032891.py in <module>
    ----> 1 add(**locals())
    

    TypeError: add() got an unexpected keyword argument '__name__'



```python
a
```




    100




```python
'{:07d} {:5.2f} {:>25s}'.format(a, b, c)
```




    '0000100 45.79         Das ist ein Text!'



## `printf`


```python
'%d' %a
```




    '100'




```python
'%d %f' % (a, b)
```




    '100 45.786724'




```python
'%07d %5.2f %25s' % (a, b, c)
```




    '0000100 45.79         Das ist ein Text!'




```python
'%(a)07d %(b)5.2f %(c)25s' % {'a': a, 'b': b, 'c': c}
```




    '0000100 45.79         Das ist ein Text!'




```python
'%(a)07d %(b)5.2f %(c)25s' % locals()
```




    '0000100 45.79         Das ist ein Text!'




```python
template = """Template

{value}
"""
```


```python
print(template.format(value=100))
```

    Template
    
    100
    



```python
value = 100
```


```python
print(eval('f"""' + template + '"""'))
```

    Template
    
    100
    



```python
'f"' + template + '"'
```




    'f"Template\n\n{value}\n"'




```python
import os
```


```python
os.get_terminal_size()
```


    ---------------------------------------------------------------------------

    OSError                                   Traceback (most recent call last)

    /tmp/ipykernel_292022/271837670.py in <module>
    ----> 1 os.get_terminal_size()
    

    OSError: [Errno 25] Inappropriate ioctl for device



```python
s
```




    'Das ist ein Text!'




```python
'_'.join(s.split())
```




    'Das_ist_ein_Text!'




```python

```
