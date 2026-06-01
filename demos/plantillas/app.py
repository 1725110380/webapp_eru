# Ejemplo de cómo mostrar una página HTML (plantilla) en vez de texto.
import web

urls = (
    '/', 'Inicio',
)

app = web.application(urls, globals())
# Le decimos dónde están las plantillas.
render = web.template.render('templates')

class Inicio:
    def GET(self):
        # Busca templates/index.html y lo muestra.
        return render.index()

if __name__ == "__main__":
    app.run()
