# Tuplas

my_tuple = tuple()  # inicializador por constructor
my_other_tuple = () 

my_tuple = (23, 1.78, "Alexa", "Padilla", "Alexa")
my_other_tuple = (23, 60, 35)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])  # se puede acceder a un elemeto por su índice
print(my_tuple[-1]) # o por índices negativos
                    # los índices funcionan igual que con las listas

print(my_tuple.count("Alexa"))      # la misma función que tienen las listas
print(my_tuple.index("Padilla"))    # arroja el índice de la primer coincidencia

#my_tuple[1] = 1.85 | las tuplas son inmutables, por lo que esto genera error
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[2:4])    # también soportan slicing

# conversión de un tupla a una lista y visceversa
my_tuple = list(my_tuple)
print(type(my_tuple))

del my_tuple[-1]
my_tuple.append("Morado")
my_tuple = tuple(my_tuple)

print(my_tuple)
print(type(my_tuple))

del my_tuple    # elimina la variable
# print(my_tuple) | esto da error, la variable ya no está definida
