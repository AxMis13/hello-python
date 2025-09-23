# Bucles en Python

# bucle While
my_condition = 0

while my_condition < 10:    # un while se repite en función de una condición
    print(my_condition)
    my_condition += 1   # nunca olvidar modificar la condición
else:   # este else es opcional
    print(f"Mi condición ahora vale: {my_condition}")

while my_condition < 20:
    my_condition += 1

    if my_condition == 21:
        print(f"Mi condición vale {my_condition}")
        break   # se fuerza la detención del while

    print(my_condition)
else:
    print("El while finalizó correctamente")    # no se imprime si se ejecuta el break

# bucle For
my_list = [23, 24, 62, 52, 30, 17, 30]

for element in my_list: # un for se repite en función de un objeto iterable
    print(element)      # en cada vuelta accede al elemento del objeto iterable
else:   # este else también es opcional
    print("Finaliza el bucle for")

# los objetos iterables son: listas, tuplas, sets  o diccionarios

my_dict = {
    "Nombre": "Alexa", 
    "Apellido": "Padilla", 
    "Edad": 23, 
    "Lenguajes": {"Python", "C", "C++"},
    1: 1.78,
}

for element in my_dict: # cuando se itera un dict, se obtienen sus claves
    print(element)
    if element == "Edad":
        break
else:
    print("Finaliza el bucle for")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue    # con esto el bucle salta todo lo demás del bloque de código
else:               # y continua al próximo elemento
    print("Finaliza el bucle for")

print("Continúa el programa")