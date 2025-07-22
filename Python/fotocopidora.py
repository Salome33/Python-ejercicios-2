cantidadCopias = int(input("Bienvenido a papeleria El CALVO, ingrese la cantidad de copias que desea imprimir: "))

def determinarPrecioPorCopia(cantidadCopias):
    if cantidadCopias > 0 and cantidadCopias < 500:
        return 120
    elif cantidadCopias >= 500 and cantidadCopias < 750:
        return 100
    elif cantidadCopias >= 750 and cantidadCopias < 1000:
        return 80
    else:
        return 50
    
def calcularPrecioPorCopia(cantidadCopias):
    precioPorCopia = determinarPrecioPorCopia(cantidadCopias)
    precioTotal = cantidadCopias * precioPorCopia
    return precioTotal

precioPorCopia = determinarPrecioPorCopia(cantidadCopias)
precio = calcularPrecioPorCopia(cantidadCopias)
print("Se le cobró $" + str(precioPorCopia) + "por copia. El precio total es de $" + str(precio))