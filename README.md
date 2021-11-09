![python3.9](https://img.shields.io/badge/python-3.9-blue)

---

# Descargar el código
### 1. Copiar y pegar el código
### 2. Descargar el proyecto desde el cuadrado verde que pone 'Code'
Dentro del código, **hay diferentes funciones** con diferentes opciones para el bot.
Para cada funcion o conjunto de funciones, hay una serie de **comentarios que indica lo que hace** y que indican los **parametros que se pueden modificar.**
	
**Es recomendable leer todos los comentarios del código previamente antes de lanzar la aplicación.**

# Twitter Token

1. Entrar en esta página e **iniciar sesión** con la cuenta de twitter:

    [Twitter Developer](https://developer.twitter.com/en)

2. Hacer **clic en 'Apply'** arriba a la derecha y despues en **'Apply for a developer account'.**

3. Hobbylist, make a bot

4. **Rellenar con todos los datos** que nos piden (Nombre, telefono, etc). En los campos de rellenar para qué vas a usar la API **se puede poner cualquier cosa:** *'I'm going to use the API to create a bot that retweets people's tweets.I'm going to use the API to create a bot that retweets people's tweets.I'm going to use the API to create a bot that retweets people's tweets.'* (debe llegar a 200 caracteres)

5. Una vez registrado hay que **crear un proyecto y** dentro de este **una App**

6. En el apartado de *Settings* **deberemos editar** el apartado *App permissions* y seleccionar *Read and write and Direct message*.

7. **Abir el código** con un entorno de desarrollo (Para descargar Visual Studio Code leer el apartado de requisitos)

8. Dentro de la App tendremos un apartado 'Keys and tokens', de donde **cogeremos y pegaremos en el lugar correspondiente del código** los **'Customer keys'(API Key and Secret) y 'Access Token and Secret'**

---
# Requisitos

## Python 3.9

[Descarga Python 3.9 en windows store](https://www.microsoft.com/es-es/p/python-39/9p7qfqmjrfp7?activetab=pivot:overviewtab)

### Entorno de desarrollo
##### [Visual Studio Code](https://code.visualstudio.com/download)
- Plugins para Visual Studio Code:
	- Python

### Librerias de Python
- Tweepy 4.0.0
- Schedule
- Datetime

---

# Ejecutar aplicación
Existen 2 maneras

## 1. Terminal

Con las librerías previamente instaladas, **abrir la terminal en el directorio del programa** y ejecutar el comando:

`python3.9 TwitterBot.py`

#### Cómo instalar las librerias

`pip3 install tweepy==4.0.1`

`pip3 install Schedule`

`pip3 install Datetime`

**Dejarlo ejecutándose** todo el tiempo que queramos.

## 2. Entorno de Desarrollo
**Con python instalado correctamente en el pc y el plugin Python añadido** a Visual Studio Code, **pulsar en el botón *play*** que aparecerá arriba a la derecha.

**La primera vez** que pulsemos el botón nos saldrá un recuadro en la parte superior para elegir la configuración, **eligiremos *python3.9 para Windows***
