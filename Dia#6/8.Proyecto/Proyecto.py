from pathlib import Path
import os

RUTA = Path.home() / "Recetas"

def inicio():
    os.system("clear")
    print("\n" + "=" * 45)  
    print("¡Bienvenido al Recetario de tu Cocina!")
    print("=" * 45)
    
    
    print(f"Las recetas se guardarán en: {RUTA}")
    recetas = 0
    
    for archivo in Path(RUTA).rglob("*.txt"):
        recetas += 1
    print(f"Actualmente tienes {recetas} recetas guardadas.")

    while True:
        print("\n¿Qué deseas hacer?")
        print("""
        1. Ver Categorías y Recetas
        2. Crear Nueva Receta
        3. Crear Categoría
        4. Eliminar Receta
        5. Eliminar Categoría
        6. Salir""")
        
        try:
            opcion = int(input("Selecciona una opción (1-6): "))
        except ValueError:
            os.system("clear")
            print("Por favor, ingresa un número válido.")
            continue
        
        if opcion == 1:
            ver_recetas()
        elif opcion == 2:
            crear_nueva_receta()
        elif opcion == 3:
            crear_categoria()
        elif opcion == 4:
            eliminar_receta()
        elif opcion == 5:
            eliminar_categoria()
        elif opcion == 6:
            print("¡Gracias por usar el Recetario de tu Cocina! ¡Hasta luego!")
            break
        else:
            os.system("clear")
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")
        

def ver_recetas():

    print("\n" + "=" * 45)
    print("\nCategorías disponibles:")
    categorias = {}
    for i, categoria in enumerate(RUTA.iterdir()):
        if categoria.is_dir():
            print(f"{i + 1}. {categoria.name}")
            categorias[categoria.name] = RUTA / categoria.name
    
    while True:
        try:
            opcion = int(input("\nSelecciona una categoría para ver sus recetas (o 0 para volver): "))
            if opcion == 0:
                inicio()
                break
            categoria_seleccionada = list(categorias.keys())[opcion - 1]
            ruta_categoria = categorias[categoria_seleccionada]
            print("=" * 45)
            print(f"\nRecetas en la categoría '{categoria_seleccionada}':")
            for receta in ruta_categoria.glob("*.txt"):
                print(f"- {receta.stem}")
            break
        except (ValueError, IndexError):
            print("Opción no válida. Por favor, selecciona una categoría válida.")

    print("\n¿Qué receta quieres ver?")
    while True:
        try:
            receta_seleccionada = input("Ingresa el nombre de la receta (o 'volver' para regresar): ")
            if receta_seleccionada.lower() == "volver":
                ver_recetas()
                break
            ruta_receta = categorias[categoria_seleccionada] / f"{receta_seleccionada}.txt"
            if ruta_receta.exists():
                with open(ruta_receta, "r") as archivo:
                    contenido = archivo.read()
                    print("-" * 45)
                    print(f"\nContenido de la receta '{receta_seleccionada}':\n")
                    print(contenido)
                print("-" * 45)
                break

            else:
                print("La receta no existe. Por favor, ingresa un nombre válido.")
        except KeyError:
            print("Categoría no válida. Por favor, selecciona una categoría válida.")


def crear_nueva_receta():
    
    print("\n" + "=" * 45)
    print("\nCategorías disponibles:")
    categorias = {}
    for i, categoria in enumerate(RUTA.iterdir()):
        if categoria.is_dir():
            print(f"{i + 1}. {categoria.name}")
            categorias[categoria.name] = RUTA / categoria.name
    
    while True:
        try:
            opcion = int(input("\nSelecciona una categoría para crear la receta (o 0 para volver): "))
            if opcion == 0:
                inicio()
                break
            categoria_seleccionada = list(categorias.keys())[opcion - 1]
            ruta_categoria = categorias[categoria_seleccionada]
            nombre_receta = input("Ingresa el nombre de la nueva receta: ")
            ruta_receta = ruta_categoria / f"{nombre_receta}.txt"
            if ruta_receta.exists():
                print("La receta ya existe. Por favor, elige otro nombre.")
            else:
                contenido_receta = input("Ingresa el contenido de la receta:\n")
                with open(ruta_receta, "w") as archivo:
                    archivo.write(contenido_receta)
                print(f"Receta '{nombre_receta}' creada exitosamente en la categoría '{categoria_seleccionada}'.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

def crear_categoria():
    nueva_categoria = input("Ingresa el nombre de la nueva categoría: ")
    ruta_nueva = RUTA / nueva_categoria
    if ruta_nueva.exists():
        print("La categoría ya existe.")
    else:
        ruta_nueva.mkdir()
        print(f"Categoría '{nueva_categoria}' creada exitosamente.")

def eliminar_receta():
    print("\n" + "=" * 45)
    print("\nCategorías disponibles:")
    categorias = {}
    for i, categoria in enumerate(RUTA.iterdir()):
        if categoria.is_dir():
            print(f"{i + 1}. {categoria.name}")
            categorias[categoria.name] = RUTA / categoria.name
    
    while True:
        try:
            opcion = int(input("\nSelecciona una categoría para ver sus recetas (o 0 para volver): "))
            if opcion == 0:
                inicio()
                break
            categoria_seleccionada = list(categorias.keys())[opcion - 1]
            ruta_categoria = categorias[categoria_seleccionada]
            print("=" * 45)
            print(f"\nRecetas en la categoría '{categoria_seleccionada}':")
            for receta in ruta_categoria.glob("*.txt"):
                print(f"- {receta.stem}")
            break
        except (ValueError, IndexError):
            print("Opción no válida. Por favor, selecciona una categoría válida.")

    print("\n¿Qué receta quiere eliminar?")
    while True:
        try:
            receta_seleccionada = input("Ingresa el nombre de la receta (o 'volver' para regresar): ")
            if receta_seleccionada.lower() == "volver":
                ver_recetas()
                break
            ruta_receta = categorias[categoria_seleccionada] / f"{receta_seleccionada}.txt"
            if ruta_receta.exists():
                ruta_receta.unlink()
                print(f"Receta '{receta_seleccionada}' eliminada exitosamente.")
                print("-" * 45)
                break

            else:
                print("La receta no existe. Por favor, ingresa un nombre válido.")
        except KeyError:
            print("Categoría no válida. Por favor, selecciona una categoría válida.")


def eliminar_categoria():
    print("\n" + "=" * 45)
    print("\nCategorías disponibles:")
    categorias = {}
    for i, categoria in enumerate(RUTA.iterdir()):
        if categoria.is_dir():
            print(f"{i + 1}. {categoria.name}")
            categorias[categoria.name] = RUTA / categoria.name
    
    while True:
        try:
            opcion = int(input("\nSelecciona una categoría para eliminar (o 0 para volver): "))
            if opcion == 0:
                inicio()
                break
            categoria_seleccionada = list(categorias.keys())[opcion - 1]
            ruta_categoria = categorias[categoria_seleccionada]
            for receta in ruta_categoria.glob("*.txt"):
                receta.unlink()
            ruta_categoria.rmdir()
            print(f"Categoría '{categoria_seleccionada}' eliminada exitosamente.")
            break
        except (ValueError, IndexError):
            print("Opción no válida. Por favor, selecciona una categoría válida.")
        except OSError:
            print("No se puede eliminar la categoría porque contiene recetas. Elimina las recetas primero.")


def main():
    inicio()


if __name__ == "__main__":
    main()