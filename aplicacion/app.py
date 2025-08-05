import web

urls = (
    '/', 'Index',
    '/registrar_tutor', 'RegistrarTutor',
    '/registrar_chiquillo', 'RegistrarChiquillo',
    '/saludo_admin', 'SaludoAdmin',
    '/perfil_admin', 'PerfilAdmin',
    '/iniciar_sesion', 'IniciarSesion',
    '/quienes_somos', 'QuienesSomos',
    '/inicio_administrador', 'InicioAdministrador'
)

render = web.template.render('templates', cache=False)

app = web.application(urls, globals())

class Index:
    def GET(self):
        # Headers más agresivos para evitar caché
        web.header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        web.header('Pragma', 'no-cache')
        web.header('Expires', '0')
        web.header('Last-Modified', '')
        web.header('ETag', '')
        web.header('Vary', '*')
        return render.index()

class RegistrarTutor:
    def GET(self):
        # Headers para evitar caché
        web.header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        web.header('Pragma', 'no-cache')
        web.header('Expires', '0')
        web.header('Last-Modified', '')
        web.header('ETag', '')
        web.header('Vary', '*')
        return render.registrar_tutor()

class RegistrarChiquillo:
    def GET(self):
        # Headers para evitar caché
        web.header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        web.header('Pragma', 'no-cache')
        web.header('Expires', '0')
        web.header('Last-Modified', '')
        web.header('ETag', '')
        web.header('Vary', '*')
        return render.registrar_chiquillo()
    
    def POST(self):
        # Headers para evitar caché
        web.header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        web.header('Pragma', 'no-cache')
        web.header('Expires', '0')
        web.header('Last-Modified', '')
        web.header('ETag', '')
        web.header('Vary', '*')
        
        # Obtener datos del formulario
        data = web.input()
        print("POST recibido en /registrar_chiquillo")
        print("Datos:", data)
        
        # Aquí puedes procesar los datos del formulario si es necesario
        # Por ejemplo, guardar los datos de los niños registrados
        
        # Redirigir a la página de saludo del administrador
        print("Redirigiendo a /saludo_admin")
        raise web.seeother('/saludo_admin')

class SaludoAdmin:
    def GET(self):
        print("GET recibido en /saludo_admin")
        # Headers para evitar caché
        web.header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        web.header('Pragma', 'no-cache')
        web.header('Expires', '0')
        web.header('Last-Modified', '')
        web.header('ETag', '')
        web.header('Vary', '*')
        print("Renderizando template saludo_admin")
        return render.saludo_admin()

class PerfilAdmin:
    def GET(self):
        # Headers para evitar caché
        web.header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        web.header('Pragma', 'no-cache')
        web.header('Expires', '0')
        web.header('Last-Modified', '')
        web.header('ETag', '')
        web.header('Vary', '*')
        return render.perfil_admin()

class IniciarSesion:
    def GET(self):
        # Headers para evitar caché
        web.header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        web.header('Pragma', 'no-cache')
        web.header('Expires', '0')
        web.header('Last-Modified', '')
        web.header('ETag', '')
        web.header('Vary', '*')
        return render.iniciar_sesion()

class QuienesSomos:
    def GET(self):
        # Headers para evitar caché
        web.header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        web.header('Pragma', 'no-cache')
        web.header('Expires', '0')
        web.header('Last-Modified', '')
        web.header('ETag', '')
        web.header('Vary', '*')
        return render.quienes_somos()

class InicioAdministrador:
    def GET(self):
        # Headers para evitar caché
        web.header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        web.header('Pragma', 'no-cache')
        web.header('Expires', '0')
        web.header('Last-Modified', '')
        web.header('ETag', '')
        web.header('Vary', '*')
        return render.inicio_administrador()
    
    def POST(self):
        # Headers para evitar caché
        web.header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        web.header('Pragma', 'no-cache')
        web.header('Expires', '0')
        web.header('Last-Modified', '')
        web.header('ETag', '')
        web.header('Vary', '*')
        
        # Obtener datos del formulario
        data = web.input()
        correo = data.get('correo', '')
        contraseña = data.get('contraseña', '')
        
        # Aquí puedes agregar la lógica de autenticación del administrador
        # Por ejemplo, verificar contra una base de datos o credenciales predefinidas
        
        # Por ahora, solo retornamos la misma página
        # En el futuro aquí redirigiríamos al dashboard de administrador
        return render.inicio_administrador()

if __name__ == "__main__":
    app.run()