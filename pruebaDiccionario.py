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
def billetes(cuentaUsr, cantidad, tipo_operacion):
    if cantidad <= 0:
        mostrarError("La cantidad ingresada no es válida.")
        return

    saldo = cuentasDebito[cuentaUsr]["Saldo"]

    if tipo_operacion == "retiro" and cantidad > saldo:
        mostrarError("No tienes suficiente saldo en tu cuenta.")
        return

    billetes_disponibles = sorted(efectivoDisponible.keys(), reverse=True)
    operacion_exitosa = False
    monto_restante = cantidad

    if tipo_operacion == "retiro":
        operacion_exitosa = True
        retirados = {}
    else:
        billetes_a_depositar = {}

    for denominacion in billetes_disponibles:
        if tipo_operacion == "retiro":
            if cantidad >= denominacion and efectivoDisponible[denominacion] > 0:
                cantidad_a_retirar = min(cantidad // denominacion, efectivoDisponible[denominacion])
                retirados[denominacion] = cantidad_a_retirar
                cantidad -= denominacion * cantidad_a_retirar
                efectivoDisponible[denominacion] -= cantidad_a_retirar
                saldo -= denominacion * cantidad_a_retirar
        else:  # Depósito
            cantidad_billetes = monto_restante // denominacion
            if cantidad_billetes > 0:
                billetes_a_depositar[denominacion] = cantidad_billetes
                monto_restante -= denominacion * cantidad_billetes
                efectivoDisponible[denominacion] += cantidad_billetes
                saldo += denominacion * cantidad_billetes

    if tipo_operacion == "retiro":
        if cantidad == 0:
            print("Operación exitosa. Retirando billetes:")
            for denominacion, cantidad in retirados.items():
                print(f"{cantidad} billete(s) de ${denominacion}")
            cuentasDebito[cuentaUsr]["Saldo"] = saldo
            operacion_exitosa = True
        else:
            mostrarError("No se puede retirar la cantidad solicitada con los billetes disponibles.")
    else:  # Depósito
        if monto_restante == 0:
            print("Operación exitosa. Se ha depositado la cantidad en la cuenta.")
            cuentasDebito[cuentaUsr]["Saldo"] = saldo
        else:
            mostrarError("No es posible depositar esa cantidad con los billetes disponibles.")

    print("Lista de billetes disponibles:")
    print(efectivoDisponible)
    print("Saldo actual:", cuentasDebito[cuentaUsr]["Saldo"])

def mostrarError(mensaje):
    print("Error:", mensaje)

# Ejemplo de uso:
billetes("1234567890", 1000, "retiro")
billetes("1234567890", 900, "deposito")
