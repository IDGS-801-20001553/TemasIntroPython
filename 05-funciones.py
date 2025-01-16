import os



def funcion1():

    os.system("cls")
    num1=int(input("numero1: "))
    num2=int(input("numero2: "))
    sum=num1+num2
    print("resultado: ",sum)

    

def funcion2():
    os.system("cls")
    num1=int(input("numero1: "))
    num2=int(input("numero2: "))
    res=num1-num2
    print("resultado: ", res)

def funcion3():
    os.system("cls")
    num1=int(input("numero1: "))
    num2=int(input("numero2: "))
    mul=num1*num2
    print("resultado: ", mul)

def funcion4():
    os.system("cls")
    num1=int(input("numero1: "))
    num2=int(input("numero2: "))
    div=num1/num2
    print("resultado: ",div)


def run():
        funcion1()
        funcion2()
        funcion3()
        funcion4()


def run():
     os.system("cls")
     print("1. suma")
     print("2. resta")
     print("3. multiplicación")
     print("4. divición")
     print("5. salir")


     op=int(input("opcion: "))
     while op<5:
            
            op=int(input("opcion: "))
            if op==1:
                funcion1()
            if op==2:
                funcion2()
            if op==3:
                funcion()
            if op==4:
                funcion4()
            if op==5:
                break


if __name__ == "__main__":
    run()
