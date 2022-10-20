class Banco:
    def __init__(self,nombre, apellido,cedula, ciudad,numeroCuenta = 0, salario = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.ciudad = ciudad
        self.numeroCuenta = numeroCuenta
        self.salario = salario

    def addAccount(self):
        numberAccount = int(input(f"{self.nombre} Digita numero de cuenta: "))
        balance = int(input(f"{self.nombre} Digita saldo: ")) 

        self.numeroCuenta = numberAccount
        self.salario = balance
        print(f"Numero cuenta: {self.numeroCuenta}")
        print(f"salario: {self.salario}")

    def consultarSaldo (self):
        print(f"Tu consulta de saldo es : {self.salario}")

    def ingresarRetirar(self):
        bandera = int(input("retirar 1 y agregar saldo 2: "))

        if (bandera == 1):
            resta = int(input("digitar monto del retiro: ")) 
            if(resta > self.salario):
                print("no tienes suficiente dinero")
                resta = int(input("digitar monto del retiro: "))
                self.salario -= resta 
                print(f"tu saldo es: {self.salario}")
            else:
                print(f"{self.salario}")

        if (bandera == 2):
            suma = int(input("digitar monto a agregar: "))
            self.salario += suma
            print(f"tu saldo es: {self.salario}")

cuentaBanco = Banco("nicolas","betancur","cedula","ciudad")
cuentaBanco.addAccount()
cuentaBanco.ingresarRetirar()



