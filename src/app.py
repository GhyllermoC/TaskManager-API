# Sistema básico de gestión de tareas

tareas = []

print("=== TASK MANAGER API ===")

while True:

    print("\n1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        tarea = input("Ingrese una nueva tarea: ")
        tareas.append(tarea)

        print("✅ Tarea agregada correctamente.")

    elif opcion == "2":

        print("\n📋 LISTA DE TAREAS")

        if len(tareas) == 0:
            print("No existen tareas registradas.")

        else:
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

    elif opcion == "3":

        print("Saliendo del sistema...")
        break

    else:
        print("❌ Opción inválida.")