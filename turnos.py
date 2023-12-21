import os
turno=1
while True:
    os.system("cls")
    print (f"Estas en el turno {turno}")
    input()
    if turno==1:
        turno=2
    else:
        turno=1
