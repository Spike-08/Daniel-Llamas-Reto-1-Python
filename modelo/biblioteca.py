from modelo.libro import Libro
from modelo.socio import Socio

def cargar_libros(ruta):
    libros = []
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()            # quita el salto de línea
            if linea == "":                  # ignora líneas vacías
                continue
            campos = linea.split(";")        # lista con los 6 campos
            codigo = campos[0]
            titulo = campos[1]
            autor = campos[2]
            anio = int(campos[3])            # el año como número
            categoria = campos[4]
            cod_socio = None if campos[5] == "None" else campos[5] # ojo: el texto "None" debe pasar a None real
            libros.append(Libro(codigo, titulo, autor, anio, categoria, cod_socio))
    return libros

def cargar_socios(ruta):
    socios = []
    with open(ruta, "r", encoding ="utf-8")as f:
        for linea in f:
            linea = linea.strip()
            if linea  == "":
                continue
            campos = linea.split(";")
            codigo_soc = campos[0]
            nombre = campos[1]
            email = campos[2]
            cod_libro_prestado = None if campos[3] == "None" else campos[3]
            socios.append(Socio(codigo_soc,nombre,email,cod_libro_prestado))
    return socios

libros = cargar_libros("libros.txt")
socios = cargar_socios("socios.txt")
print(f"Se han cargado {len(libros)} libros y {len(socios)} socios.")

def guardar_libros(ruta, libros):
    with open(ruta, "w", encoding="utf-8") as f:
        for libro in libros:
            f.write(f"{libro.codigo};{libro.titulo};{libro.autor};{libro.anio};{libro.categoria};{libro.cod_socio}\n")

def guardar_socios(ruta,socios):
    with open(ruta, "w", encoding="utf-8") as f:
        for socio in socios:
           f.write(f"{socio.codigo_soc};{socio.nombre};{socio.email};{socio.cod_libro_prestado}\n")
    
def mostrar_libros(libros):
    print(f"{'Código':<8}{'Título':<35}{'Autor':<25}{'Estado'}")
    print("-" * 80)
    for libro in libros:
        estado = "Disponible" if libro.esta_disponible() else "Prestado"
        print(f"{libro.codigo:<8}{libro.titulo:<35}{libro.autor:<25}{estado}")

def mostrar_socios(socios):
    print(f"{'Código':<8}{'Nombre':<35}{'Email':<25}{'Estado'}")
    print("-" * 80)
    for socio in socios:
        estado = "None" if socio.prestar_libro() else "Prestado"
        print(f"{socio.codigo:<8}{socio.nombre:<35}{socio.email:<25}{estado}")
