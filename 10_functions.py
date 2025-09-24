# Funciones en Python

def my_function():   # con la palabra def se define una función
    print("Mi primer función en Python")

my_function()    # de esta manera se llama a una función

def sum_two_values(value1, value2): # esta función recibe parámetros
    print(f"{value1} + {value2} = {value1 + value2}")

sum_two_values(13, 7)   # de esta manera se llama a una función que requiere parámetros
sum_two_values("13", "7")  # debido a que python es de tipado dinámico también acepta cadenas sin problema
sum_two_values(13.7, 7.13)

def div_two_values(value1, value2): # esta función retorna la división
    return value1 / value2

print(div_two_values(13, 7))

result = div_two_values(32, 12) # también se puede guardar el valor que retorna la función
print(result)

def grettings(name, surname):
    print(f"¡Hola, {name} {surname}! ¿Cómo estás?")

grettings(surname = "Padilla", name = "Alexa")  # se cambiar el orden en el que se envian los parámetros sin generar conflicto

def grettings_with_default(name, surname, alias = "sin alias"): # parámetros con valor por defecto
    print(f"{name} {surname}, {alias}")

grettings_with_default("Alexa", "Padilla", "AxMish13")
grettings_with_default("Alexa", "Padilla")

def print_texts(*text): # con el asterísco se indica que se pueden pasar tantos parámetros como se quiera,
    print(text)   # es decir, una función con parámetros arbitrarios

print_texts("Hola")
print_texts("Hola", "Python", "AxMish13")

def print_upper_texts(*texts):  
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "AxMish13")

def print_texts(*text):
    print(type(text))

print_texts("Hola")
print_texts("Hola", "Python", "AxMish13")