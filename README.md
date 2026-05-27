# Diseño de una webapp con python3, web.py y sqlite 3
 
## 1. Crea un ambiente virtual (enviroment) 

crear un virtual enviroment para instalar las librerias necesarias de python 

````shell
python3 -m venv .venv
````
## 2. iniciar virtual enviroment 
iniciar el virtual enviroment para instalar las librerias necesarias para el proyecto 

````shell
source .venv/bin/activate
````

## 3. actualizar **pip**
 
actualizar el instalador de paquetes de python **pip**
````shell
pip install --upgrade pip
````

## 4. instalar el micro-framework **web.py**

instalar el micro-framework **web.py** para la creacion de aplicaciones web utilizando python.

````shell
pip install web.py
````

## 5. crear el archivo **requirements.txt**

crear el archivo **requirements** con la lista de las librerias y versiones de cada una, necesarias para el proyecto.

````shell
pip freeze > requirements.txt
````

## 6. crear el archivo **runtime.txt**

crear el archivo **runtime.txt** con la version de python3 utilizada.

````shell
python3 -V > runtime.txt
````
## 7. crear el archivo **.gitignore**

crear el archivo **.gitignore** para indicar las carpetas y archivos que no se van a sincronizar con el repositorio 

````shell
*.pyc
__pycache__/
.venv/
````
## 8. indexar las carpetas y archivos 

indexar las carpetas y archivos creados o modificados.

````shell
git add .
````

## 9. crear punto de control **COMMMI**

crear el punto de control **commit** con los cambios realizados al pryecto 

````shell
 git commit -m "CREATED configuracion del virtual environment"
 ````

## 10. sincronizar los cambios al repositorio 

sincronizar los cambios al proyecto con el repositorio. 

````shell
git push -u origin main
````