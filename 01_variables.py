# Variables

my_string_variable = "Mi variable tipo string" # convención tipo snake case
print(my_string_variable)

my_int_variable = 13 # variable tipo int
print(my_int_variable)

# Variables en una sola línea
name, surname, alias, age = "Alexa", "Padilla", "Mishima", 23
print("Hola! Soy", name,surname, "tengo", age, "años y mi alias es:", alias)

# concatenación de variables en print
print(my_string_variable, my_int_variable)

my_float_variable = 7.7 
my_complex_str_variable = "13+7j"

# Conversión de tipos de datos
my_int_to_str = str(my_int_variable) # conversión a string
my_float_to_int = int(my_float_variable) # conversión a int
my_complex_variable = complex(my_complex_str_variable) # conversión a complex

print(type(my_int_to_str))
print(type(my_float_to_int))
print(type(my_complex_variable))

print("Valor de mi variable compleja: ", my_complex_variable)

# Algunas funciones del lenguaje

print(len(my_complex_str_variable)) # len() calcula el tañano de un string

# Inputs

name = input("¿Cuál es tu nombre?: ")
age = input("¿Y tu edad?: ")

print(name)
print(age)