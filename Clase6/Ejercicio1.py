class Empleado():
    
    def __init__(self):
        self.nombre = []
        self.__salario = []
        self.fechaInicio = []
        self.aumentoSalario=[]

    def __str__(self):
        return print('{} su fecha de ingreso es {}, su salario {} y el aumento de su salario sera '.format(self.nombre, self.fechaInicio, self.salario, self.aumentoSalario))
    
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
        self.aumentoSalario= salario*antiguedad

    
       

class Institucion():
    
    empleados = []
    
    def __init__(self, empleados=[]):
        
        Institucion.empleados = empleados

    def agregarEmpleado(self, e):
        Institucion.empleados.append(e)
    
    def mostrarEmpleados(self):
        for e in Institucion.empleados:
            print(e)
            print('Calculo de sueldo: ', empleado.calcularAumento)


empleado = Empleado('Pedro','1000', (10,11,2006))
institucion= Institucion()
institucion.agregarEmpleado(empleado)