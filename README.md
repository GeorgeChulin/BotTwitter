![python3.9](https://img.shields.io/badge/python-3.9-blue)

---

# Twitter Token

1. Entrar en esta página e iniciar sesión con la cuenta de twitter:

    [Twitter Developer](https://developer.twitter.com/en)

2. Hacer clic en 'Apply' arriba a la derecha y despues en 'Apply for a developer account'.

3. Hobbylist, make a bot

4. Rellenar con todos los datos que nos piden (Nombre, telefono, etc). En los campos de rellenar para qué vas a usar la API se puede poner cualquier cosa: *'I'm going to use the API to create a bot that retweets people's tweets.I'm going to use the API to create a bot that retweets people's tweets.I'm going to use the API to create a bot that retweets people's tweets.'* (debe llegar a 200 caracteres)

5. Una vez registrado hay que crear un proyecto y dentro de este una App

6. Dentro de la App tendremos un apartado 'Keys and tokens', de donde cogeremos y pegaremos en el lugar correspondiente del código los 'Customer keys' y 'Access Token and Secret'
---
# Requisitos

## Python 3.9

[Descarga Python 3.9 en windows store](https://www.microsoft.com/es-es/p/python-39/9p7qfqmjrfp7?activetab=pivot:overviewtab)

### Librerias de Python

- Tweepy 4.0.0
- Schedule
- Datetime

#### Cómo instalar las librerias

`pip3 install tweepy==4.0.1`

`pip3 install Schedule`

`pip3 install Datetime`

---

# Ejecutar aplicación
Abrir la terminan en el directorio de lal programa y ejecutar el comando:

`python3.9 TwitterBot.py`

Dejarlo ejecutándose todo el tiempo que queramos.
