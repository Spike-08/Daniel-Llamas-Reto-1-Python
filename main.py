from modelo.libro import Libro

libro = Libro("L001", "978-1", "Dune", "Herbert", 1965, "Ciencia ficción")
print(libro.esta_disponible())   # debería salir True

libro.cod_socio = "S001"
print(libro.esta_disponible())   # debería salir False