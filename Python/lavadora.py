tipoLavadora = int(input("Bienvenido, digite 1 si su lavadora es pequeña y 2 si su lavadora es grande: "))
horasPrestada = int(input("Ingrese la cantidad de horas del alquiler: "))
cantidadLavadoras = int(input("Ingrese la cantidad de lavadoras que alquiló: "))

def valor_Lavadora_Por_Hora(tipoLavadora):
    if tipoLavadora == 1:
        return 4000
    else:
        return 3000
    
def precioTotalAlquiler(cantidadLavadoras, horasPrestada):

    precio_Por_Tipo_Lavadora = valor_Lavadora_Por_Hora(tipoLavadora)

    if cantidadLavadoras > 3:
        precioTotal = float(cantidadLavadoras) * float(precio_Por_Tipo_Lavadora) * float(horasPrestada)
        return precioTotal
    else:
        precioTotal = float(cantidadLavadoras) * float(precio_Por_Tipo_Lavadora) * 0.03
        return precioTotal
    
mensaje = "El costo total a pagar es: " + str(precioTotalAlquiler(cantidadLavadoras, horasPrestada))  
print(mensaje)  
