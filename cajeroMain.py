# Estructuras de datos
cuentasDebito = {}  # Diccionario para almacenar las cuentas de débito
efectivoDisponible = {20: 10,50: 10,100: 10, 200: 10, 500: 10, 1000: 10}  # Diccionario para almacenar el efectivo disponible

# Funciones
def iniciar_sesion():
    while True:
        tipo_usuario = input("0.- Salir\n"
                             "1.- Usuario\n"
                             "2.- Administrador \n"
                             "Seleccione tipo de usuario: ")

        match tipo_usuario:
            case "1":
                iniciarSesionUsuario()
            case "2":
                iniciarSesionAdmin()
            case "0":
                exit()


def iniciarSesionAdmin():
    while True:
        nip_admin = input("Bienvenido Administrador\n"
                          "Ingresa tu NIP (o '0' para volver atrás): ")
        if nip_admin == "0000":
            menuAdmin()
        elif nip_admin == "0":
            return
        else:
            mostrarError("No coincide el NIP. Intentalo de nuevo")
            while True:
                salir = input("Deseas regresar al menu anterior?\n"
                              "0.- Salir \n"
                              "1.- Reintentar")
                if(salir == 0):
                    iniciar_sesion()
                else:
                    pass

def menuAdmin():
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

def iniciarSesionUsuario():
    while True:
        cuentaUsr = input("Bienvenido Usuario\n"
                          "Ingresa tu numero de cuenta: ")

        nipUsr = input("Ingresa tu numero de NIP: ")

        if(verificarNIP(cuentaUsr,nipUsr)):
            menuUsuario(cuentaUsr)
        else:
            mostrarError("No coincide el NIP. Intentalo de nuevo")
            while True:
                salir = input("Deseas regresar al menu anterior?\n"
                              "0.- Salir \n"
                              "1.- Reintentar")
                if salir == '0':
                    return
                elif salir == '1':
                    iniciar_sesion()
                else:
                    mostrarError("Opción inválida. Por favor, elige 0 o 1.")
def menuUsuario(cuentaUsr):

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
                deposito(cuentaUsr)
            case "2":
                retiro(cuentaUsr)
            case "3":
                cambiarNIP(cuentaUsr)


def realizarDeposito(cuentaUsr):
    cantidad_deposito = int(input("Ingrese la cantidad que desea depositar: "))

    if cantidad_deposito <= 0:
        mostrarError("La cantidad ingresada no es válida.")
        return

    # Actualizar el saldo de la cuenta
    cuentasDebito[cuentaUsr]["Saldo"] += cantidad_deposito

    # Actualizar la disponibilidad de billetes
    billetes_disponibles = sorted(efectivoDisponible.keys(), reverse=True)
    billetes_a_depositar = {}

    monto_restante = cantidad_deposito
    for denominacion in billetes_disponibles:
        cantidad_billetes = monto_restante // denominacion
        if cantidad_billetes > 0 and efectivoDisponible[denominacion] >= cantidad_billetes:
            billetes_a_depositar[denominacion] = cantidad_billetes
            monto_restante -= cantidad_billetes * denominacion

    if monto_restante == 0:
        # Actualizar la disponibilidad de billetes
        for denominacion, cantidad in billetes_a_depositar.items():
            efectivoDisponible[denominacion] += cantidad
        print(f"Se ha depositado ${cantidad_deposito} en la cuenta.")
        print("Nuevo saldo:", cuentasDebito[cuentaUsr]["Saldo"])
        print("Disponibilidad de billetes actualizada:")
        print(efectivoDisponible)
    else:
        mostrarError("No es posible depositar esa cantidad con los billetes disponibles.")

def deposito(cuentaUsr):
    while True:
        print("1. Realizar depósito")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            realizarDeposito(cuentaUsr)
        elif opcion == "2":
            return
        else:
            mostrarError("Opción no válida. Por favor seleccione 1 o 2.")


def evaluaBilletes():
    for x in efectivoDisponible:
        if efectivoDisponible[x] != 0:
            return x

def retirarEfectivo(opcRet, cuentaUsr):
    saldo = cuentasDebito[cuentaUsr]["Saldo"]

    if opcRet > saldo:
        mostrarError("No tienes suficiente saldo en tu cuenta.")
        return

    billetes_disponibles = sorted(efectivoDisponible.keys(), reverse=True)
    retirados = {}

    for denominacion in billetes_disponibles:
        if opcRet >= denominacion and efectivoDisponible[denominacion] > 0:
            cantidad_a_retirar = min(opcRet // denominacion, efectivoDisponible[denominacion])
            retirados[denominacion] = cantidad_a_retirar
            opcRet -= denominacion * cantidad_a_retirar

    if opcRet == 0:
        print("Retirando billetes:")
        for denominacion, cantidad in retirados.items():
            print(f"{cantidad} billete(s) de ${denominacion}")
            efectivoDisponible[denominacion] -= cantidad

        # Actualizar el saldo de la cuenta
        cuentasDebito[cuentaUsr]["Saldo"] -= cantidad*denominacion

    else:
        mostrarError("No se puede retirar la cantidad solicitada con los billetes disponibles.")

    print("Lista de billetes disponibles después del retiro:")
    print(efectivoDisponible)
    print("Saldo actual:", cuentasDebito[cuentaUsr]["Saldo"])


def retiro(cuentaUsr):
    while True:
        print("Billetes desde $" + str(evaluaBilletes()) + " disponibles")
        print("1. Realizar retiro")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            opcRet = int(input("¿Qué cantidad deseas retirar? "))
            confirmaNIP = input("Ingresa tu NIP para validar la transacción: ")

            if verificarNIP(cuentaUsr, confirmaNIP):
                if opcRet <= 8000:
                    retirarEfectivo(opcRet,cuentaUsr)
                else:
                    print("No se admiten retiros mayores a 8000")
            else:
                mostrarError("NIP incorrecto")
        elif opcion == "2":
            return
        else:
            mostrarError("Opción no válida. Por favor selecciona 1 o 2.")


def cambiarNIP(numeroCuenta):
    if numeroCuenta in cuentasDebito:
        nuevoNIP = input("Ingresa el nuevo NIP para la cuenta " + numeroCuenta + ": ")
        cuentasDebito[numeroCuenta]['NIP'] = nuevoNIP
        print("El NIP de la cuenta " + numeroCuenta + " se ha cambiado correctamente.")
    else:
        mostrarError("La cuenta con el número " + numeroCuenta + " no existe.")

def mostrarError(mensaje):
    print("Error:", mensaje)

iniciar_sesion()
