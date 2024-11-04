Realtime Chat Python
Este es un proyecto de chat en tiempo real utilizando Flask, Flask-SocketIO y MySQL. Los usuarios pueden unirse a diferentes salas de chat y enviar mensajes que se almacenan en una base de datos MySQL.

Requisitos Previos
Asegúrate de tener instalados los siguientes componentes antes de comenzar:

Python 3.7+
MySQL
pip (Administrador de paquetes de Python)


Instalación y Configuración
Paso 1: Clonar el Repositorio

git clone https://github.com/tu-usuario/realtime-chat-python.git
cd realtime-chat-python


Paso 2: Crear un Entorno Virtual
Es recomendable crear un entorno virtual para manejar las dependencias.

python3 -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

Paso 3: Instalar Dependencias
Instala las dependencias que están listadas en requirements.txt.

pip install -r requirements.txt

Paso 4: Configurar la Base de Datos MySQL
Inicia MySQL y asegúrate de tener las credenciales de acceso.

Ejecuta el script SQL de configuración que creará la base de datos y las tablas necesarias.

mysql -u tu_usuario -p < sql/setup_db.sql
Nota: Asegúrate de reemplazar tu_usuario con el usuario que usas en MySQL.

Contenido del archivo sql/setup_db.sql

Este script se encarga de:

Crear la base de datos chat_app si aún no existe.
Usar la base de datos chat_app.
Crear las tablas rooms y messages solo si no existen.

Paso 5: Configurar las Credenciales de la Base de Datos
Abre el archivo config/db_config.py.

Reemplaza las credenciales con las de tu instalación de MySQL:

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="chat_app"
    )
Cambia tu_usuario, tu_contraseña y chat_app por los valores correctos.

Paso 6: Ejecutar el Proyecto
Asegúrate de que el entorno virtual está activo.

Ejecuta el servidor de Flask:

python main.py
Abre tu navegador y accede a http://localhost:5000 para ver la aplicación.

Estructura del Proyecto

realtime-chat-python/
│
├── main.py                         # Archivo principal con la lógica de la aplicación y los sockets
├── requirements.txt                # Archivo de dependencias
├── README.md                       # Instrucciones del proyecto
├── setup_db.sql                    # Script SQL para crear la base de datos y las tablas
│
├── config/
│   └── db_config.py                # Configuración de conexión a la base de datos
│
├── models/
│   └── db.py                       # Funciones para interactuar con la base de datos (guardar mensajes, crear salas, etc.)
│
├── static/
│   └── css/
│       └── style.css               # Estilos de la aplicación
│
├── templates/
│   ├── base.html                   # Plantilla base
│   ├── home.html                   # Plantilla para la página principal
│   └── room.html                   # Plantilla para la sala de chat
│
└── sql/
    └── setup_db.sql                # Script SQL de creación de la base de datos y las tablas

Uso de la Aplicación
Ingresa un nombre en la página de inicio.
Puedes unirte a una sala existente ingresando el código de la sala o crear una nueva sala.
Envía mensajes en tiempo real dentro de la sala de chat.
Los mensajes enviados se almacenarán en la base de datos MySQL y se cargarán cuando un usuario ingrese a una sala.

Script de Creación de Base de Datos
El archivo sql/setup_db.sql contiene el script SQL para crear las tablas necesarias.
