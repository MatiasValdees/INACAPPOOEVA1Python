class Item:
    def __init__(self,nombre:str,vida:int,fuerza:int,coste:int):
        self.__nombre=nombre
        self.__vida=vida
        self.__fuerza=fuerza
        self.__coste=coste

    def getNombre(self):
        return self.__nombre
    def getVida(self):
        return self.__vida
    def getFuerza(self):
        return self.__fuerza
    def getCost(self):
        return self.__coste