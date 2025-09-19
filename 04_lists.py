# Listas en Phython
# cuando se habla de listas, se habla ya de estructuras de datos

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [23, 24, 62, 52, 30, 17, 30]

print(my_list)
print(len(my_list))

my_other_list = [23, 1.78, "Alexa", "Padilla"]

print(type(my_other_list))
print(type(my_list))

# acceder a los elementos de una lista
# en python, los índices de las lístas comienzan en cero, por lo que el índice
# máximo es igual al tamaño de la lista menos uno
print(my_other_list[0])     # [0 <- índice] se utilizan corchetes para acceder 
                            # a un elemento
print(my_other_list[-1])    # se pueden utilizar índices negativos
print(my_other_list[-3])
# print(my_other_list[7])   # esto da error: list index out of range
                            # cuidar no sobrepasar el tamaño de la lista

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list) # concatenación de listas

my_other_list.append("Un string")   # agrega un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Naranja")  # inserta el elemento en el índice indicado
print(my_other_list)                # desplazando los elementos existentes

my_other_list[1] = "Morado"     # se puede modificar un índice exacto
print(my_other_list)

my_other_list.remove("Un string")   # elimina la primer coincidencia
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop()   # saca el último elemento y lo retorna
print(my_list)

my_pop_element = my_list.pop(2) # se puede indicar el índice a desapilar
print(my_pop_element)           # pero no es tan habitual
print(my_list)

del my_list[2]  # elimina el elemento del índice
print(my_list)

my_new_list = my_list.copy()    # hace una copia en otra variable

my_list.clear() # limpia la lista, es decir, la deja vacía
print(my_list)
print(my_new_list)

my_new_list.reverse()   # invierte el orden de la lista
print(my_new_list)

my_new_list.sort()  # por defecto, ordena la lista de menor a mayor
print(my_new_list)

print(my_new_list[1:2]) # el slicing también funciona en listas

my_list = "Hola Python" # python usa tipado dinámico, se puede cambiar el tipo
print(my_list)          # de dato que guarda una variable sin problema
print(type(my_list))
