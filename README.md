# Las peque noticias — Proyecto Final Django

Aplicación web tipo blog desarrollada con Python/Django.

## Funcionalidades

- **Inicio**: Página de inicio con posts recientes
- **Sobre mí**: Vista "Acerca de mí" en `/about/`
- **Noticias**: 
  - Listado con búsqueda
  - Detalle de post con "Leer más"
  - Crear, editar y eliminar (requiere login)
  - Mensaje "No hay noticias aún" si no hay posts
- **Cuentas**: App `accounts/`
  - Registro (username, email, password)
  - Login / Logout
  - Perfil con avatar, bio, nombre, apellido, email, fecha nacimiento
  - Edición de perfil y cambio de contraseña
- **Mensajería**: App `messaging/`
  - Bandeja de entrada y enviados
  - Envío de mensajes entre usuarios
  - Detalle y eliminación de mensajes

## Tecnologías

- Python 3.x
- Django 6.x
- django-ckeditor (texto enriquecido)
- Pillow (imágenes)
- SQLite (desarrollo)

## Instalación

```bash
git clone <repo-url>
cd TP_Final-Chavez
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Estructura

```
myblog/          # Configuración del proyecto
pages/           # App de posts/artículos
accounts/        # App de usuarios y perfiles
messaging/       # App de mensajería
templates/       # Templates HTML con herencia
static/css/      # Estilos CSS
```

