# Conjuntos o sets

my_set = set()
my_other_set = {} # inicialmente es un diccionario

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Alexa", "Padilla", 23}
print(type(my_other_set))

print(len(my_other_set))

#print(my_other_set[0]) | los sets no tienen índices, son conjuntos desordenados
my_other_set.add("Morado")  # añade el elemento al conjunto
print(my_other_set)

my_other_set.add("Morado")
print(my_other_set) # no se admiten elementos repetidos

print("Morado" in my_other_set)
print("morado" in my_other_set)

my_other_set.remove("Morado")   # la misma función que en las listas
print(my_other_set)

my_other_set.clear()        # la misma función de limpiar que en una lista
print(len(my_other_set))

del my_other_set    # elimina definitivamente el objeto

my_set = {"Alexa", "Padilla", 23}
my_list = list(my_set)  # es arriesgado ya que los set no tienen orden, por lo que la lista se 
print(my_list)          # orden de manera aleatoria

print(my_list[0])

my_other_set = {"C", "C++", "Python"}

my_new_set = my_set.union(my_other_set) # une dos conjuntos
print(my_new_set)

print(my_new_set.difference(my_set))    # la diferencia del conjuto que se pasa como parámetro con
                                        # el otro conjunto