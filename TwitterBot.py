import tweepy
import random
import time
from random import randint
import schedule
import datetime

consumer_key = ''  # insertar consumer_key aquí (entre comillas simples: '1234' )
consumer_secret = ''  # insertar consumer_secret aquí (entre comillas simples: '1234' )
access_token = ''  # insertar access_token aquí (entre comillas simples: '1234' )
access_token_secret = ''  # insertar access_token_secret aquí (entre comillas simples: '1234' )

# Initialization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

"""
    ██╗   ██╗ █████╗ ██████╗ ██╗ █████╗ ██████╗ ██╗     ███████╗███████╗
    ██║   ██║██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝
    ██║   ██║███████║██████╔╝██║███████║██████╔╝██║     █████╗  ███████╗
    ╚██╗ ██╔╝██╔══██║██╔══██╗██║██╔══██║██╔══██╗██║     ██╔══╝  ╚════██║ 
     ╚████╔╝ ██║  ██║██║  ██║██║██║  ██║██████╔╝███████╗███████╗███████║    
      ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝
                                                                        """

lastTweet = 0  # No tocar

# Número de tweets que leerá con cada función
nItem = 30
# Fecha tope para buscar tweets
startDate = datetime.datetime(2021, 11, 9, 00, 00, 00, tzinfo=datetime.timezone.utc)

# INSERTE AQUÍ TODAS LAS FOTOS QUE QUIERA USAR PARA EL BOT (de 1 a n)
# si no quiere poner ninguna dejar solo los corchetes
# ES RECOMENDABLE PONER LAS FOTOS EN LA MISMA CARPETA QUE EL BOT O CREAR UNA CARPETA
# EN EL MISMO DIRECTORIO QUE EL BOT (COMO EN EL EJEMPLO)
# INDICAR LA RUTA RELATIVA (DESDE EL DIRECTORIO DEL BOT) DE LAS FOTOS

images = ['fotos/foto1.jpeg', 'fotos/foto2.jpeg', 'fotos/foto3.jpeg', 'fotos/foto4.jpeg', 'fotos/foto5.jpeg']
# si no quisieramos usar fotos, poner: images = []

image = "NULL"  # NO TOCAR

"""
██╗███╗   ███╗██████╗  ██████╗ ██████╗ ████████╗ █████╗ ███╗   ██╗████████╗███████╗
██║████╗ ████║██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝██╔════╝
██║██╔████╔██║██████╔╝██║   ██║██████╔╝   ██║   ███████║██╔██╗ ██║   ██║   █████╗  
██║██║╚██╔╝██║██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══██║██║╚██╗██║   ██║   ██╔══╝  
██║██║ ╚═╝ ██║██║     ╚██████╔╝██║  ██║   ██║   ██║  ██║██║ ╚████║   ██║   ███████╗
╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝
                                                                                    """

# TODAS LAS FUNCIONES CON TEXTO TIENEN UNA VARIANTE "_photo" PARA PUBLICAR EL TWEET CON LA FOTO
# QUE HAS PUESTO EN LA VARIABLE "image"


"""
    ██████╗ ███████╗████████╗██╗    ██╗███████╗███████╗████████╗███████╗
    ██╔══██╗██╔════╝╚══██╔══╝██║    ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝
    ██████╔╝█████╗     ██║   ██║ █╗ ██║█████╗  █████╗     ██║   ███████╗
    ██╔══██╗██╔══╝     ██║   ██║███╗██║██╔══╝  ██╔══╝     ██║   ╚════██║
    ██║  ██║███████╗   ██║   ╚███╔███╔╝███████╗███████╗   ██║   ███████║
    ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝   ╚══════╝
                                                                        """

# Hastag en el que buscar, introducir el que deseas
# También se puede buscar una palabra
hastag = '#ejemplo'

# Retweet with comment (#hastag)
# Cita con el texto de la variable 'retweetText' todos los tweets que que aparezcan en el hashtag
retweetText = 'texto de ejemplo'


def retweet_comment():
    print("Ejecutando retweet_comment...")
    for tweet in tweepy.Cursor(api.search_tweets, q=hastag, count=100).items(nItem):
        if not bool(tweet.in_reply_to_status_id):
            try:
                tweet_to_quote_url = "https://twitter.com/anyuser/status/" + tweet.id_str
                api.update_status(retweetText, attachment_url=tweet_to_quote_url)
                print("Tweet citado correctamente: ", tweet_to_quote_url)
            except Exception as err:
                print(err)
    print("Fin de retweet_comment")


def retweet_comment_photo():
    print("Ejecutando retweet_comment_photo...")

    for tweet in tweepy.Cursor(api.search_tweets, q=hastag, count=100).items(nItem):
        if not bool(tweet.in_reply_to_status_id):
            try:
                tweet_to_quote_url = "https://twitter.com/anyuser/status/" + tweet.id_str
                api.update_status_with_media(filename=image, status=retweetText, attachment_url=tweet_to_quote_url)
                print("Tweet citado con imagen correctamente: ", tweet_to_quote_url)

            except Exception as err:
                print(err)
    print("Fin de retweet_comment_photo")


# Retweet (#hastag)
# Retweetea todos los tweets que aparezcan en el hashtag
def retweet():
    print("Ejecutando retweet...")
    aciertos = 0
    for tweet in tweepy.Cursor(api.search_tweets, q=hastag).items(nItem):
        if not tweet.retweeted:
            try:
                api.retweet(tweet.id)
                aciertos += 1
            except Exception as err:
                print(err)
    if aciertos > 0:
        print("Tweets retweeteados correctamente -> ", aciertos)
    print("Fin de retweet")


"""
    ██████╗ ███████╗██████╗ ██╗     ██╗███████╗███████╗
    ██╔══██╗██╔════╝██╔══██╗██║     ██║██╔════╝██╔════╝
    ██████╔╝█████╗  ██████╔╝██║     ██║█████╗  ███████╗
    ██╔══██╗██╔══╝  ██╔═══╝ ██║     ██║██╔══╝  ╚════██║
    ██║  ██║███████╗██║     ███████╗██║███████╗███████║
    ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝╚══════╝╚══════╝
"""

"""
#####                IMPORTANTE                   #####
   NO ES RECOMENDABLE USAR LAS DOS FUNCIONES A LA VEZ   
    PUEDE PROVOCAR QUE NO RESPONDA A TODOS LOS TWEETS   
     SI SE QUIERE RESPONDER A MÁS DE UNA PERSONA LA    
   MEJOR OPCIÓN ES USAR LA LISTA Y AÑADIR A TODAS LAS  
                    PERSONAS AHÍ                       
                                                   """

# Sustituir el texto por el que deseas que utilice para responder
replyText = 'texto de ejemplo'

# Reply all tweets (person)
# Responde con el texto de la variable 'replyText' a todos los tweets que publique una persona

idperson = 'EJEMPLO'  # introducir el nombre de usuario (@) de la persona a la que se quiere responder


# ejemplo idperson = 'anne' (@anne)


def reply_all_person_tweets():
    print("Ejecutando reply_all_person_tweets...")
    for tweet in tweepy.Cursor(api.user_timeline, id=idperson, exclude_replies="True", include_rts="False").items(
            nItem):
        try:
            if tweet.created_at > startDate and not bool(tweet.in_reply_to_status_id):
                text = "@" + idperson + " " + replyText
                api.update_status(text, in_reply_to_status_id=tweet.id)
                time.sleep(40)
                print("Tweet respondido correctamente: ", "https://twitter.com/anyuser/status/" + tweet.id_str)
        except Exception as err:
            print(err)
    print("Fin de reply_all_person_tweets")


def reply_all_person_tweets_photo():
    print("Ejecutando reply_all_person_tweets_photo...")
    for tweet in tweepy.Cursor(api.user_timeline, id=idperson, exclude_replies="True", include_rts="False").items(
            nItem):
        try:
            if tweet.created_at > startDate and not bool(tweet.in_reply_to_status_id):
                text = "@" + idperson + " " + replyText
                api.update_status_with_media(filename=image, status=text, in_reply_to_status_id=tweet.id)
                time.sleep(40)
                nextPhoto()
                print("Tweet respondido con imagen correctamente: ", "https://twitter.com/anyuser/status/" +
                      tweet.id_str)
        except Exception as err:
            print(err)
    print("Fin de reply_all_person_tweets_photo")


# Reply all tweets (list)
# Responde con el texto de la variable 'replyText' a todos los tweets que se publiquen en una lista de twitter
# ¿Qué es una lista? una lista es una opción de twitter para que muestre solo los tweets de unas personas seleccionadas
# Crear una lista en twitter es muy facil, buscamos el apartado de 'listas' y creamos una, a continuación elegimos
# las cuentas que queremos que aparezcan y una vez dentro de las lista, copiamos su ID, que la pegaremos en la variable
# 'idlista'. La ID de la lista se encuentra en la url (twitter.com/..../lists/123 <- son estos números)

#### IMPORTANTE ####
# En ocasiones cuando añades alguna cuenta a la lista no se añade bien y no aparecen sus tweets, retweets...
# en este caso deberemos eliminar esa cuenta de la lista y volver a añadir la misma cuenta.

idlista = 123  # id de la lista que se quiere usar (poner el número sin comillas)


def reply_all_list_tweets():
    print("Ejecutando reply_all_list_tweets...")
    global lastTweet
    statuses = []
    for status in tweepy.Cursor(api.list_timeline, list_id=idlista, include_rts="False", since_id=lastTweet).items(
            nItem):
        statuses.append(status)
    for tweet in reversed(statuses):
        try:
            if tweet.created_at > startDate and not bool(tweet.in_reply_to_status_id):
                text = "@" + tweet.user.screen_name + " " + replyText
                api.update_status(text, in_reply_to_status_id=tweet.id)
                time.sleep(40)
                lastTweet = tweet.id
                print("Tweet respondido correctamente: ", "https://twitter.com/anyuser/status/" + tweet.id_str)

        except Exception as err:
            print(err)
    print("Fin de reply_all_list_tweets...")


def reply_all_list_tweets_photo():
    print("Ejecutando reply_all_list_tweets_photo...")

    global lastTweet
    statuses = []
    for status in tweepy.Cursor(api.list_timeline, list_id=idlista, include_rts="False", since_id=lastTweet).items(
            nItem):
        statuses.append(status)
    for tweet in reversed(statuses):
        try:
            if tweet.created_at > startDate and not bool(tweet.in_reply_to_status_id):
                text = "@" + tweet.user.screen_name + " " + replyText
                api.update_status_with_media(filename=image, status=text, in_reply_to_status_id=tweet.id)
                time.sleep(40)
                lastTweet = tweet.id
                nextPhoto()
                print("Tweet respondido con imagen correctamente: ", "https://twitter.com/anyuser/status/" +
                      tweet.id_str)
        except Exception as err:
            print(err)
    print("Ejecutando reply_all_list_tweets_photo...")


"""
    ███╗   ██╗███████╗██╗    ██╗    ████████╗██╗    ██╗███████╗███████╗████████╗    
    ████╗  ██║██╔════╝██║    ██║    ╚══██╔══╝██║    ██║██╔════╝██╔════╝╚══██╔══╝    
    ██╔██╗ ██║█████╗  ██║ █╗ ██║       ██║   ██║ █╗ ██║█████╗  █████╗     ██║       
    ██║╚██╗██║██╔══╝  ██║███╗██║       ██║   ██║███╗██║██╔══╝  ██╔══╝     ██║       
    ██║ ╚████║███████╗╚███╔███╔╝       ██║   ╚███╔███╔╝███████╗███████╗   ██║       
    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝        ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝       
                                                                                """

# Texto que se usará cuando publique un tweet
tweetText = 'texto de ejemplo'


# New tweet
# Publica un tweet con el texto de la variable 'tweetText'
def new_tweet():
    print("Ejecutando new_tweet...")
    try:
        api.update_status(tweetText, in_reply_to_status_id=random.randint(0, 1000))
        print("Tweet publicado correctamente")
    except Exception as err:
        print(err)
    print("Fin de new_tweet")


def new_tweet_photo():
    print("Ejecutando new_tweet_photo...")
    try:
        api.update_status_with_media(filename=image, status=tweetText, in_reply_to_status_id=random.randint(0, 1000))
        nextPhoto()
        print("Tweet con imagen publicado correctamente")
    except Exception as err:
        print(err)
    print("Fin de new_tweet")


"""
    ██████╗ ███████╗██╗     ███████╗████████╗███████╗    ████████╗██╗    ██╗███████╗███████╗████████╗███████╗     
    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝    ╚══██╔══╝██║    ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝    
    ██║  ██║█████╗  ██║     █████╗     ██║   █████╗         ██║   ██║ █╗ ██║█████╗  █████╗     ██║   ███████╗    
    ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝         ██║   ██║███╗██║██╔══╝  ██╔══╝     ██║   ╚════██║    
    ██████╔╝███████╗███████╗███████╗   ██║   ███████╗       ██║   ╚███╔███╔╝███████╗███████╗   ██║   ███████║    
    ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝       ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝   ╚══════╝    
                                                                                                            """


# Delete all
# Borra todo el contenido publicado en la cuenta
def delete():
    for tweet in tweepy.Cursor(api.user_timeline).items():
        api.destroy_status(tweet.id)
    print("Tweets eliminados correctamente")


#####################################################
###################### IGNORAR ######################
#####################################################
def inicio():
    last_reply()
    initPhoto()


# Esta función se usa al iniciar el programa para recoger el ID del ultimo tweet respondido
def last_reply():
    global lastTweet
    statuses = []
    for status in tweepy.Cursor(api.user_timeline).items(50):
        if not "RT" in status.text:
            try:
                statuses.append(status)
            except Exception as err:
                print(err)
    i = 0
    if len(statuses) != 0:
        while not bool(statuses[i].in_reply_to_status_id) and i < len(statuses) - 1:
            i += 1
        lastTweet = statuses[i].in_reply_to_status_id
    else:
        lastTweet = 1


def initPhoto():
    global image
    if len(image) > 0:
        image = images[randint(0, len(images) - 1)]


def nextPhoto():
    global image
    x = (images.index(image) + 1) % 5
    image = images[x]


#####################################################
#####################################################
#####################################################

"""                                                                
                            ██████   ██████   █████████   █████ ██████   █████    
                           ░░██████ ██████   ███░░░░░███ ░░███ ░░██████ ░░███     
                            ░███░█████░███  ░███    ░███  ░███  ░███░███ ░███     
                            ░███░░███ ░███  ░███████████  ░███  ░███░░███░███     
                            ░███ ░░░  ░███  ░███░░░░░███  ░███  ░███ ░░██████     
                            ░███      ░███  ░███    ░███  ░███  ░███  ░░█████     
                            █████     █████ █████   █████ █████ █████  ░░█████    
                           ░░░░░     ░░░░░ ░░░░░   ░░░░░ ░░░░░ ░░░░░    ░░░░░ 
"""


## Insertar todas las funciones que se quieren ejecutar aquí
## con 'schedule' se crea un bucle que se repite cada x tiempo (se introduce cuando se llama a la función,
# ejemplo más abajo)

def main():
    inicio()

    # INTRODUCIR AQUÍ LAS FUNCIONES

    # EJEMPLOS (Se puede poner el temporizador en hora/s (hours) o en minuto/s (minutes))
    #    schedule.every(10).minutes.do(retweet())
    #    schedule.every(1).hours.do(retweet_comment())
    #    schedule.every(30).minutes.do(reply_all_person_tweets())
    #    schedule.every(40).minutes.do(reply_all_list_tweets())
    #    schedule.every().day.at('12:00').do(new_tweet)

    # A PARTIR DE AQUÍ NO TOCAR
    while True:
        try:
            schedule.run_pending()
        except tweepy.errors.TweepyException as e:
            raise e


if __name__ == "__main__":
    main()
