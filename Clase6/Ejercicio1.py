class Empleado():
    
    def __init__(self):
        self.nombre = []
        self.__salario = []
        self.fechaInicio = []
        self.aumentoSalario=0

    def __str__(self):
        return '{} su fecha de ingreso es {}, su salario {} y el aumento de su salario sera {}'.format(self.nombre, self.fechaInicio, self.salario, self.aumentoSalario)
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self,salario):
        self.__salario=salario
    
    
    
    def cargarEmpleado(self, nombre, salario,fechaInicio):
        self.nombre= nombre
        self.salario=salario
        self.fechaInicio=fechaInicio
        antiguedad= 2024-self.fechaInicio[2]
        self.aumentoSalario= int(salario)*antiguedad

    
       

class Institucion():
    
    empleados = []
    
    def __init__(self, empleados=[]):
        
        Institucion.empleados = empleados

    def agregarEmpleado(self, e):
        Institucion.empleados.append(e)
    
    def mostrarEmpleados(self):
        for empleado in Institucion.empleados:
            print(empleado)
            


empleado = Empleado()
empleado.cargarEmpleado('Pedro','1000', (10,11,2006))
institucion= Institucion()
institucion.agregarEmpleado(empleado)
institucion.mostrarEmpleados()