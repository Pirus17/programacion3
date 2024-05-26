class Contacto():
    
    cantidadContactos=0
    
    def __init__(self):
        self.nombre = []
        self.telefono = []
        self.email = []
        
    def cargar(self):
        print("\033[H\033[J")          # Limpiamos la pantalla
        print("Cargar de Contactos:")
        print()

        nombre = input('Ingrese el Nombre: ')
        self.nombre.append(nombre)
          
        telefono = input('Ingrese el Telefono: ')
        self.telefono.append(telefono)
            
        email = input('Ingrese el Email: ')
        self.email.append(email)
            
        self.cantidadContactos+=1
         


    def buscarContacto(self):
        print("\033[H\033[J")          # Limpiamos la pantalla
        print("Buscar de Contactos:")
        print()
        contacto= input("Ingrese el nombre del contacto:")
        print()
        encontrado= False
        for i in range (self.cantidadContactos):
            if contacto == self.nombre[i]:
                encontrado= True
                break
        if encontrado:
            print(self.nombre[i],self.telefono[i],self.email[i])
        else:
            print("No existe el contacto")
        print("-"*35)
        print()
        salir=input("Presione cualquier tecla para salir")

    def mostrarContacto(self):
        print("\033[H\033[J")          # Limpiamos la pantalla
        print("Listado de Contactos:")
        print()
        for i in range(self.cantidadContactos):
            print(self.nombre[i],self.telefono[i],self.email[i])
        print("-"*35)
        print()
        salir=input("Presione cualquier tecla para salir")

    def modificarContacto(self):
        print("\033[H\033[J")          # Limpiamos la pantalla
        print("Modificar Contacto:")
        print()
        contacto= input("Ingrese el nombre del contacto:")
        print()
        for i in range(self.cantidadContactos):
            if contacto == self.nombre[i]:
                del self.nombre[i]
                self.cargar()
                self.cantidadContactos-=1
    
    def finalizar(self):
        print("Programa finalizado!")
        print("-"*35)

    def menu(self):
        opcion=0
        while opcion!=5:
            print("\033[H\033[J")          # Limpiamos la pantalla
            print("1- Cargar Contacto")
            print("2- Mostrar Contactos")
            print("3- Buscar Contactos")
            print("4- Editar Contacto")
            print("5- Cerrar Contacto")
            print()
            opcion=int(input("Ingrese su opcion: "))
            print("-"*35)
            if opcion==1: self.cargar()
            elif opcion==2: self.mostrarContacto()
            elif opcion==3: self.buscarContacto()
            elif opcion==4: self.modificarContacto()
            else: self.finalizar()        

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------

print("\033[H\033[J")          # Limpiamos la pantalla
Agenda = Contacto()
Agenda.menu()