# Importing all modules/packages/libraries
from logging import exception
from math import e
import tweepy
import random
import time
import schedule
import datetime

consumer_key ='' # insertar consumer_key aquí (entre comillas simples: '1234' )
consumer_secret = '' # insertar consumer_secret aquí (entre comillas simples: '1234' )
access_token = '' # insertar access_token aquí (entre comillas simples: '1234' )
access_token_secret = '' # insertar access_token_secret aquí (entre comillas simples: '1234' )

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

# Hashtag 
nItem = 30
startDate = datetime.datetime(2021, 10, 24, 00, 00, 00, tzinfo=datetime.timezone.utc)
lastTweet = 0
# INSERTE AQUÍ TODAS LAS FOTOS QUE QUIERA USAR PARA EL BOT (de 1 a n)
images = ['fotos/foto1.jpeg', 'fotos/foto2.jpeg', 'fotos/foto3.jpeg', 'fotos/foto4.jpeg', 'fotos/foto5.jpeg']
image = "NULL" # NO TOCAR

"""
     █████ ██████   ██████ ███████████     ███████    ███████████   ███████████   █████████   ██████   █████ ███████████ ██████████
    ░░███ ░░██████ ██████ ░░███░░░░░███  ███░░░░░███ ░░███░░░░░███ ░█░░░███░░░█  ███░░░░░███ ░░██████ ░░███ ░█░░░███░░░█░░███░░░░░█
     ░███  ░███░█████░███  ░███    ░███ ███     ░░███ ░███    ░███ ░   ░███  ░  ░███    ░███  ░███░███ ░███ ░   ░███  ░  ░███  █ ░ 
     ░███  ░███░░███ ░███  ░██████████ ░███      ░███ ░██████████      ░███     ░███████████  ░███░░███░███     ░███     ░██████   
     ░███  ░███ ░░░  ░███  ░███░░░░░░  ░███      ░███ ░███░░░░░███     ░███     ░███░░░░░███  ░███ ░░██████     ░███     ░███░░█   
     ░███  ░███      ░███  ░███        ░░███     ███  ░███    ░███     ░███     ░███    ░███  ░███  ░░█████     ░███     ░███ ░   █
     █████ █████     █████ █████        ░░░███████░   █████   █████    █████    █████   █████ █████  ░░█████    █████    ██████████
    ░░░░░ ░░░░░     ░░░░░ ░░░░░           ░░░░░░░    ░░░░░   ░░░░░    ░░░░░    ░░░░░   ░░░░░ ░░░░░    ░░░░░    ░░░░░    ░░░░░░░░░░  """

# TODAS LAS FUNCIONES CON TEXTO TIENEN UNA VARIANTE "_photo" PARA PUBLICAR EL TWEET CON LA FOTO QUE HAS PUESTO EN LA VARIABLE "image"


"""
    ██████╗ ███████╗████████╗██╗    ██╗███████╗███████╗████████╗███████╗
    ██╔══██╗██╔════╝╚══██╔══╝██║    ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝
    ██████╔╝█████╗     ██║   ██║ █╗ ██║█████╗  █████╗     ██║   ███████╗
    ██╔══██╗██╔══╝     ██║   ██║███╗██║██╔══╝  ██╔══╝     ██║   ╚════██║
    ██║  ██║███████╗   ██║   ╚███╔███╔╝███████╗███████╗   ██║   ███████║
    ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝   ╚══════╝
                                                                        """

# Hastag en el que buscar (también se puede buscar una palabra)
hastag = '#ejemplo'

# Retweet with comment (#hastag)
## Cita todos los tweets que que aparezcan en el hashtag con el texto de la variable 'retweetText' que aparece a continuación 
retweetText = 'texto de ejemplo'


def retweet_comment():
    for tweet in tweepy.Cursor(api.search_tweets, q=hastag, count=100).items(nItem):
        if bool(tweet.in_reply_to_status_id):
            try:
                tweet_to_quote_url = "https://twitter.com/anyuser/status/" + tweet.id_str
                api.update_status(retweetText, attachment_url=tweet_to_quote_url)
            except Exception as err:
                print(err)


def retweet_comment_photo():
    for tweet in tweepy.Cursor(api.search_tweets, q=hastag, count=100).items(nItem):
        if bool(tweet.in_reply_to_status_id):
            try:
                tweet_to_quote_url = "https://twitter.com/anyuser/status/" + tweet.id_str
                # api.update_status_with_media(filename="foto.jpg", status = retweetText, in_reply_to_status_id=tweet.id)
            except Exception as err:
                print(err)


# Retweet (#hastag)
## Retweetea todos los tweets que aparezcan en el hashtag
def retweet():
    aciertos = 0
    fallos = 0
    for tweet in tweepy.Cursor(api.search_tweets, q=hastag).items(nItem):
        if not tweet.retweeted:
            try:
                api.retweet(tweet.id)
            except Exception as err:
                print(err)


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

replyText = 'texto de ejemplo'

# Reply all tweets (person)
## Responde a todos los tweets que publique una persona con el texto de la variable 'replyText'
idperson = 'EJEMPLO'  # introducir el '@' de la persona a la que se quiere reponder (sin el @)


def reply_all_person_tweets():
    for tweet in tweepy.Cursor(api.user_timeline, id=idperson, exclude_replies="True", include_rts="False").items(
            nItem):
        try:
            if (tweet.created_at > startDate):
                text = "@" + idperson + " " + replyText
                api.update_status(text, in_reply_to_status_id=tweet.id)
                time.sleep(40)
                print(tweet.text, "https://twitter.com/anyuser/status/" + tweet.id_str)
        except Exception as err:
            print(err)


def reply_all_person_tweets_photo():
    for tweet in tweepy.Cursor(api.user_timeline, id=idperson, exclude_replies="True", include_rts="False").items(
            nItem):
        try:
            if (tweet.created_at > startDate):
                text = "@" + idperson + " " + replyText
                api.update_status_with_media(filename=image, status=text, in_reply_to_status_id=tweet.id)
                time.sleep(40)
                nextPhoto()
                print(tweet.text, "https://twitter.com/anyuser/status/" + tweet.id_str)
        except Exception as err:
            print(err)


# Reply all tweets (list)
## Responde a todos los tweets que se publiquen en una lista de twitter con el texto de la variable 'replyText'
idlista =   # id de la lista que se quiere usar


def reply_all_list_tweets():
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
        except Exception as err:
            print(err)


def reply_all_list_tweets_photo():
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
        except Exception as err:
            print(err)


"""
    ███╗   ██╗███████╗██╗    ██╗    ████████╗██╗    ██╗███████╗███████╗████████╗    
    ████╗  ██║██╔════╝██║    ██║    ╚══██╔══╝██║    ██║██╔════╝██╔════╝╚══██╔══╝    
    ██╔██╗ ██║█████╗  ██║ █╗ ██║       ██║   ██║ █╗ ██║█████╗  █████╗     ██║       
    ██║╚██╗██║██╔══╝  ██║███╗██║       ██║   ██║███╗██║██╔══╝  ██╔══╝     ██║       
    ██║ ╚████║███████╗╚███╔███╔╝       ██║   ╚███╔███╔╝███████╗███████╗   ██║       
    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝        ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝       
                                                                                """

tweetText = 'texto de ejemplo'


# New tweet
## Publica un tweet con el texto de la variable 'tweetText'
def new_tweet():
    try:
        api.update_status(tweetText, in_reply_to_status_id=random.randint(0, 1000))
    except Exception as err:
        print(err)


def new_tweet_photo():
    try:
        api.update_status(tweetText, in_reply_to_status_id=random.randint(0, 1000))
        api.update_status_with_media(filename="foto.jpg", status=tweetText,
                                     in_reply_to_status_id=random.randint(0, 1000))

    except Exception as err:
        print(err)


"""
    ██████╗ ███████╗██╗     ███████╗████████╗███████╗    ████████╗██╗    ██╗███████╗███████╗████████╗███████╗     
    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝    ╚══██╔══╝██║    ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝    
    ██║  ██║█████╗  ██║     █████╗     ██║   █████╗         ██║   ██║ █╗ ██║█████╗  █████╗     ██║   ███████╗    
    ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝         ██║   ██║███╗██║██╔══╝  ██╔══╝     ██║   ╚════██║    
    ██████╔╝███████╗███████╗███████╗   ██║   ███████╗       ██║   ╚███╔███╔╝███████╗███████╗   ██║   ███████║    
    ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝       ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝   ╚═╝   ╚══════╝    
                                                                                                            """


# Delete all
## Borra todo el contenido publicado en la cuenta 
def delete():
    for tweet in tweepy.Cursor(api.user_timeline).items():
        api.destroy_status(tweet.id)
        print("delete")


#####################################################
###################### IGNORAR ######################
#####################################################
## esta función se usa al iniciar el programa para recoger el ID del ultimo tweet respondido
def last_reply():
    global lastTweet
    global image
    image = images[randint(1, 5)]
    statuses = []
    for status in tweepy.Cursor(api.user_timeline).items(50):
        if not "RT" in status.text:
            try:
                statuses.append(status)
            except Exception as err:
                print(err)
    i = 0
    while not bool(statuses[i].in_reply_to_status_id):
        i += 1
    lastTweet = statuses[i].in_reply_to_status_id


def nextPhoto():
    global image
    x = image.split("/foto")
    x = x[1].split(".jpeg")
    x = int(x[0])
    x = x % len(images)
    x = x + 1
    x = 'fotos/foto' + str(x) + '.jpeg'
    image = x


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
## con 'schedule' se crea un bucle que se repite cada x tiempo (se introduce cuando se llama a la función, ejemplo más abajo)

def main():
    last_reply() # NO TOCAR

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
        except tweepy.TweepError as e:
            raise e
    
if __name__ == "__main__":
	main()
