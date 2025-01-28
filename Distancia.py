from io import open 
import math
# Distancia ente dos puntos 

class Distancia:
    x1=0
    x2=0
    y1=0
    y2=0

    operacion=0

    #declaracion del constructor 
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    #declaracion de metodos de la clase

    def DistanciaTotal(self):

        operacion = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        return operacion


def main():
    x1 = int(input("Ingrese la primera coordenada x1: "))
    y1 = int(input("Ingrese la segunda coordenada y1: "))
    x2 = int(input("Ingrese la tercera coordenada x2: "))
    y2 = int(input("Ingrese la cuarta coordenada y2: "))
    #objeto de mi clase distancia
    obj = Distancia(x1, y1, x2, y2)

    #resultado
    resultado=obj.DistanciaTotal()
    print(f"La distancia entre los dos puntos es: {resultado}")

if __name__ == "__main__":
    main()