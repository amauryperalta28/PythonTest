# PythonTest


## Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Instalación

Sigue estos pasos para poner el proyecto en funcionamiento:


1. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv

   ```

2. Activa el entorno virtual 
   En windows
   ```bash
   venv-pythontest\Scripts\activate

   ```

   En macOS y Linux:
   ```bash
   source venv-pythontest/bin/activate

   ```

3. Instala las dependencias
   ```bash
   pip install -r requirements.txt

   ```

4. Realiza las migraciones de la base de datos:
   ```bash
   python manage.py migrate

   ```

5. Crear el usuario super user
   ```bash
   python manage.py createsuperuser

   ```
   - Indicar en el username: **alpha**
   - indicar en el correo: **alpha@gmail.com**
   - indicar en el password: **alpha123@**

6. Ejecuta el servidor de desarrollo backend
   ```bash
   python manage.py runserver

   ```

7. Entrar en la carpeta Site que es el frontend
   
8. Instalar las dependencias

   ```bash
   npm i
   ```

9. Correr el frontend
   ```bash
   npm start
