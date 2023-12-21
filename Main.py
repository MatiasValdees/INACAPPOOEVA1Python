import os
from warnings import catch_warnings
from personajes import*
contador1=0
contador2=0
turno=1
P1=Personaje("Machucao")
P2=Personaje("loco")
def OpcionIncorrecta(turno):
    if turno==2:turno=1
    else: 
        turno=2
    return turno

while P1.getVida()>0 and P2.getVida()>0:
    input("presione Enter para iniciar")
    os.system("cls")
    print ("Estado de jugadores: ")
    print(f" Nombre Jugador 1: [{P1.getNombre()}] Fuerza:[{P1.getFuerza()}]  Vida :[{P1.getVida()}] Oro:[{P1.getOro()}]")
    print(f" Nombre Jugador 2: [{P2.getNombre()}] Fuerza:[{P2.getFuerza()}]  Vida :[{P2.getVida()}] Oro:[{P2.getOro()}]")
    print(f" Turno del Jugador : {turno}")
    print("Que acción desea realizar?")
    print("Opción [1]: Atacar \nOpción [2]: Comprar\nOpción [3]: Vender\nOpción [4]: Rendirse")

    opcion=input("Ingrese opción:")
            
    match opcion:
        case "1":
            if turno==1:
                P1.Attack(P2)
                contador1+=1
                
            else:
                P2.Attack(P1)
                contador2+=1
        case "2":
            from Tienda import*
            pos=1
            for i in Shop:               
                print (f"{[pos]}Nombre del Item:[{i.getNombre()}] Fuerza: [{i.getFuerza()}] Vida: [{i.getVida()}] Costo: [{i.getCost()}] ")
                pos+=1
            selec=input("Elija un Item: ")
            if len(selec)!=0:
                seleccion=int(selec)
                if turno==1:
                    if len(P1.getInventory())<6:
                        try:
                            P1.ComprarItem(Shop[seleccion - 1])
                            P1.VerInventario()
                            contador1+=1
                        except IndexError:
                            print("Elegir opción valida")
                            turno=OpcionIncorrecta(turno)
                    else:
                        print("Lo siento no puedes tener más de 6 item en el inventario")
                        turno=OpcionIncorrecta(turno)
                else:
                    if len(P2.getInventory())<6:
                        try:
                            P2.ComprarItem(Shop[seleccion -1])
                            P2.VerInventario()
                            contador2+=1
                        except IndexError:
                            print("Elegir opción valida")
                            turno=OpcionIncorrecta(turno)  
                    else:
                        print("Lo siento no puedes tener mas de 6 item en el inventario")
                        turno=OpcionIncorrecta(turno)                   
            else:
                print("Elige una opción valida")
                turno=OpcionIncorrecta(turno)
        case "3":

            if turno==1:
                if len(P1.getInventory())!=0:
                    try:
                        P1.VerInventario()
                        sel=input("Seleccione item a vender: ")
                        if len(sel)!=0:
                            sele=int(sel)                                                   
                            P1.venderItem(P1.getInventory()[sele-1])
                            contador1+=1
                        else: 
                            print("Elige una opción valida")
                            turno=OpcionIncorrecta(turno)
                    except IndexError:
                        print("Elige una opcion valida3")
                        turno=OpcionIncorrecta(turno)
                else:
                    print("No tienes item para vender")
                    turno=OpcionIncorrecta(turno)
            else:
                if len(P2.getInventory())!=0:
                    try:
                        P2.VerInventario()
                        sel=input("Seleccione item a vender: ")
                        if len(sel)!=0:
                            sele=int(sel)
                            P2.venderItem(P2.getInventory()[sele-1])
                            contador2+=1
                        else:
                            print("Elige opcion valida")
                            turno=OpcionIncorrecta(turno)
                    except IndexError:
                        print("Elige una opción valida")
                        turno=OpcionIncorrecta(turno)
                else:
                    print("No tienes item para vender")
                    turno=OpcionIncorrecta(turno)                      
        case "4":
            if turno==1:
                op=input("Estas Seguro de rendirte?\nTeclea:\n[1] - Si\n[2] - No\n")
                if op=="1":
                    Win=P2.getNombre()
                    break
                else:
                    turno=OpcionIncorrecta(turno)
            else:
                op=input("Estas Seguro de rendirte?\nTeclea:\n[1] - Si\n[2] - No\n")
                if op=="1":
                    Win=P1.getNombre()
                    break
                else:
                    turno=OpcionIncorrecta(turno)
        case _:
            print("favor ingresar una opcion valida")
            turno=OpcionIncorrecta(turno)


    if turno==1:turno=2
    else: turno=1
os.system("cls")
if P1.getVida()>P2.getVida():
    Win=P1.getNombre()
else:
    Win=P2.getNombre()
print(f"Ganador : {Win}")
print(f"Turnos del jugador 1: {contador1}\nTurnos del jugador 2: {contador2}\nTotal de Turnos en el juego {contador1+contador2}")
input()