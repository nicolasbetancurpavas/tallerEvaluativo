#Declarando una funcion tradicional
def calcular ():
    numero1 = int(input("Ingresa un número: "))
    numero2 = int(input("Ingresa un segundo número: "))
    if numero1 > numero2:
        print(f'El {numero1} es mayor que {numero2}')
    else:
        print(f'El {numero1} es menor que {numero2}')
#Llamando la funcion tradicional
calcular()


#Declarando una funcion lambda
calculando = lambda num1, num2: True if num1 > num2 else False;
#Llamando funcion lambda
print(calculando(1, 2))