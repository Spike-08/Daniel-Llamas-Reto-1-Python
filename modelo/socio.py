class Socio:
    def __init__(self, codigo_soc,nombre,email,cod_libro_prestado = None):
        self.codigo_soc = codigo_soc
        self.nombre = nombre
        self.email=email
        self.cod_libro_prestado = cod_libro_prestado

    def tiene_libro(self):
    # devuelve True si el socio tiene un libro
        return self.cod_libro_prestado is not None 
     
    def prestar_libro(self, libro):
    # 1) el socio guarda el código del libro
    # 2) el libro guarda el código del socio
        self.cod_libro_prestado = libro.codigo
        libro.cod_socio = self.codigo_soc
   