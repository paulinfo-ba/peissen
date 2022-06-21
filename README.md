# peissen
## Strings:
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Strings.PNG" width="550">
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/fString.PNG" width="550">

## Mengen
```python
s1 = {3, 3, 1, 2, 3, 4, 5, 4, 3, 2, 1}
```


```python
s1
```




    {1, 2, 3, 4, 5}




```python
{'d', 10, 3, 2, 1, 50, 'a'}
```




    {1, 10, 2, 3, 50, 'a', 'd'}
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Mengen.PNG" width="600">

## Sequenzen:
```python
s = 'abcdefghijklm'
```
```python
s[-1]
```
```python
'ac' in s
```

<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/sequenzen.PNG" width="550">

## Liste:
```python
L = list(range(2, 11))
```
```python
L
```




    [2, 3, 4, 5, 6, 7, 8, 9, 10]


<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Listen.PNG" width="550">

## Dictionary:
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Dictionary.PNG" width="550">

## Funktionen:

<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Funktionen, Liste und Dictionary.PNG" width="250">

## Klasse:
```python
class AddierbaresAutoRepr:
    """
    Ein einfaches Auto.

    Kann nur fahren.
    """

    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe
        self.km_stand = 0

    def fahre(self, km):
        """Erhöhe `km_stand` um `km`. """
        self.km_stand += km

    def __add__(self, other):
        return AddierbaresAuto(self.marke + other.marke,
                               self.farbe + other.farbe)
    def __repr__(self):
        return f'AddierbaresAutoRepr({self.marke!r}, {self.farbe!r})'
```

<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Spezielle_Methoden.PNG" width="550">

## Dateien:
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Dateien.PNG" width="550">

## Bibliotheken:
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Biblio.PNG" width="650">

## Eingabe:
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Eingabe.PNG" width="450">

### Exception:

<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Exception.PNG" width="450">
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/excep_finally.PNG" width="650">

### Generatorausdrücke und -funktionen:
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Generatorausdrücke.PNG" width="450">
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Genratorfunktionen.PNG" width="650">


### Namensgebung:
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Namensgebung.PNG" width="450">

### Zeitmessung:
<img src="https://raw.githubusercontent.com/paulinfo-ba/peissen/main/Bilder/Zeitmessung.PNG" width="650">
