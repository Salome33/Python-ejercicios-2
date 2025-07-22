numero = int(input("ingrese un número: "))

def averiguar_numero_postivo_o_negativo(numero):

    if numero >= 0:
        return "Su número es positivo"
    else:
        return "Su número es negativo"

print(averiguar_numero_postivo_o_negativo(numero))       
