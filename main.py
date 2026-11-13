from datetime import datetime
from modelo.libro import Libro
from modelo.socio import Socio
from errores.prestamo_error import PrestamoError
from modelo.biblioteca import cargar_libros, cargar_socios, guardar_libros, guardar_socios, mostrar_libros

def registrar_log(evento, detalles):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{fecha}][{evento}][{detalles}]\n")

def main():
    # 1. Carga inicial
    try:
        libros = cargar_libros("datos/libros.txt")
        socios = cargar_socios("datos/socios.txt")
        print(f"Se han cargado {len(libros)} libros y {len(socios)} socios.")
    except FileNotFoundError:
        print("Error: No se encontraron los archivos de datos en la carpeta 'datos/'.")
        return
    
    print("\n--- Bienvenido a la Biblioteca DALLS ---")
    opcion = ""
    while opcion != "8":
        print("\n--- MENÚ BIBLIOTECA ---")
        print("1. Mostrar todos los libros")
        print("2. Mostrar libros disponibles")
        print("3. Buscar libro por título")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Mostrar socios con libro")
        print("7. Añadir socio/libro")
        print("8. Salir y guardar")
        
        opcion = input("\nElige una opción: ")
        
        # Usamos match-case, y con el case _ atrapamos las opciones incorrectas
        match opcion:
            case "1":
                mostrar_libros(libros)
            case "2":
                disponibilidad(libros)
            case "3":
                buscar_libro(libros)
            case "4":
                prestar_libro(socios, libros)
            case "5":
                devolucion(socios, libros)
            case "6":
                mostrar_socio_libro(socios, libros)
            case "7":
                anadir_libro_y_socio(libros, socios)
            case "8":
                guardar_socio_libros(libros, socios)
                break # IMPORTANTE: Rompe el bucle para salir
            case _:
                print("Opción no válida. Elige del 1 al 8.")

def disponibilidad(libros):
    print("\n--- LIBROS DISPONIBLES ---")
    disponibles = [l for l in libros if l.esta_disponible()]
    if not disponibles:
        print("No hay libros disponibles.")
    else:
        mostrar_libros(disponibles)
        
def buscar_libro(libros):
    termino = input("Introduce el título: ").lower()
    encontrados = [l for l in libros if termino in l.titulo.lower()]
    if encontrados:
        print(f"Se encontraron {len(encontrados)} libros:")
        mostrar_libros(encontrados)
    else:
        print("No se encontró ningún libro con ese título.")

def prestar_libro(socios, libros):
    cod_libro = input("Código del libro: ").strip().upper()
    cod_socio = input("Código del socio: ").strip().upper()
                
    libro_obj = next((l for l in libros if l.codigo == cod_libro), None)
    socio_obj = next((s for s in socios if s.codigo_soc == cod_socio), None)
    
    if libro_obj and socio_obj:
        try:
            socio_obj.prestar_libro(libro_obj)
            print(f"Préstamo realizado con éxito por el socio {cod_socio} al libro {cod_libro}")
            registrar_log("PRESTAMO", f"Socio {cod_socio} toma el libro {cod_libro}")
        except PrestamoError as e:
            if e.codigo == socio_obj.codigo_soc:
                print(f"Error: El socio {e.codigo} ya tiene un libro.")
            else:
                print(f"Error: El libro {e.codigo} ya está prestado.")
    else:
        print("Libro o socio no encontrado.")

def devolucion(socios, libros):
    # 1. Pedimos solo el código del socio
    cod_socio = input("Código del socio que devuelve el libro: ").strip().upper()
    socio_obj = next((s for s in socios if s.codigo_soc == cod_socio), None)
                
    if not socio_obj:
        print("Error: Socio no encontrado.")
    elif not socio_obj.tiene_libro():
        print("Error: Este socio no tiene ningún libro prestado.")
    else:   
        cod_libro = socio_obj.cod_libro_prestado
        libro_obj = next((l for l in libros if l.codigo == cod_libro), None)
                    
        if libro_obj:
            try:
                socio_obj.devolver_libro(libro_obj)
                print(f"Libro {cod_libro} devuelto correctamente.")
                registrar_log("DEVOLUCION", f"Socio {cod_socio} devuelve el libro {cod_libro}")
            except PrestamoError as e:
                print(f"Error inesperado: {e}")
        else:
            print("Error: El libro que tenía el socio no existe en el catálogo.")

def mostrar_socio_libro(socios, libros):
    print("\n--- SOCIOS CON LIBROS PRESTADOS ---")
    alguno = False
    for s in socios:
        if s.tiene_libro():
            libro_obj = next((l for l in libros if l.codigo == s.cod_libro_prestado), None)
            titulo = libro_obj.titulo if libro_obj else "Desconocido"
            print(f"Socio: {s.nombre} ({s.codigo_soc}) -> Libro: '{titulo}' ({s.cod_libro_prestado})")
            alguno = True
            
    if not alguno:
        print("Ningún socio tiene libros prestados actualmente.")

def anadir_libro_y_socio(libros, socios):
    tipo = input("\n¿Qué quieres añadir? (Libro/Socio): ").strip().upper()
                
    if tipo == "LIBRO":
        if libros:
            # Extraemos el número del último código (ej: "L100" -> 100) y le sumamos 1
            ultimo_num = int(libros[-1].codigo[1:]) 
            cod = f"L{ultimo_num + 1:03d}"
        else:
            cod = "L001"
            
        print(f"El código asignado automáticamente es: {cod}")
        
        titulo = input("Título: ")
        autor = input("Autor: ")
        anio = int(input("Año: "))
        categoria = input("Categoría: ")
        nuevo_libro = Libro(cod, titulo, autor, anio, categoria, None)
        libros.append(nuevo_libro)
        print("Libro añadido a la lista. (Se guardará al salir con la opción 8).")
                        
    elif tipo == "SOCIO":
        # Generar código automático para Socio (S001, S002...)
        if socios:
            ultimo_num = int(socios[-1].codigo_soc[1:])
            cod = f"S{ultimo_num + 1:03d}"
        else:
            cod = "S001"
            
        print(f"El código asignado automáticamente es: {cod}")
        
        nombre = input("Nombre: ")
        email = input("Email: ")
        nuevo_socio = Socio(cod, nombre, email, None)
        socios.append(nuevo_socio)
        print("Socio añadido a la lista. (Se guardará al salir con la opción 8).")
    else:
        print("Opción no válida. Escribe Libro o Socio.")

def guardar_socio_libros(libros, socios):
    guardar_libros("datos/libros.txt", libros) 
    guardar_socios("datos/socios.txt", socios)
    print("Datos guardados en los ficheros. ¡Hasta pronto!")

if __name__ == "__main__":
    main()