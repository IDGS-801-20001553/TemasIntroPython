class OperasBas:

    #public 
    num1=0
    #private
    num2=0
    #protected
    res=0
    #declaracion del constructor 
    def __init__(self,num1,_num2):
        self.num1=num1
        self.num2=_num2
    
    #declaracion de metodos de la clase

    def suma(self):
        self.res=self.num1+self.num2
        print("la suma es: {}".format(self.res))
    
    def resta(self):
        self.res=self.num1-self.num2
        print("la resta es: {}".format(self.res))

def main():
    obj=OperasBas(3,4)
    obj.suma

if __name__ == "__main__":
    main()

#distancia entre dos puntos 