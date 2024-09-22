# PythonTest


## Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Instalación

Sigue estos pasos para poner el proyecto en funcionamiento:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/nombre_del_proyecto.git
   cd nombre_del_proyecto

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv

   ```

  3. Activa el entorno virtual 
   En windows
   ```bash
   venv\Scripts\activate

   ```

   En macOS y Linux:
   ```bash
   source venv/bin/activate

   ```

   4. Instala las dependencias
   ```bash
   pip install -r requirements.txt

   ```

  5. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate

   ```

   6. Ejecuta el servidor de desarrollo
   ```bash
   python manage.py runserver

   ```
