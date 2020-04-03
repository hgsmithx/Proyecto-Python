1) Se debe ejecutar el archivo proyecto_vacuna.py .
Para poder tener estos archivos se debe posicionar en una carpeta donde se quiera
tener los documentos para ello, desde consola nos posicionamos
en la carpeta y ejecutamos 
"   git init 
    git clone https://github.com/hgsmithx/Proyecto-Python.git" 
Para ello nos posicionamos en la carpeta donde este el archivo proyecto_vacuna.py
para luego ejecutarlo de la siguiente manera: 
python proyecto_vacuna.py

2) para ello se debe instalar ciertas cosas dentro de nuestro equipo.
partiendo por python este se puede encontrar en la pagina principal de python

3) ejecutar desde consola pip install -U pip

4) pip install -r requiriments.txt (ubicarse en la carpeta del proyecto anteriormente clonado)

5) dirigirse a la chocolatey.org luego ir a GET STARTED y copiar este comando desde la powerShell 
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
luego

6) ejecutar desde consola choco install mariadb

7) aceptar todo 

8) luego abrir MariaDB y seleccionar hostnameIP 127.0.0.1

9) luego OPEN y abrir con el programa el script SQL importado en el clone que se descargo previamente.
