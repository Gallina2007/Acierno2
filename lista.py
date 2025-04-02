lista=["ciao", "gallina"]
def aggiungi():
    x=input()
    lista.append(x)
def visualizza():
    for i in range(len(lista)):
        print(f"{i+1}.{lista[i]}")
visualizza()
def rimuovi():
    visualizza()
    indice=int(input())
    lista.pop(indice-1)
def conta():
    print(len(lista))
def svuota():
    lista.clear()
while True:
    scelta=int(input())
    if scelta==1:
        aggiungi()
    elif scelta==2:
        visualizza()
    elif scelta==3:
        rimuovi()
    elif scelta==4:
        conta()
    elif scelta==5:
        svuota()
    elif scelta==0:
        break

















