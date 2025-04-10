print("Bienvenido al gestor de tareas")

# Versión 1 - Guardar tareas
with open("tareas.txt", "a") as archivo:
    tarea = input("Escribe una nueva tarea: ")
    archivo.write(tarea + "\n")
    print("Tarea guardada.")

# Versión 2 - Ver tareas
print("\nTus tareas:")
with open("tareas.txt", "r") as archivo:
    print(archivo.read())
def agregar_tarea():
    tarea = input("Escribe una nueva tarea: ")
    with open("tareas.txt", "a") as archivo:
        archivo.write(tarea + "\n")
    print("Tarea guardada.")

def ver_tareas():
    print("\nTus tareas:")
    try:
        with open("tareas.txt", "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("No hay tareas aún.")

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
