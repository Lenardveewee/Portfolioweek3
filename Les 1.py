Les 1: Starten met Python

Practice Exercise 1.1 (expressions)

			Uitkomst	Type
5			5			Int
5.0			5.0			Float
5 % 2		1			int
5 > 1		true		bool exp
‘5’			‘5’			Str
5*2			10			Int
‘5’*2		‘55’		Str
‘5’+’2’		‘52’		Str
5/2	        2.5		    Float
5//2	    2	        Int
[5, 2, 1]	[5, 2, 1]	List
5 in [1, 4, 6]	false	Boolean

Practice Exercise 1.2 (strings)

Schrijf en evalueer Python expressies die de volgende vragen beantwoorden:

1.	Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious'?
>>> string = 'Supercalifragilisticexpialidocious'
>>> print len(string)
34

2.	Komt in 'Supercalifragilisticexpialidocious' de tekst 'ice' voor?
>>> str = 'Supercalifragilisticexpialidocious'
>>> str.count('ice')

>>> A = 'Supercalifragilisticexpialidocious'
>>> B = ‘ice’
>>> B in A
true

3.	Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?
>>> len('Antidisestablishmentarianism') > len('Honorificabilitudinitatibus')
True

 
4.	Welke componist komt in alfabetische volgorde het eerst: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'? Welke het laatst?
>>> list = ['berlioz', 'borodin', 'brian', 'bartok', 'Belini', 'Buxthude', 'Bernstein']
>>> list.sort()
['Belini', 'Bernstein', 'Buxthude', 'bartok', 'berlioz', 'borodin', 'brian']

Practice Exercise 1_3 (statements)
Schrijf Python statements die het volgende doen:
1.	Ken de waarde 6 toe aan variabele a, en waarde 7 aan variabele b.
>>> a = 6
>>> b = 7

2.	Ken aan variabele c als waarde het gemiddelde van a en b toe.
>>> a = 6
>>> b = 7
>>> c = ((a + b) / 2)
>>> c
6.5
()

Practice Exercise 1_4 (boolean expressions)
Schrijf booleaanse expressies die van de variabelen van Practice Exercise 1_3 evalueren of:

1.	6.75 groter is dan a en kleiner b.
>>> 6.75 > a+b
False

2.	de lengte van inventaris meer dan 5 keer zo groot is als de lengte van variabele mijnnaam.
>>> inventaris = ['papier', 'nietjes', 'pennen']
>>> voornaam = 'brunhilde'
>>> tussenvoegsel = ‘ ‘
>>> achternaam = 'vink'
>>> mijnnaam = voornaam + tussenvoegsel + achternaam
>>> len('inventaris') * 5 > len('mijnnaam')
True

3.	de lijst inventaris leeg is, of juist meer dan 10 items bevat.
>>> len('inventaris') >= 0 or 10
Practice Exercise 1_6 (lists)
Het bereik van een lijst is het verschil tussen het grootste en het kleinste getal. Schrijf een Python expressie die het bereik van een lijst berekent. Als bijvoorbeeld variabele list bestaat uit de getallen 3, 7, -2 en 12, dan moet de expressie evalueren naar 14 (verschil tussen 12 en -2). Zorg dat de expressie altijd werkt, ook al bestaat de lijst uit andere waarden!

>>> numlist = [3, 7, -2, 12]
>>> max_val = max(numlist)
>>> min_val = min(numlist)
>>> outcome = (max_val) - (min_val)
>>> print(outcome)
14