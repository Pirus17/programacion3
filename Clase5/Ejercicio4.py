class Cliente():
    
    cantidadClientes=0 
    
    def __init__(self):
        self.nombre = []
        self.cuenta = []
        self.montoTotal = []
        
    def cargar(self):
        print("\033[H\033[J")          # Limpiamos la pantalla
        print("Cargar de Contactos:")
        print()

        cuenta = input('Ingrese el numero de cuenta: ')
        self.cuenta.append(cuenta)
        
        nombre = input('Ingrese el Nombre: ')
        self.nombre.append(nombre)

        self.montoTotal.append(0)
            
        self.cantidadClientes+=1
         
    def verSaldo(self):
        print("\033[H\033[J")          # Limpiamos la pantalla
        print("Saldo del Cliente:")
        print()
        cuenta= input("Ingrese el numero de cuenta o nombre:")
        print()

        encontrado= False
        for i in range (self.cantidadClientes):
            if cuenta == self.cuenta[i] or cuenta == self.nombre[i]:
                encontrado= True
                break
        if encontrado:
            print("Su saldo es: ", self.montoTotal[i])
        else:
            print("No existe el Cliente")
        print("-"*35)
        print()
        salir=input("Presione cualquier tecla para salir")

    def verDatos(self):
        print("\033[H\033[J")          # Limpiamos la pantalla
        print("Datos del Clientes:")
        print()
        cuenta= input("Ingrese el numero de cuenta o nombre:")
        print()
        encontrado= False
        for i in range (self.cantidadClientes):
            if cuenta == self.cuenta[i] or cuenta == self.nombre[i]:
                encontrado= True
                break
        if encontrado:
            print(f"Numero de cuenta: {self.cuenta[i]}, Nombre:  {self.nombre[i]}, Saldo: {self.montoTotal[i]}")
        else:
            print("No existe el Cliente")
        print("-"*35)
        print()
        salir=input("Presione cualquier tecla para salir")

    
    def extraccion(self):
        print("\033[H\033[J")          # Limpiamos la pantalla
        print("Extracion")
        print()
        cuenta= input("Ingrese el numero de cuenta o nombre:")
        print()
        encontrado= False
        for i in range (self.cantidadClientes):
            if cuenta == self.cuenta[i] or cuenta == self.nombre[i]:
                encontrado= True
                break
        if encontrado:
            if self.montoTotal[i]>0:
                extracionDinero = int(input("Ingrese el monto que desea extraer: "))
                if extracionDinero <= self.montoTotal[i]:
                    self.montoTotal[i]-=extracionDinero
                    print("Extraccion Exitosa")
                    print("-"*35)
                    print()
                else:
                    print("No tiene saldo suficiente")
                    print("-"*35)
                    print()

            else:
                print("No tiene saldo suficiente")
                print("-"*35)
                print()
        else:
            print("No existe el Cliente")
        print("-"*35)
        print()
        salir=input("Presione cualquier tecla para salir")

    def deposito(self):
        print("\033[H\033[J")          # Limpiamos la pantalla
        print("Deposito")
        print()
        cuenta= input("Ingrese el numero de cuenta o nombre:")
        print()
        encontrado= False
        for i in range (self.cantidadClientes):
            if cuenta == self.cuenta[i] or cuenta == self.nombre[i]:
                encontrado= True
                break
        if encontrado:
            depositoDinero=int(input("Ingrese el monto que desea Depositar: "))
            self.montoTotal[i]+=depositoDinero
            print("Deposito Exitoso")
            print("-"*35)
            print()  
        else:
            print("No existe el Cliente")
        print("-"*35)
        print()
        salir=input("Presione cualquier tecla para salir")

    def menu(self):
        opcion=0
        while opcion!=6:
            print("\033[H\033[J")          # Limpiamos la pantalla
            print("1- Cargar Cliente")
            print("2- Ver Saldo")
            print("3- Ver Datos de la Cuenta")
            print("4- Realizar Extracciones")
            print("5- Realizar Depositos")
            print("6- Cerrar Cuenta")
            print()
            opcion=int(input("Ingrese su opcion: "))
            print("-"*35)
            if opcion==1: self.cargar()
            elif opcion==2: self.verSaldo()
            elif opcion==3: self.verDatos()
            elif opcion==4: self.extraccion()
            elif opcion==5: self.deposito()
            else: self.finalizar()        

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------

print("\033[H\033[J")          # Limpiamos la pantalla
Banco = Cliente()
Banco.menu()