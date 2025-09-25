# Manejo de errores en Python

number_one = 13
number_two = 7

# try-except
try:    # dentro del bloque try va el código propenso a errores
    print(number_one + number_two)
    print("No se ha producido ningún error")
except: # este bloque se ejecuta si en el bloque try surge un error
    print("¡Se produjo un error!")

number_two = "7"
try:
    print(number_one + number_two)  # esto genera un error
    print("No se ha producido ningún error")
except:
    print("¡Se produjo un error!")

# try-except-else
try:
    print(number_one + number_two)
    print("No se ha producido ningún error")
except:
    print("¡Se produjo un error!")
else:   # esto es opcional   
    # esto se ejecuta si en el bloque try no ocurre ningún error
    print("La ejecución continua sin errores")

# try-except-else-finally
try:
    print(number_one + number_two)
    print("No se ha producido ningún error")
except:
    print("¡Se produjo un error!")
else:   # esto se ejecuta si en el bloque try no ocurre ningún error
    print("La ejecución continua sin errores")
finally:    # esto es opcional    
    # esto se ejecuta siempre, haya o no algún error en el bloque try
    print("El programa continua")

# excepciones por tipo
try:
    print(number_one + number_two)  # esto genera un error
    print("No se ha producido ningún error")
except ValueError:  # se ejecuta sólo si ocurre un ValueError en el try
    print("¡Se produjo un ValueError!")
except TypeError:   # se ejecuta sólo si ocurre un TypeError en el try
    print("¡Se produjo un TypeError!")
# de esta forma se puede continuar con código específico dependiendo del error

# capturar la información de la excepción
try:
    print(number_one + number_two)  # esto genera un error
    print("No se ha producido ningún error")
except ValueError as error:  # la información del error se guarda en la variable error
    print("¡Se produjo un error!")
    print(error)
except Exception as error:  # esto es una excepción genérica, Exception captura cualquier error
    print(error)
finally:
    print("El programa continua...")
