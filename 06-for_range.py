

range(20) # 0,2,...19

x=range(1,20)
x=range(1,20,2)

for i in range(20):
   print(i)

# usando un ciclo for pedir un numero y que me imprima la tabla de multiplicar y que imprima del 1 al 10 

num=int(input("dame un numero: "))


for i in range(1,11):
    print("{0} x {1} = {2}".format(num, i, num * i))



