## 0. Instalar recursos 
Se puede instalar primero `venv`(entorno virtual) dentro de cada actividad que se realizará, así no contaminamos las demás carpetas.
1. `python3 -m venv venv`
* Al inicio no nos dejerá hacerlo, pues Debian/Ubuntu no tiene los paquetes necesarios (python3-venv)
2. `sudo apt install python3.13-venv -y`
* Ya después de poder tener los paquetes necesarios podremos usar **venv**.
* `source venv/bin/activate` es la forma para iniciar en el entorno virtual.  

Lo que si es posible es instalar **venv** para todas las carpetas que deseamos, pero en entornos reales de trabajo no es recomendable, porque se pierde la independenia.


![0.1](imagenes/instalar_recursos_1.PNG)

3. `pip install flask`, De esta forma ya también tenemos el otro recurso faltante para realizar la actividad.
![0.2](imagenes/instalar_recursos_2.PNG)


## 1. HTTP: Fundamentos y herramientas
1. Levanta la app 
![1.1](imagenes/run_app_py_1.PNG)
![1.2](imagenes/run_app_py_2.PNG)

Esa salida por consola es stdout, donde: 
* `PORT=8080`: Menciona que se escuchará en el puerto 8080.
* `MESSAGE="Hola CC3S2"`: Es el mensaje que devuelva la API.


2. Inspección con curl
Con otra terminal de Debian.
2.1. Petición GET normal
   * Usando `curl -v http://127.0.0.1:8080/`
   * ![2.1.1](imagenes/curl_1.PNG)
   * -v: muestra detalle de la conexión
2.2. Petición POST a una ruta no soportada
   * Con el comando `curl -i -X POST http://127.0.0.1:8080/`
   * ![2.2.1](imagenes/curl_2.PNG)
   * -i: incluye las cabeceras de respuesta.
   * Da una respuesta `HTTP/1.1 405 METHOD NOT ALLOWED` porque en el app.py solo está definida la petición GET.


3. Ver puertos abiertos
Como el puerto 8080 está siendo usado, lo podemos comprobar.
* `ss -ltnp | grep :8080`
![3.1](imagenes/puerto_1.PNG)

* Donde:
  * ss = herramienta para sockets
  * -l = solo sockets en escucha
  * -t = TCP
  * -n = mostrar números (no nombres de servicio)
  * -p = mostrar el proceso asociado

4. Logs a stdout
Cuando se ejecute peticiones con `curl`, se podrá observar líneas como:

![4.1](imagenes/stdout_1.PNG)
* Cumple con los principios de 12-Factor.
* Log van hacia stdout y no a los archivos locales.


## 2. DNS: nombres, registros y caché

























