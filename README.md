# PythonTest

## Instalación backend usando Docker

```
docker-compose up
```

Para acceder al backend navegar a la url
http://localhost:8000/admin/

Para acceder al frontend navegar a la url
http://localhost:4200/login

## Instalación backend

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

## Como correr las pruebas
 ### Activa el entorno virtual 
   En windows
   ```bash
   venv-pythontest\Scripts\activate
   ```

   En macOS y Linux:
   ```bash
   source venv-pythontest/bin/activate
   ```

Dentro de la carpeta **APIProject**, correr el comando
```bash
python manage.py test
```

## Instalacion frontend
1. Entrar en la carpeta Site que es el frontend
   
2. Instalar las dependencias

   ```bash
   npm i
   ```

3. Correr el frontend
   ```bash
   npm start
