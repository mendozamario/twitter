#**Aplicación de python con acceso a twitter**

Para poder realizar la correcta ejecuciónd este programa, es necesario tener ciertas herramientas instaladas en la
computadora, recuerde que este programa funciona en cualquier sistema operativo (windows, linux, mac)

- Python
- Dash
- Configparser
- Pymysql
- MySql
- Cryptography

Para instalar Python [link](https://www.python.org/downloads/)
Para instalar MySql [link](https://www.mysql.com/downloads/)

``pip install dash``
``pip install configparser``
``pip install pymysql``
``pip install criptography``

Crear base de datos.
Para esto es necesario dirigirse al mysql command y ejecutar los siguientes comandos.
``CREATE DATABASE mys;``
``USE mys``
``CREATE TABLE usuario (Id VARCHAR(100), username VARCHAR(100), screen_name VARCHAR(60), location VARCHAR(30), followers_count FLOAT, friends_count FLOAT, listed_count FLOAT, favourites_count FLOAT, statuses_count FLOAT, verified BOOL);``

Para ejecutar este programa luego de realizar las correspondientes instalaciones es necesario ejecutar el siguiente
comando desde la terminal.

``python index.py``

Si se encuentra en visual studio, es posible ejecutarlo dirigiendose al boton de play, que es posible encontrarlo en
la parte superior derecha de la pantalla.

Luego de haber ejecutado el programa, en la consola le va a arrojar un link de localhost, el cual puede abrir 
presionando ctrl + click o simplemente copiando la dirección y pegandola en su navegador.

Una vez que se este ejecutando, que vea usted la pagina web, lo que sigue es insertar el nombre de usuario y darle
al boton de buscar.
