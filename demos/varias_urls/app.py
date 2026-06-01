# Ejemplo con varias rutas (URLs). Cada una muestra un texto distinto.
import web

urls = (
    '/',         'Inicio',
    '/acerca',   'Acerca',
    '/contacto', 'Contacto',
)

app = web.application(urls, globals())

# Una clase por ruta (POO).
class Inicio:
    def GET(self):
        return "Página de Inicio - prueba /acerca y /contacto"

class Acerca:
    def GET(self):
        return "Página: Acerca de"

class Contacto:
    def GET(self):
        return "Página: Contacto"

if __name__ == "__main__":
    app.run()
