def menu():
    print("MENÚ\n")
    print("SISTEMA DE ARRENDAMIENTO")
    print("1. Ingresar datos de las empresas arrendadoras")
    print("2. Ingresar datos de las personas arrendatarias")
    print("3. Visualizar datos de las empresas arrendadoras")
    print("4. Visualizar datos de las personas arrendatarias")
    print("5. Visualizar gráfico del monto a pagar de las personas arrendatarias")
    print("6. Salir del programa")
empresa=[]
persona=[]
class Gestion_arriendos():
    
    def __init__(self):
        self.rut_empresa = 0
        self.nombre_empresa = 0
        self.phono_empresa = 0
        self.email_empresa = 0
        self.direccion_empresa = 0
        self.rut_persona = 0
        self.primer_nombre = 0
        self.segundo_nombre = 0
        self.apellido_paterno = 0
        self.apellido_materno = 0
        self.phono_persona = 0
        self.email_persona = 0
        self.fecha_nacimiento = 0
        self.Ingreso_mensual = 0
        self.monto_a_pagar = 0

    def empresa(self):
        self.rut_empresa=input("Ingrese Rut de la empresa: ")
        self.nombre_empresa=input("Ingrese el nombre de la empresa: ")
        self.phono_empresa=input(input("Ingrese el telefono de la empresa: "))
        self.email_empresa=input("Ingrese el email de la empresa: ")
        self.dirección_empresa=input("ingrese la dirección de la empresa: ")

    def personas_arrendatarias(self):
        self.rut_persona=input("Ingrese el nombre de la persona arrendataria: ")
        self.primer_nombre=input("Ingrese el primer nombre: ")
        self.segundo_nombre=input("Ingrese el segundo nombre: ")
        self.apellido_paterno=input("Ingrese el apellido paterno: ")
        self.apellido_materno=input("Ingrese el apellido materno: ")
        self.phono_persona=input("Ingrese el telefono de la persona arrendataria: ")
        self.email_persona=input("Ingrese el email de la persona arrendataria: ")
        self.fecha_nacimiento=input("Ingrese la fecha de nacimiento: ")
        self.Ingreso_mensual=input("Ingrese el ingreso mensual: ")
        self.monto_a_pagar=input("Ingrese el monto de la pagar: ")
menu()
opc=input("Ingrese opcion que desea seleccionar: ")
print(f"cosa: {Gestion_arriendos()}")
  #  if opc == "1":
   #     empresa()
    #elif(opc == "2"):
    #    personas_arrendatarias()
    #elif(opc == "3"):

    #elif(opc == "4"):
    #elif(opc == "5"):
