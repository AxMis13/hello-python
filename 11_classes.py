# Clases en Python

class MyEmptyPerson:    # con class se define una clase, por convención los nombres se escriben con
    pass                # camel case y sin guiones bajos

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "sin alias"):  # esto es un constructor de clase, siempre debe llevar self
        self.name = name    # de esta forma se le da valor a los atributos de la clase
        self.surname = surname
        self.alias = alias
    
    def walk(self): # todas las funciones deben recibir self para poder acceder a los atributos del objeto
        print(f"¡{self.name} está caminando!")

my_person = Person("Alexa", "Padilla")  # instanciando un objeto
print(f"{my_person.name} {my_person.surname}, {my_person.alias}")  # accediendo a los atributos del objeto
my_person.walk()    # llamando a una función del objeto

my_other_person = Person("Alexa", "Padilla", "AxMis")
print(f"{my_other_person.name} {my_other_person.surname}, {my_other_person.alias}")

my_other_person.name = "Ashley" # modificando el atributo del objeto
print(f"{my_other_person.name} {my_other_person.surname}, {my_other_person.alias}")

class Car:
    def __init__(self, model, year, km):
        self.model = model
        self.year = year
        self.__km = km  # esto es un atributo privado, no se puede modificar a menos de que exista 
                        # una función para ello
    def get_km(self):   # función para obtener el atributo privado
        return self.__km
        
my_car = Car("Tesla", 2020, 75945)

print(f"Auto: {my_car.model}, año: {my_car.year}")
#print(my_car.__km) no se puede acceder a un atributo definido con dos guiones bajos al principio
print(f"Auto: {my_car.model}, año: {my_car.year}, kilometraje: {my_car.get_km()}")  # se llama a la función que permite conocer el kilometraje
