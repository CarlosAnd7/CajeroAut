efectivoDisponible = {20: 10,50: 10,100: 10, 200: 10, 500: 10, 1000: 10}  # Diccionario para almacenar el efectivo disponible
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

def verificarNIP(numero_cuenta, nip):
    cuenta = cuentasDebito.get(numero_cuenta)
    if cuenta and cuenta["NIP"] == nip:
        return True
    else:
        return False

def evaluaBilletes():
    for x in efectivoDisponible:
        if efectivoDisponible[x] != 0:
            return x
def realizarDeposito(cuentaUsr):
    cantidad_deposito = int(input("Ingrese la cantidad que desea depositar: "))

    if cantidad_deposito <= 0:
        print("La cantidad ingresada no es válida.")
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
        print("No es posible depositar esa cantidad con los billetes disponibles.")

def deposito(cuentaUsr):
    while True:
        print("1. Realizar depósito")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            realizarDeposito(cuentaUsr)
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor seleccione 1 o 2.")
def mostrar_error(mensaje):
    print("Error:", mensaje)

deposito("1234567890")