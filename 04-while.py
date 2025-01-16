x=0

tem=""
while x<10:

    print(x)
    tem+=str(x)+"+"
    x=x+2

    print(tem)

print("dame 2 numeros")
a=int(input("num1: "))
b=int(input("num2: "))

contador = 0 
tem = ""  

while b > 0:
    contador += a  
    tem += str(a) + "+"  
    b -= 1  


print("{0} = {1}".format(tem,contador))

