import random

inventario = []
capacidad_maxima_por_zona = {'A': 50, 'B': 50, 'C': 50, 'D': 50}
inventario_por_zona = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

def generar_id():
    return random.randint(1, 100)
option = 100
while (option !=10):
    print("\nBienvenido al sistema de administración de inventario de la tienda de cómics")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto por nombre")
    print("4. Modificar unidades compradas")
    print("5. Eliminar producto")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        nombre = input("Nombre del producto: ")
        while True:
            precio_input = input("Precio unitario del producto: ")
            if precio_input.replace('.', '', 1).isdigit():
                precio = float(precio_input)
                break
            else:
                print("Por favor, ingrese un precio válido (solo números).")
        
        ubicacion = input("Ubicación en la tienda (A, B, C o D): ").upper()
        while ubicacion not in ['A', 'B', 'C', 'D']:
            print("Ubicación no válida. Por favor, ingrese una ubicación válida (A, B, C o D).")
            ubicacion = input("Ubicación en la tienda (A, B, C o D): ").upper()

        total_unidades_zona = sum(producto['unidades'] for producto in inventario if producto['ubicacion'] == ubicacion)

        if total_unidades_zona >= capacidad_maxima_por_zona[ubicacion]:
            print(f"Error: La zona {ubicacion} ha alcanzado su capacidad máxima de 50 productos.")
            continue

        nuevas_unidades = int(input(f"Ingrese el número de unidades de {nombre} a agregar (máximo {capacidad_maxima_por_zona[ubicacion] - total_unidades_zona}): "))
        if total_unidades_zona + nuevas_unidades > capacidad_maxima_por_zona[ubicacion]:
            print(f"Error: No se pueden agregar más de {capacidad_maxima_por_zona[ubicacion] - total_unidades_zona} unidades en la zona {ubicacion}.")
            continue

        descripcion = input("Descripción del producto: ")
        casa = input("Casa a la que pertenece el producto (Marvel, DC, etc): ")
        referencia = input("Referencia (código alfanumérico): ")
        pais = input("País de origen del producto: ")

        while True:
            garantia = input("Producto con garantía extendida (S/N): ").upper()
            if garantia in ['S', 'N']:
                break
            else:
                print("Por favor, ingrese una respuesta válida (S para sí, N para no).")

        producto = {
            'id': generar_id(),
            'nombre': nombre,
            'precio': precio,
            'ubicacion': ubicacion,
            'descripcion': descripcion,
            'casa': casa,
            'referencia': referencia,
            'pais': pais,
            'unidades': nuevas_unidades,
            'garantia': garantia
        }

        inventario.append(producto)
        inventario_por_zona[ubicacion] += nuevas_unidades
        print("Producto registrado con éxito. ID del producto:", producto['id'])
    
    elif opcion == '2':
        if not inventario:
            print("El inventario está vacío.")
        else:
            for producto in inventario:
                print("ID:", producto['id'])
                print("Nombre:", producto['nombre'])
                print("Precio:", producto['precio'])
                print("Descripción:", producto['descripcion'])
                print("Unidades:", producto['unidades'])
                print("Garantía:", producto['garantia'])
                print()
    
    elif opcion == '3':
        nombre = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for producto in inventario:
            if producto['nombre'].lower() == nombre.lower():
                print("ID:", producto['id'])
                print("Nombre:", producto['nombre'])
                print("Precio:", producto['precio'])
                print("Descripción:", producto['descripcion'])
                print("Unidades:", producto['unidades'])
                print("Garantía:", producto['garantia'])
                encontrado = True
        if not encontrado:
            print("Producto no encontrado.")
    
    elif opcion == '4':
        nombre = input("Ingrese el nombre del producto a modificar: ")
        nuevas_unidades = int(input("Ingrese el nuevo número de unidades compradas: "))
        for producto in inventario:
            if producto['nombre'].lower() == nombre.lower():
                inventario_por_zona[producto['ubicacion']] -= producto['unidades']
                producto['unidades'] = nuevas_unidades
                inventario_por_zona[producto['ubicacion']] += nuevas_unidades
                print("Unidades modificadas con éxito.")
                break
        else:
            print("Producto no encontrado.")
    
    elif opcion == '5':
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        for producto in inventario:
            if producto['nombre'].lower() == nombre.lower():
                inventario_por_zona[producto['ubicacion']] -= producto['unidades']
                inventario.remove(producto)
                print("Producto eliminado del inventario.")
                break
        else:
            print("Producto no encontrado.")
    
    elif opcion == '6':
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")