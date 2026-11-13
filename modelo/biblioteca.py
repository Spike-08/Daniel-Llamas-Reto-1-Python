from modelo.libro import Libro
from modelo.socio import Socio

def cargar_libros(ruta):
    libros = []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea == "":
                    continue
                
                campos = linea.split(";")
                codigo = campos[0]
                titulo = campos[1]
                autor = campos[2]
                anio = int(campos[3])
                categoria = campos[4]
                # Si el campo es "None" (texto), lo convertimos a None real de Python
                cod_socio = None if campos[5] == "None" else campos[5]
                
                libros.append(Libro(codigo, titulo, autor, anio, categoria, cod_socio))
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")
    return libros

def cargar_socios(ruta):
    socios = []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea == "":
                    continue
                
                campos = linea.split(";")
                codigo_soc = campos[0]
                nombre = campos[1]
                email = campos[2]
                # Si el campo es "None", lo convertimos a None real
                cod_libro_prestado = None if campos[3] == "None" else campos[3]
                
                socios.append(Socio(codigo_soc, nombre, email, cod_libro_prestado))
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")
    return socios

def guardar_libros(ruta, libros):
    with open(ruta, "w", encoding="utf-8") as f:
        for libro in libros:
            # Si el socio es None, escribimos la palabra "None" para que al leerlo se entienda
            socio_texto = "None" if libro.cod_socio is None else libro.cod_socio
            f.write(f"{libro.codigo};{libro.titulo};{libro.autor};{libro.anio};{libro.categoria};{socio_texto}\n")

def guardar_socios(ruta, socios):
    with open(ruta, "w", encoding="utf-8") as f:
        for socio in socios:
            libro_texto = "None" if socio.cod_libro_prestado is None else socio.cod_libro_prestado
            f.write(f"{socio.codigo_soc};{socio.nombre};{socio.email};{libro_texto}\n")

def mostrar_libros(libros):
    if not libros:
        print("No hay libros para mostrar.")
        return
        
    print(f"{'Código':<8} | {'Título':<35} | {'Autor':<25} | {'Estado'}")
    print("-" * 90)
    for libro in libros:
        estado = "Disponible" if libro.esta_disponible() else f"Prestado a {libro.cod_socio}"
        # Acortamos el título si es muy largo para que la tabla quede mas organizada y comprensible para el usuario
        titulo_corto = (libro.titulo[:32] + '...') if len(libro.titulo) > 35 else libro.titulo
        autor_corto = (libro.autor[:22] + '...') if len(libro.autor) > 25 else libro.autor
        print(f"{libro.codigo:<8} | {titulo_corto:<35} | {autor_corto:<25} | {estado}")
