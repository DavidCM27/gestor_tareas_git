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
