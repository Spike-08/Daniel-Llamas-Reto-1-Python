# Daniel-Llamas-Reto-1-Python
# Sistema de Gestión de Biblioteca 

Proyecto final de Programación Orientada a Objetos en Python. Se trata de un sistema de gestión de biblioteca por consola que permite administrar libros y socios, gestionar préstamos y devoluciones, y persistir los datos en archivos de texto.

##  Características principales

- **Programación Orientada a Objetos (POO):** Clases `Libro` y `Socio` con responsabilidades bien definidas.
- **Persistencia de datos:** Carga inicial de 100 libros y 15 socios desde archivos `.txt` (carpeta `datos/`) y guardado automático al salir.
- **Gestión de excepciones:** Excepción personalizada `PrestamoError` con atributo de instancia (`codigo`) para identificar si el error es por el socio o por el libro.
- **Registro de actividad:** Los préstamos y devoluciones se registran con fecha y hora en el archivo `log.txt`.
- **Modularidad:** Separación de responsabilidades en carpetas `modelo/`, `errores/` y un `main.py` que actúa como controlador de flujo.
- **Menú interactivo:** Implementado con `match-case` para un enrutamiento limpio de las opciones.

##  Requisitos e Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>