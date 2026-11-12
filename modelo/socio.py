from errores.prestamo_error import PrestamoError
class Socio:
    def __init__(self, codigo_soc,nombre,email,cod_libro_prestado = None):
        self.codigo_soc = codigo_soc
        self.nombre = nombre
        self.email=email
        self.cod_libro_prestado = cod_libro_prestado

    def tiene_libro(self):
        return self.cod_libro_prestado is not None 
     
    def prestar_libro(self, libro):
        if self.tiene_libro():
            raise PrestamoError("El socio ya tiene un libro", self.codigo_soc)
        if not libro.esta_disponible():
            raise PrestamoError("El libro no está disponible", libro.codigo)
        self.cod_libro_prestado = libro.codigo
        libro.cod_socio = self.codigo_soc
   