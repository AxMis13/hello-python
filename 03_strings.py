# Strings en python

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string) # concatenación

# Caracteres de escape
my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string) # \n <- salto de línea

my_tab_string = "\tEste es un string con tabulación al principio"
print(my_tab_string) # \t <- tabulación

# formateo de strings
name, surname, age = "Alexa", "Padilla", 23

# maneras de formatear strings
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # mejor opción

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División o slicing
language_slice = language[1:3]  # [1 <- inicio : 3 <- final] el final no se 
print(language_slice)           # cuenta

language_slice = language[1:]   # como el final está vacío, se toman todos
print(language_slice)           # los caracteres a partir del inicio

language_slice = language[-2]   # con índices negativos comienza desde el
print(language_slice)           # final del string

language_slice = language[0:6:2]# [0:6:2 <- paso] el paso indica cada cunato
print(language_slice)           # toma un caracter

# Reverse
reversed_language = language[::-1]  # si se deja vacío el inicio y fin, toma 
print(reversed_language)            # toda la cadena y con -1 indica que vaya
                                    # en reversa
# Funciones

print(language.capitalize())    # la prime letra en mayúscula
print(language.upper())         # todo en mayúsculas
print(language.count("t"))      # cuenta el caracter especificado
print(language.isnumeric())     # indica si es un número
print("1".isnumeric())
print(language.lower())         # todo en minúsculas
print(language.lower().isupper())   # se pueden encadenar
print(language.startswith("py"))    # para verificar si la cadena empieza
                                    # de la forma especificada. Key sensitive
