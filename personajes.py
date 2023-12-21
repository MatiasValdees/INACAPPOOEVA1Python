from Tienda import *


class Personaje:

    def __init__(self,nombre):
        self.__nombre=nombre
        self.__vida=100
        self.__fuerza=100
        self.__oro=1000
        self.__inventario=[]

    def getNombre(self):
        return self.__nombre
    
    def getVida(self):
        return int(self.__vida)

    def getFuerza(self):
        return self.__fuerza

    def getOro(self):
        return self.__oro

    def getInventory(self):
        return self.__inventario

    def setVida(self,vida):
        self.__vida-=vida
        return self.__vida


    def Attack(self,Objetivo):
        valorGolpe=int(self.__fuerza/15+10)
        Objetivo.setVida(valorGolpe)
        print(f"Objetivo: {Objetivo.getNombre()}\nDaño Causado: {(valorGolpe)}\nVida Restante: {Objetivo.getVida()} ")

    def ComprarItem(self,itemComprado):
        self.itemComprado=itemComprado
        if self.__oro>=self.itemComprado.getCost():    
            self.__oro-=self.itemComprado.getCost()
            self.__vida+=self.itemComprado.getVida()
            self.__fuerza+=self.itemComprado.getFuerza()
            self.__inventario.append(itemComprado)

        else:
            print(f"Lo siento no tienes dinero suficiente, tu saldo es: {self.getOro()}")
            

    def VerInventario(self):
        inve=[]
        pus=1
        for i in self.getInventory():
            inve.append(i)
            print(f"{[pus]} Nombre del item: {i.getNombre()}")    
            pus+=1        
        

    def venderItem(self,itemVendido):
         self.__oro+=int(itemVendido.getCost()/2)
         self.__vida-=(itemVendido.getVida())
         self.__fuerza-=(itemVendido.getFuerza())
         self.__inventario.remove(itemVendido)

