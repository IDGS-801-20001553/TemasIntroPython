from io import open 
import math

class Cinepolis:
    def __init__(self, personas, boletos):
        self.personas = personas
        self.boletos = boletos
        self.ventas = []  
        self.archivo = "corte_ventas.txt"  

    def calcular_total(self):
        precio = 12
        total = self.boletos * precio

        if self.boletos > 5:
            total *= 0.85  
        elif 3 <= self.boletos <= 5:
            total *= 0.90  

        return total

    def insertar_venta(self, nombre, total, metodo_pago):
        if metodo_pago == "1":
            total *= 0.90
        self.ventas.append((nombre, total))

        with open(self.archivo, "a") as file:
            file.write(f"{nombre}: ${total:.2f}\n")

        return total

    def mostrar_corte(self):
        print("\n--- Corte de ventas ---")
        total_general = 0

        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    print(linea.strip())
                    _, total = linea.strip().rsplit(": $")
                    total_general += float(total)
        except FileNotFoundError:
            print("No se encontraron ventas registradas.")

        print(f"Total general de ventas: ${total_general:.2f}")


def main():

    with open("corte_ventas.txt", "w") as file:
        file.truncate(0)

    while True:
        print("\n--- Menú ---")
        print("1. Comprar ")
        print("2. Terminar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("¿cual es su nombre?: ")
            while True:
                personas = int(input("¿Cuántas personas son en total? : "))
                max_boletos = personas * 7

                boletos = int(input(f"¿Cuántos boletos desea comprar? hasta {max_boletos}: "))
                if boletos <= max_boletos:
                    break

                print(f"No se puede comprar excedes el numero total de boletos por persona 7, solo puedes comprar {max_boletos} boletos.")
                print("¿Desea cambiar el número de personas o el número de boletos?")
                print("1. Cambiar número de personas")
                print("2. Cambiar número de boletos")
                opcion_cambio = input("Seleccione una opción: ")

                if opcion_cambio == "1":
                    personas = int(input("¿Cuántas personas son en total? :  "))
                    max_boletos = personas * 7
                    if boletos <= max_boletos:
                        
                        break
                    else:
                        print(f"No puede comprar más de {max_boletos} boletos con {personas} personas. deben ser mas de {personas} ")
                        
                elif opcion_cambio == "2":
                    boletos = int(input(f"¿Cuántos boletos desea comprar? (Máximo {max_boletos}): "))
                    if boletos <= max_boletos:
                        break
                    else:
                        print(f"No puede comprar más de {max_boletos} boletos. Intente de nuevo.")
                else:
                    print("Opción inválida. Intente nuevamente.")

            cinepolis = Cinepolis(personas, boletos)
            total = cinepolis.calcular_total()

            print("Forma de pago")
            print("1. cineco")
            print("2. efectivo")
            metodo_pago = input("Seleccione una opción: ")
            total = cinepolis.insertar_venta(nombre, total, metodo_pago)

            print(f"Nombre: {nombre}")
            print(f"Total a pagar: ${total:.2f}")
            input("Presione Enter para regresar al menú principal...")
        elif opcion == "2":
            cinepolis = Cinepolis(0, 0)  
            cinepolis.mostrar_corte()
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()