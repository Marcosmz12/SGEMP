import xmlrpc.client

# --- CONFIGURACIÓN ---
# Cambia estos valores por los de tu servidor Odoo
URL = 'http://127.0.0.1:8069' # URL de tu instancia
DB = 'desarrollo'
USERNAME = 'mmolzap0412@g.educaand.es' # Tu usuario o correo
PASSWORD = '7764d4817392f42ca64c3e27362a0d6d37c1142a' # Se recomienda usar API Key

# Nombres técnicos de los modelos (ajustar según tu módulo)
MODEL_SESSION = 'openacademy.session'
MODEL_COURSE = 'openacademy.course'

def main():
    # 1. CONEXIÓN Y AUTENTICACIÓN
    try:
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))
        uid = common.authenticate(DB, USERNAME, PASSWORD, {})

        if not uid:
            print("Error: No se pudo autenticar. Verifica credenciales.")
            return
        
        print(f"Autenticación exitosa. UID: {uid}")

        # Endpoint para interactuar con los modelos
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))
    except Exception as e:
        print(f"Error de conexión: {e}")
        return

    # 2. LISTAR SESIONES EXISTENTES Y SUS ASIENTOS
    print("\n--- Listado de Sesiones ---")
    try:
        # Usamos search_read para buscar y leer campos en una sola llamada
        # [[]] significa un dominio vacío (traer todos los registros)
        sessions = models.execute_kw(DB, uid, PASSWORD,
            MODEL_SESSION, 'search_read',
            [[]],
            {'fields': ['name', 'seats', 'course_id']} # Campos a leer
        )
        if not sessions:
            print("No se encontraron sesiones.")
        else:
            print(f"{'ID':<5} | {'Nombre de la Sesión':<30} | {'Asientos':<10} | {'Curso'}")
            print("-" * 70)
            for session in sessions:
                # course_id viene como una tupla (id, "Nombre Curso") o False
                course_name = session['course_id'][1] if session['course_id'] else "Sin curso"
                print(f"{session['id']:<5} | {session['name']:<30} | {session['seats']:<10} | {course_name}")
    except Exception as e:
        print(f"Error al leer sesiones: {e}")
    # 3. CREAR UNA NUEVA SESIÓN
    print("\n--- Creando Nueva Sesión ---")
    try:
        # Primero, necesitamos el ID de un curso existente para asociar la sesión.
        # Buscamos el último curso disponible por ejemplo.
        courses = models.execute_kw(DB, uid, PASSWORD,
            MODEL_COURSE, 'search_read',
            [[]],
            {'fields': ['name']} # Campos a leer
        )
        print(f"{'ID':<5} | {'Cursos Disponibles':<30}")
        print("-" * 35)
        for course in courses:
            print(f"{course['id']:<5} | {course['name']:<30}")
            course_id_to_use = course['id']
        print(f"El último curso encontrado para añadirle una sesión es {course_id_to_use}")
        # Datos de la nueva sesión
        new_session_data = {
        'name': 'Sesión creada via XML-RPC-2',
        'course_id' : course_id_to_use,
        'seats': 25
        }

        # La llamada 'create' toma una lista que contiene el diccionario de valores
        new_session_id = models.execute_kw(DB, uid, PASSWORD,
        MODEL_SESSION, 'create',
        [new_session_data]
        )

        print(f"¡Éxito! Nueva sesión creada con ID: {new_session_id} | Nombre: {new_sesion_data{'name'}} ")
    except Exception as e:
        print(f"Error al crear la sesión: {e}")
    
if __name__ == '__main__':
    main()