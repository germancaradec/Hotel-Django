# Hotel Furavery

## Descripción
El proyecto Hotel Furavery es una aplicación web desarrollada en Django que permite gestionar consultas relacionadas con un hotel. La aplicación proporciona una interfaz para registrar, consultar, actualizar y eliminar registros de consultas.

## Tecnología
Este proyecto utiliza Django para gestionar la lógica de aplicación, la interacción con la base de datos, y la generación de respuestas HTTP.

El proyecto utiliza MySQL como sistema de gestión de bases de datos.

Motor: django.db.backends.mysql
Host: localhost
Puerto: 3307
Usuario: root
Contraseña: (vacío en este caso)
Nombre de la base de datos: hotel_furavery1
Opciones: init_command con SET sql_mode='STRICT_TRANS_TABLES' para garantizar un modo de SQL estricto.

## Middleware y Seguridad

CORS: Se utiliza el middleware corsheaders para permitir solicitudes de orígenes cruzados (CORS_ALLOW_ALL_ORIGINS = True), facilitando el acceso a la API desde diferentes dominios.

CSRF: El middleware csrf_exempt se usa en las vistas para deshabilitar la protección CSRF en las solicitudes, facilitando las pruebas y el desarrollo, aunque esto debería ajustarse para producción.

## Vistas

GET: Obtiene consultas específicas o todas las consultas.
POST: Crea una nueva consulta a partir de los datos recibidos en la solicitud.
PUT: Actualiza una consulta existente según el id proporcionado.
DELETE: Elimina una consulta existente según el id proporcionado.

## Configuración Adicional

Archivo de Configuración de Django: Contiene configuraciones básicas y específicas del proyecto.
Validadores de Contraseña: Se utilizan validadores para garantizar la fortaleza de las contraseñas de los usuarios.

## Instalación y Configuración

Para configurar y ejecutar el proyecto localmente:
Clona el repositorio:
git clone https://github.com/germancaradec/Hotel-Furavery-Django.git

Instala las dependencias:
Asegúrate de tener pip y virtualenv instalados, luego:

pip install -r requirements.txt

Configura la base de datos: 
Asegúrate de que MySQL esté funcionando y que la base de datos hotel_furavery1 esté creada.

Ejecuta las migraciones:

python manage.py migrate

Inicia el servidor de desarrollo:
python manage.py runserver

Accede a la aplicación en http://127.0.0.1:8000/.