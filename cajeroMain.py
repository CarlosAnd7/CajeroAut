# Estructuras de datos
cuentasDebito = {}  # Diccionario para almacenar las cuentas de débito
efectivoDisponible = {100: 10, 200: 10, 500: 10, 1000: 10}  # Diccionario para almacenar el efectivo disponible

# Funciones
def iniciar_sesion():
    while True:
        tipo_usuario = input("0.- Salir\n"
                             "1.- Usuario\n"
                             "2.- Administrador \n"
                             "Seleccione tipo de usuario: ")

        match tipo_usuario:
            case "1":
                iniciar_sesion_usuario()
            case "2":
                iniciar_sesion_administrador()
            case "0":
                exit()


def iniciar_sesion_administrador():
    while True:
        nip_admin = input("Bienvenido Administrador\n"
                          "Ingresa tu NIP (o '0' para volver atrás): ")
        if nip_admin == "0000":
            menu_administrador()
        elif nip_admin == "0":
            return
        else:
            mostrar_error("No coincide el NIP. Intentalo de nuevo")
            while True:
                salir = input("Deseas regresar al menu anterior?\n"
                              "0.- Salir \n"
                              "1.- Reintentar")
                if(salir == 0):
                    iniciar_sesion()
                else:
                    pass

def menu_administrador():
    while True:
        print("0.- Cerrar Sesión\n"
              "1.- Crear cuenta\n"
              "2.- Eliminar cuenta")

        opc_menu = input("Ingresa el índice de la operación que deseas realizar: ")

        match opc_menu:
            case "0":
                return
            case "1":
                creaCuenta()
            case "2":
                eliminarCuenta()


def creaCuenta():
    nuevoNC = input("Ingresa el nuevo numero de cuenta: ")

    nuevoNIP = input("Ingresa el NIP para la cuenta: ")

    saldo = input("Cuanto saldo tendra disponible?: ")

    nombre = input("A nombre de quien estara?")

    nuevaCuenta = {'NIP': nuevoNIP, 'Saldo': saldo, 'Nombre': nombre}

    cuentasDebito[nuevoNC] = nuevaCuenta

    print("La cuenta con el numero " + nuevoNC + " tiene los siguientes datos:")
    print("Nombre: " + cuentasDebito[nuevoNC]['Nombre'])
    print("NIP: " + cuentasDebito[nuevoNC]['NIP'])
    print("Saldo: " + cuentasDebito[nuevoNC]['Saldo'])

def eliminarCuenta():
    numeroCuentaDel = input("Ingrese el numero de cuenta a eliminar: ")
    confirmaNIP = input("Confirma tu NIP para eliminar la cuenta")

    if(confirmaNIP == "0000"):
        cuentasDebito.pop(numeroCuentaDel, "Cuenta no encontrada")
    else:
        pass

def verificarNIP(numero_cuenta, nip):
    cuenta = cuentasDebito.get(numero_cuenta)
    if cuenta and cuenta["NIP"] == nip:
        return True
    else:
        return False

def iniciar_sesion_usuario():
    while True:
        cuentaUsr = input("Bienvenido Usuario\n"
                          "Ingresa tu numero de cuenta: ")

        nipUsr = input("Ingresa tu numero de NIP: ")

        if(verificarNIP(cuentaUsr,nipUsr)):
            menu_usuario()
        else:
            mostrar_error("No coincide el NIP. Intentalo de nuevo")
            while True:
                salir = input("Deseas regresar al menu anterior?\n"
                              "0.- Salir \n"
                              "1.- Reintentar")
                if salir == '0':
                    return
                elif salir == '1':
                    iniciar_sesion()
                else:
                    print("Opción inválida. Por favor, elige 0 o 1.")
def menu_usuario():

    while True:
        opcMenuUsr= input("Bienvenido al menu de Usuario \n"
                          "0.- Salir \n"
                          "1.- Deposito \n"
                          "2.- Retiro \n"
                          "3.- Cambiar NIP \n")

        match opcMenuUsr:
            case "0":
                return
            case "1":
                deposito()
            case "2":
                retiro()
            case "3":
                cambiarNIP()



def operaciones_billetes(tipo_operacion, cantidad):
    # Aquí deberías implementar la lógica para operaciones con billetes (retirar/depositar)
    pass

def deposito():
    pass
def retiro():
    pass
def cambiarNIP():
    pass

def mostrar_error(mensaje):
    print("Error:", mensaje)

iniciar_sesion()
