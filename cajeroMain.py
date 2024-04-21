cuentasDebito = {
    "1234567890": {
        "NIP": "1234",
        "Saldo": 5000,
        "Nombre": "Juan Perez"
    },
    "0987654321": {
        "NIP": "5678",
        "Saldo": 3000,
        "Nombre": "Maria Garcia"
    },
    "1357924680": {
        "NIP": "4321",
        "Saldo": 7000,
        "Nombre": "Pedro Rodriguez"
    }
}
efectivoDisponible = {20: 10, 50: 10, 100: 10, 200: 10, 500: 10, 1000: 10}

def iniciarSesion():
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
            mostrarError("No coincide el NIP. Inténtalo de nuevo")


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

    saldo = input("¿Cuánto saldo tendrá disponible?: ")

    nombre = input("¿A nombre de quién estará?")

    nuevaCuenta = {'NIP': nuevoNIP, 'Saldo': float(saldo), 'Nombre': nombre}

    cuentasDebito[nuevoNC] = nuevaCuenta

    print("La cuenta con el número " + nuevoNC + " tiene los siguientes datos:")
    print("Nombre: " + cuentasDebito[nuevoNC]['Nombre'])
    print("NIP: " + cuentasDebito[nuevoNC]['NIP'])
    print("Saldo: " + str(cuentasDebito[nuevoNC]['Saldo']))


def eliminarCuenta():
    numeroCuentaDel = input("Ingrese el número de cuenta a eliminar: ")
    confirmaNIP = input("Confirma tu NIP para eliminar la cuenta")

    if confirmaNIP == "0000":
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
                          "Ingresa tu numero de cuenta (o '0' para salir): ")

        if cuentaUsr == "0":
            return
        else:
            nipUsr = input("Ingresa tu numero de NIP: ")

            if verificarNIP(cuentaUsr, nipUsr):
                menuUsuario(cuentaUsr)
            else:
                mostrarError("No coincide el NIP. Inténtalo de nuevo")



def menuUsuario(cuentaUsr):

    while True:
        opcMenuUsr = input("Bienvenido al menú de Usuario \n"
                           "0.- Salir \n"
                           "1.- Depósito \n"
                           "2.- Retiro \n"
                           "3.- Cambiar NIP \n")

        match opcMenuUsr:
            case "0":
                return
            case "1":
                realizarOperacion(cuentaUsr, "deposito")
            case "2":
                realizarOperacion(cuentaUsr, "retiro")
            case "3":
                cambiarNIP(cuentaUsr)


def realizarOperacion(cuentaUsr, tipo_operacion):
    nipOp = input("Ingresa tu NIP para validar la operacion: ")
    if verificarNIP(cuentaUsr, nipOp):
        if tipo_operacion == "retiro":
            monto_operacion = int(input("Ingrese la cantidad que desea retirar: "))
            if(monto_operacion > 8000):
                mostrarError("No es posible hacer retiros mayores a 8000 en el cajero automatico")
                return
            else:
                saldo = cuentasDebito[cuentaUsr]["Saldo"]
                if monto_operacion > saldo:
                    mostrarError("No tienes suficiente saldo en tu cuenta.")
                    return
                else:
                    cuentasDebito[cuentaUsr]["Saldo"] -= monto_operacion
        elif tipo_operacion == "deposito":
            monto_operacion = int(input("Ingrese la cantidad que desea depositar: "))
            cuentasDebito[cuentaUsr]["Saldo"] += monto_operacion
        else:
            mostrarError("Tipo de operación no válido.")
            return


        billetes_disponibles = sorted(efectivoDisponible.keys(), reverse=True)
        billetes_a_depositar_o_retirar = {}

        monto_restante = monto_operacion
        for denominacion in billetes_disponibles:
            if tipo_operacion == "retiro":
                if monto_restante >= denominacion and efectivoDisponible[denominacion] > 0:
                    cantidad_billetes = min(monto_restante // denominacion, efectivoDisponible[denominacion])
                    billetes_a_depositar_o_retirar[denominacion] = cantidad_billetes
                    monto_restante -= cantidad_billetes * denominacion
                    efectivoDisponible[denominacion] -= cantidad_billetes
            else:
                cantidad_billetes = monto_restante // denominacion
                if cantidad_billetes > 0:
                    billetes_a_depositar_o_retirar[denominacion] = cantidad_billetes
                    monto_restante -= denominacion * cantidad_billetes
                    efectivoDisponible[denominacion] += cantidad_billetes

        if monto_restante == 0:
            if tipo_operacion == "retiro":
                print("Operación exitosa. Retirando billetes:")
                for denominacion, cantidad in billetes_a_depositar_o_retirar.items():
                    print(f"{cantidad} billete(s) de ${denominacion}")
            else:
                print(f"Operación exitosa. Se ha depositado ${monto_operacion} en la cuenta.")

            print("Nuevo saldo:", cuentasDebito[cuentaUsr]["Saldo"])
            print("Disponibilidad de billetes actualizada:")
            print(efectivoDisponible)
        else:
            mostrarError("No es posible realizar la operación con los billetes disponibles.")
    else:
        mostrarError("NIP incorrecto")

def cambiarNIP(numeroCuenta):
    if numeroCuenta in cuentasDebito:
        nipActual = input("Ingresa tu NIP actual: ")
        if verificarNIP(numeroCuenta, nipActual):
            nuevoNIP = input("Ingresa el nuevo NIP para la cuenta " + numeroCuenta + ": ")
            cuentasDebito[numeroCuenta]['NIP'] = nuevoNIP
            print("El NIP de la cuenta " + numeroCuenta + " se ha cambiado correctamente.")
        else:
            mostrarError("NIP incorrecto")

    else:
        mostrarError("La cuenta con el número " + numeroCuenta + " no existe.")


def mostrarError(mensaje):
    print("Error:", mensaje)


iniciarSesion()
