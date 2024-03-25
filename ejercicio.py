inventarios = []

print("***********Menu salpicon***********")

while True:
    print("***********************************")
    print("1.- Ingresa la fruta")
    print("2.- Valor total Salpicon") 
    print("3.- Cual es la fruta mas barata")
    print("4.- Cancelar")
    print("***********************************")
    
    option = input("Dijita una opcion: ")

    if option == "1":
        inventario = {}
        inventario["id"] = input("Dijita el ID: ")
        inventario["nombre"] = input("Dijita el Nombre de la fruta: ")

        while True:
            precio_input = input("Dijita el precio de la fruta: ")
            if precio_input.isdigit() or (precio_input.count('.') == 1 and precio_input.replace('.', '').isdigit()):
                inventario["precio"] = float(precio_input) if '.' in precio_input else int(precio_input)
                break
            else:
                print("Error: El precio debe ser un número.")

        while True:
            cantidad_input = input("Dijita la cantidad de frutas: ")
            if cantidad_input.isdigit():
                inventario["cantidad"] = int(cantidad_input)
                break
            else:
                print("Error: La cantidad debe ser un número entero.")

        inventarios.append(inventario)

    elif option == "2":
        if inventarios:
            inventarios_ordenados = sorted(inventarios, key=lambda x: x["precio"], reverse=True)
            total_salpicon = sum(fruta["precio"] * fruta["cantidad"] for fruta in inventarios_ordenados)
            print("Frutas de mayor a menor por precio:")
            print("***********************************")
            for fruta in inventarios_ordenados:
                print(f"{fruta['nombre']}: ${fruta['precio']}")    
            print(f"\nTotal del Salpicón: ${total_salpicon}")
        else:
            print("No hay frutas en el inventario.")

    elif option == "3":
        if inventarios:
            fruta_mas_barata = min(inventarios, key=lambda x: x["precio"])
            print(f"La fruta más barata es: {fruta_mas_barata['nombre']} con un precio de ${fruta_mas_barata['precio']}")
        else:
            print("No hay frutas en el inventario.")

    elif option == "4":
        print("Operación cancelada.")
        break 

    else:
        print("Opción inválida. Por favor, elija una opción del 1 al 4.")


