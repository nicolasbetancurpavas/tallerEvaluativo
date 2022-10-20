from tkinter import N


i = 0
opcion = 0

ciclistas = []
tiempos = []
while opcion != 2:
    opcion = int(input("Si desea agregar un ciclista digite 1, de lo contrario digite 2: "))
    if(opcion == 1):
        ciclista = {}
        ciclista['nombre'] = input("Digite nombre de ciclista: ")
        ciclista['edad'] = input("Digite edad de ciclista: ")
        ciclista['pais'] = input("Digite pais de ciclista: ")
        ciclista['equipo'] = input("Digite Equipo de ciclista: ")
        tiempos.append(int(input("Digite tiempo de ciclista(minutos): ")))
        ciclistas.insert(i, ciclista)
        i = i + 1
    elif(opcion == 2):
        print("")
    else:
        print("Digite una opcion valida")

def menorTiempo(tiempos):
    menor = tiempos[0]
    for n in tiempos:
        if n < menor:
            menor = n
    return menor

print(menorTiempo(tiempos))