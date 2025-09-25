# Módulo creado como ejemplo

def sum_values(value1, value2, value3):
    print(f"{value1} + {value2} + {value3} = {value1 + value2 + value3}")

def triangle(value):
    aux = value
    for i in range(value):
        for j in range(aux):
            print("+", end="")  # end="" sirve para evitar el salto de línea con cada print
        print("")
        aux -= 1