# Modulos en Python

import module   # de esta forma se importa todo el código que haya en el módulo

module.sum_values(13, 7 , 3)    # así se llama a la función de un módulo
module.triangle(7)

from module import sum_values, triangle # de esta forma se importan solo algunas funciones de un módulo

sum_values(13, 7, 5)    # ahora se pueden llamar directamente
triangle(13)

import math # importar un módulo propio del lenguaje

print(math.pi)
print(math.pow(13, 3))

from math import e as E_VALUE   # se puede renombrar lo que se importa con 'as'

print(E_VALUE)