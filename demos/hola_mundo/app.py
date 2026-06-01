# El programa más básico de web.py: muestra un texto en pantalla.
import web

# Una sola ruta: la raíz '/' la maneja la clase Inicio.
urls = (
    '/', 'Inicio',
)

app = web.application(urls, globals())

class Inicio:
    def GET(self):
        return "¡Hola, mundo!"

# Arranca el servidor en http://localhost:8080/
if __name__ == "__main__":
    app.run()
