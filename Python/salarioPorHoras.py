cantidadHoras: int 
precioPorHora: float
total_a_Pagar: float
nombreCliente: str

def calcular_Precio_Por_Hora(cantidadHoras, precioPorHora):
    if cantidadHoras > 1 & cantidadHoras <= 10:
        return 30000
    else:
        return 33000  

nombre: list = input()       