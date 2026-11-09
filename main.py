from modelo.libro import Libro
from modelo.socio import Socio

libro = Libro("L001", "Dune", "Herbert", 1965, "Ciencia ficción")
socio = Socio("S001", "Ana", "ana@mail.com")

print(socio.tiene_libro())          # False
socio.prestar_libro(libro)
print(socio.tiene_libro())          # True
print(libro.esta_disponible())      # False
print(socio.cod_libro_prestado)     # L001
print(libro.cod_socio)              # S001