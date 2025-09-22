# Diccionarios en Python

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Alexa", "Apellido":"Padilla", "Edad":23,} # {(clave):(valor)}

my_dict = {
    "Nombre": "Alexa", 
    "Apellido": "Padilla", 
    "Edad": 23, 
    "Lenguajes": {"Python", "C", "C++"},
    1: 1.78,
}

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Lenguajes"]) # accediendo a una clave específica

my_dict["Edad"] = 20    # se pueden modificar los valores de las claves
print(my_dict)

my_dict["Email"] = "miemail@host.me"    # se puede agregar una nueva clave y su valor
print(my_dict)

del my_dict["Email"]
print(my_dict)

print("Padilla" in my_dict)
print("Apellido" in my_dict)    # se puede buscar, pero por clave
print(my_dict["Apellido"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Email"]

my_new_dict = dict.fromkeys(my_list) # se crea otro diccionario con claves a partir de un objeto
print(my_new_dict)                   # iterable, pero sin valores
my_new_dict = dict.fromkeys(my_dict, "valor") # se establece el mismo valor para todas las claves
print(my_new_dict)

print(list(my_new_dict))    # se convierte en una lista, pero solo las claves
print(list(my_new_dict.values()))   # se convierte en una lista, pero solo los valores
print(tuple(my_new_dict))   # se convierte en una tupla, solo las claves
print(set(my_new_dict))     # se convierte en un set, solo las claves
