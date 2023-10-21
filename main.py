empleados = []

def agregar_empleado(id_empleado, nombre, apellido, cargo, area, salario):
    empleado = {
        'id': id_empleado,
        'nombre': nombre,
        'apellido': apellido,
        'cargo': cargo,
        'area': area,
        'salario': salario
    }
    empleados.append(empleado)

def imprimir_colilla(empleado):
    print(f"Colilla de Pago")
    print(f"Nombre: {empleado['nombre']} {empleado['apellido']}")
    print(f"Cargo: {empleado['cargo']}")
    print(f"Área: {empleado['area']}")
    print(f"Salario: {empleado['salario']}")

def calcular_salario_neto(id_empleado):
    smlv = 1160000
    for empleado in empleados:
        if empleado['id'] == id_empleado:
            salario = empleado['salario']
            if salario <= (2 * smlv):
                salario_neto = salario + 136454
            else:
                salario_neto = salario
            return salario_neto
    return None

def listar_empleados():
    for empleado in empleados:
        imprimir_colilla(empleado)

def buscar_por_empleado(id_empleado):
    for empleado in empleados:
        if empleado['id'] == id_empleado:
            imprimir_colilla(empleado)
            return
    print("Empleado no encontrado")

def visualizar_todos():
    for empleado in empleados:
        imprimir_colilla(empleado)

while True:
    print("Menú:")
    print("1. Registrarse")
    print("2. Listar Empleados")
    print("3. Calcular Salario Neto")
    print("4. Imprimir Colilla de Pago")
    print("5. Buscar por empleado")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_empleado = input("Ingrese su ID: ")
        nombre = input("Nombre de usuario: ")
        apellido = input("Apellido: ")
        cargo = input("Cargo: ")
        area = input("Area: ")
        salario = int(input("Salario: "))
        agregar_empleado(id_empleado, nombre, apellido, cargo, area, salario)
        print("Registro exitoso")

    elif opcion == "2":
        listar_empleados()

    elif opcion == "3":
        id_empleado = input("Ingrese el ID del empleado para calcular el salario neto: ")
        salario_neto = calcular_salario_neto(id_empleado)
        if salario_neto is not None:
            print(f"El salario neto es: {salario_neto}")
        else:
            print("Empleado no encontrado")

    elif opcion == "4":
        id_empleado = input("Ingrese su ID: ")
        buscar_por_empleado(id_empleado)

    elif opcion == "5":
        id_empleado = input("Ingrese el ID del empleado: ")
        buscar_por_empleado(id_empleado)

    elif opcion == "6":
        break

