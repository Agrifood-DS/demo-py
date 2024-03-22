# -*- coding: utf-8 -*-
"""basic.ipynb



B2. Programación básica I: Condiciones y bucles

**OPERADORES**

Operadores aritméticos
"""

x = 15
y = 2

print("x + y:", x + y)
print("x - y:", x - y)
print("y^2:", y ** 2)
print("x % 2:", x % 5)
print("x / y:", x / y)
print("x // y:", x // y)

"""Operadores de comparación"""

x = 5
y = 3

print("x == y", x == y)
print("x != y", x != y)
print("x > y", x > y)
print("x < y", x < y)
print("x >= y", x >= y)
print("x <= y", x <= y)

"""Comparadores lógicos"""

x = 8

print(x > 3 and x < 10)


print(x > 3 or x < 4)

x = 6

print(not(x > 3 and x < 10))

"""Operadores de pertenencia"""

x = ["apple", "banana", "olives"]

print("banana" in x)
print("patata" not in x)
print("banana" not in x)

"""---

**Condiciones**
"""

a = 50
b = 10

if b > a:
  print(b, "es más grande que", a)
else:
  print(b, "es más pequeño que", b)

a = 22
b = 100

if b > a:
  print(b, "es más grande que", a)
else:
  print(b, "es más pequeño que", a)

print("Enter a number: ")
xString = input()
x = int(xString)
if x % 2 == 0:
    print(x, "es un número par")
elif x == 0:
    print(x, "es igual a 0")
else:
    print(x, "es un número impar")

"""---

# **Ex1**
ejemplos sobre condiciones
"""

import random

#random.seed(6)

theNumber=random.randint(1, 100);


end = False;

while not(end) :
    print("Quin número creus que és?. En cas de voler abandonar escriu -1");
    n = int(input());

    if (n<0) :
        print("Gràcies per participar. Fins aviat");
        end = True;
    elif (n < theNumber):
        print("El nombre que cerques és més gran");
    elif (n > theNumber):
        print("El nombre que cerques és més petit");
    elif (n == theNumber):
        print(F"Ho has encertat era el {theNumber}!!")
        end = True;

"""## **Bucles**

**The while Loop**
"""

i = 0
while i < 6:
  print(i)
  i += 1

"""**The while loop - Break**"""

i = 0
while i < 6:
  print(i)
  if (i == 4):
    break
  i += 1

"""**The while loop - continue**"""

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

"""**The while loop - else**"""

i = 0
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

"""**For loop - range**"""

for i in range(0, 15):
  print(i)

"""**For loop - range II**"""

for i in range(0,15,2):
  print(i)

"""---

**List Comprehension vs. Loops**
"""

temperatures = [22, 24, 19, 24, 27, 29, 25]
above_25 = [temp for temp in temperatures if temp > 25]
above_25

temperatures = [22, 24, 19, 24, 27, 29, 25]
out=[]
for temp in temperatures:
  if temp >25:
    out.append(temp)
out

"""**List Comprehension vs. Loops - II**"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
newlist

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
fruits[2:4]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for i in range(0, len(fruits)-1):
  if i >= 2 and i<=4:
    newlist.append(fruits[i])
newlist

"""---

# **Ex2**


Desarrollar un algoritmo que gestione las entradas y salidas de una cisterna existente en una finca agrícola que gestiona sus recusos hídricos. La cisterna tiene un volumen determinado inical
"""

def depositoCisterna(inicial, s):
    """
    s es un string formado por los
    caracteres + y - que representa
    la evolucion de los días de lluvia.
    "+" indica que ese día ha llovido y las necesidades
    hídricas de la finca quedan satisfechas
    "-" indica que la bomba ha sacado de la cisterna
    las necesidades hídricas de ese día en la finca

    Retorna la capacidad que resta de la cisterna

    >>> depositoCisterna(4, '++++--+')
    7
    >>> depositoCisterna(3,'++++++++++----+')
    11
    >>> depositoCisterna(0,'+-++--+++---++--')
    0
    """

#
#
#

resto = depositoCisterna(4, '++++--+')
print(resto)

resto = depositoCisterna(3,'++++++++++----+')
print(resto)

resto = depositoCisterna(0,'+-++--+++---++--')
print(resto)

"""---

# **Ex3**
Imagínate poder manejar un tractor con solo unos simples comandos que determinen el avance de un vehículo agrícola únicamente indicando su orden (norte, sur, este y oeste) de movimientos

    Dado un string 'line' formado con
    las letras n, s, e y o,
    retorna True si y solo si el tractor
    termina en la posicion de salida.
    >>> action('nseo')
    True
    >>> action('nen')
    False
"""

def action(line):
    """
    Dado un string 'line' formado con
    las letras n, s, e y o,
    retorna True si y solo si el tractor
    termina en la posicion de salida.
    Cada letra determina un movimiento en
    una coordenada.
    Ejemplo:
    >>> action('nseo')
    True
    >>> action('nen')
    False
    """
    mv = 0
    mh = 0

###    return ()

ret = action('nseo')
print(ret)

ret = action('nen')
print(ret)

"""---

# **Ej4**
Dibuja una finca de un terreno agrícola indicando la forma del cuadrado vacío
"""

def empty_square(n):
    '''
    Dado un número entero n > 2,
    dibuja una finca en forma de cuadrado vacío de dimensión n vacío.
    >>> empty_square(3)
    ***
    * *
    ***
    >>> empty_square(5)
    *****
    *   *
    *   *
    *   *
    *****
    '''
    s=""

  ###
  ### TO-DO
  ###

empty_square(3)

empty_square(5)

empty_square(8)

"""# **Diccionarios**

ejemplos sobre diccionarios

---
"""

# Crear el diccionario de inventario
inventario = {
    "manzanas": 50,
    "plátanos": 30,
    "naranjas": 40,
    "peras": 25
}

# 1. Agregar 10 mangos al inventario
inventario["mangos"] = 10

# Imprimir el inventario después de agregar mangos
print("Inventario después de agregar mangos:", inventario)

# 2. Eliminar las peras del inventario
del inventario["peras"]

# Imprimir el inventario después de eliminar peras
print("Inventario después de eliminar peras:", inventario)

# 3. Actualizar la cantidad de naranjas en el inventario a 50
inventario["naranjas"] = 50

# Imprimir el inventario después de actualizar naranjas
print("Inventario después de actualizar naranjas:", inventario)

"""---

# **Ej5**
En un Centro de control de plagas se desea controlar la carga de enfermedades como mosca de la fruta en cítricos. Por este motivo se registra en un diccionario el nombre de la finca y la carga  detectada después de hacer una prueba. Este valor es númerico

Diseña una función que, dado este diccionario de entrada y un valor límite de carga, devuelva una lista ordenada con los nombres de las fincas que superan el valor límite. En caso de que ninguna persona supere el valor
límite, la función debe devolver la lista vacía.
"""

def plagas(d_enfermedades, limite):

    '''
    Parámetros
    ----------
    d_enfermedades  : dict
               Diccionario con los nombres de las fincas como claves (string)
               y la carga de enfermedades de la fincar (int)

    limite : int
             límite de carga utilizado para filtrar

    Retorna
    -------
    l_result : list
               Lista ordenada alfabéticatemente con los nombres de las fincas
               que superan el límite de carga.


    Ejemplos Públicos
    -----------------

    >>> d_enfermedades = {'finca la nova': 5000,
    ...            'finca de l'avi Pere: 6000,
    ...             'finca de l'olivereta': 3261,
    ...             'Ca la Pepa': 2348,
    ...             'Del Mas': 6150}
    >>> plagas (d_malaties, 3500)
    >>> plagas (d_virus, 9500)
    []
    '''

    l_result=[]

    ### 
    ### TO-DO
    ###

    return l_result

d_enfermedades = {'finca la nova': 5000,
    'finca de l\'avi Pere': 6000,
    'finca de l\'olivereta': 3261,
    'Ca la Pepa': 2348,
    'Del Mas': 6150}

ret = plagas (d_enfermedades, 3500)
print(ret)


ret = plagas (d_enfermedades, 4999)
print(ret)

ret = plagas (d_enfermedades, 5000)
print(ret)

ret = plagas (d_enfermedades, 9500)
print(ret)

"""# **Ej5** - Versión actualizada con un vector de diccionarios"""

def plagas(finques, limite):

    '''
    Parámetros
    ----------
    fincas  : vector de diccionarios
               Diccionario con los nombres de las fincas como claves (string)
               y la carga de enfermedades de la fincar (int)

    limite : int
             límite de carga utilizado para filtrar

    Retorna
    -------
    l_result : list
               Lista ordenada alfabéticatemente con los nombres de las fincas
               que superan el límite de carga.


    Ejemplos Públicos
    -----------------

    >>> fincas = [{'nombre': 'La nova', 'carga': 5000,
    ...            'nombre': 'finca avi Pere , 'carga':6000,
    ...             'nombre': 'Olivereta' , 'carga': 3261,
    ...             'nombre': 'Ca la pepa', 'carga': 2348,
    ...             'nombre': 'Mas del Bages', 'carga': 6150}
    ...           ]
    >>> plagas (fincas, 3500)
    >>> plagas (fincas, 9500)
    []
    '''

    l_result=[]

    ###
    ### TO-DO
    ###

    l_result = sorted(l_result, key=lambda d: d['nombre'])
    #l_result.sort()
    return l_result

fincas = [
                {
                  "nombre":"La nova",
                  "carga": 5000,
                  "cultivo": ["blat", "ordi"]
                },
                {
                  "nombre":"Finca avi Pere",
                  "carga": 6000,
                  "cultivo": ["blat"]
                },
                {
                    "nombre":"Olivereta",
                    "carga": 3261,
                    "cultivo": ["olives"]
                },
                {
                    "nombre":"Ca la Pepa",
                    "carga": 2348,
                    "cultivo": ["atmelles"]
                },
                {
                    "nombre":"Mas del Bages",
                    "carga": 6150,
                    "cultivo": ["vinya"]
                }
                ]

print("0 => ")
ret = plagas (fincas, 0)
print(ret)

print("3500 => ")
ret = plagas (fincas, 3500)
print(ret)

print("4999 => ")
ret = plagas (fincas, 4999)
print(ret)

print("5000 => ")
ret = malalties (fincas, 5000)
print(ret)

print("9500 => ")
ret = malalties (fincas, 9500)
print(ret)