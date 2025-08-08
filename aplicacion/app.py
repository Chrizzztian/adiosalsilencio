# Importamos la librería web.py para crear nuestra aplicación web
import web

# Aquí definimos todas las rutas (URLs) de nuestra aplicación
# Cada ruta está conectada a una clase que maneja esa página
urls = (
    '/', 'Index',                                    # Página principal (home)
    '/registrar_tutor', 'RegistrarTutor',           # Formulario para registrar tutores
    '/registrar_chiquillo', 'RegistrarChiquillo',   # Formulario para registrar niños
    '/saludo_admin', 'SaludoAdmin',                 # Página de saludo para administradores
    '/saludo_chiquillo', 'SaludoChiquillo',         # Página de saludo para niños
    '/presentacion_lucas', 'PresentacionLucas',     # Presentación del personaje Lucas
    '/presentacion_pagina', 'PresentacionPagina',   # Presentación general de la aplicación
    '/lecciones', 'Lecciones',                      # Página principal de lecciones
    '/perfil_admin', 'PerfilAdmin',                 # Perfil del administrador/tutor
    '/iniciar_sesion', 'IniciarSesion',             # Página de inicio de sesión
    '/quienes_somos', 'QuienesSomos',               # Página informativa "Quiénes somos"
    '/inicio_administrador', 'InicioAdministrador'   # Panel de inicio para administradores
)

# Configuramos el motor de plantillas de web.py
# Le decimos que busque los archivos HTML en la carpeta 'templates'
# cache=False significa que los cambios se ven inmediatamente (útil para desarrollo)
render = web.template.render('templates', cache=False)

# Creamos la aplicación web usando las rutas definidas arriba
app = web.application(urls, globals())

# Clase que maneja la página principal (cuando alguien visita "/")
class Index:
    def GET(self):
        return render.index()

class RegistrarTutor:
    def GET(self):
        return render.registrar_tutor()

class RegistrarChiquillo:
    def GET(self):
        return render.registrar_chiquillo()
    
    def POST(self):
        # Obtenemos todos los datos que el usuario escribió en el formulario
        data = web.input()
        print("POST recibido en /registrar_chiquillo")  # Para debugging - ver en consola
        print("Datos:", data)  # Mostrar qué datos llegaron
        
        # Aquí podríamos procesar los datos del formulario
        # Por ejemplo: guardar los datos de los niños en una base de datos
        
        # Después de procesar, redirigimos al usuario a la página de saludo del admin
        print("Redirigiendo a /saludo_admin")
        raise web.seeother('/saludo_admin')  # Esto cambia la página automáticamente

class SaludoAdmin:
    def GET(self):
        print("GET recibido en /saludo_admin")
        print("Renderizando template saludo_admin")
        return render.saludo_admin()

class PerfilAdmin:
    def GET(self):
        return render.perfil_admin()

class IniciarSesion:
    def GET(self):
        return render.iniciar_sesion()

class QuienesSomos:
    def GET(self):
        return render.quienes_somos()

class InicioAdministrador:
    def GET(self):
        return render.inicio_administrador()
    
    def POST(self):
        # Obtener datos del formulario
        data = web.input()
        correo = data.get('correo', '')
        contraseña = data.get('contraseña', '')
        
        # Aquí puedes agregar la lógica de autenticación del administrador
        # Por ejemplo, verificar contra una base de datos o credenciales predefinidas
        
        # Por ahora, solo retornamos la misma página
        # En el futuro aquí redirigiríamos al dashboard de administrador
        return render.inicio_administrador()

class SaludoChiquillo:
    def GET(self):
        return render.saludo_chiquillo()

class PresentacionLucas:
    def GET(self):
        return render.presentacion_lucas()

class PresentacionPagina:
    def GET(self):
        return render.presentacion_pagina()

class Lecciones:
    def GET(self):
        return render.lecciones()

# Esta línea especial hace que la aplicación se ejecute solo cuando 
# ejecutamos este archivo directamente (no cuando lo importamos desde otro lugar)
if __name__ == "__main__":
    app.run()  # ¡Aquí arranca nuestro servidor web!