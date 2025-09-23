# Condicionales en Python

my_condicion = True
my_other_condition = False

if my_condicion:    # es lo mismo que if my_condition == True
    print("Se ejecuta el if")

if my_other_condition:
    print("Se ejecuta el segundo if")

# un if se ejecuta siempre que la condición sea True

my_condicion = 13 + 7
if my_condicion == 19 and my_condicion < 20:
    print("Se ejecuta el tercer if")
elif my_condicion == 13:        # se imprime si la condición anterior no se cumplió
    print("Se ejecuta el elif") # pero esta sí
else:
    print("Se ejecuta el else") # si imprime si ninguna condición se cumple 
    print("Todo lo que tenga la tabulación adecuada se imprimirá con el else")

my_string = ""

if my_string:   # comprueba que la variable no esté vacía
    print("La cadena no está vacía")
elif my_string == "cadena":
    print("La cadena es 'cadeda'")
elif not my_string:
    print("La cadena está vacía")

print("Continúa el programa")
