# Arcadia Chatbot : Python Edition
A chatbot for Twitch streamers powered by TwitchIO and Python
# ES:
 Chatbot para streamers de twich, creado  por TwitchlO y Python. 

# ¿Que es y para que sirve un chatbot?
 Chatbot es un bot que te permite gestionar y moderar las salas de chat. Este bot también facilita el trabajo de los streamers, puesto que permiten saludar a los nuevos subscriptores, al igual que mandar algunos mensajes programados.

# How to run this project
 Lo primero de todo, necesitas instalar las dependencias usando poetry:

 ```shell
 poetry install
 ```
 Después, ejecuta el main script con el siguiente comando:

 ```shell
 poetry run python src/main.py
 ```

 o

 ```shell
 poetry shell
 python src/main.py
 ```
 Una vez instalado el bot, dentro de la cuenta de twitch te va a pedir el nombre de la cuenta en la que lo vas a usar como bot. Después introduce el token que se consigue en la web: https://twitchapps.com/tmi/

First of all, you need to install the dependencies using [poetry](https://python-poetry.org/):
# ¿Como usar los comandos?
 Las comandos se utilizan poniendo: !(función).
 Algunos ejemplos son:
 !cita ; !Hola ; !hola ; !dado ...(etc). Más comandos e información sobre ellos se encuentran en el archivo arcadia.py

# ¿Como puedes aportar a este repo?
 Para ayudar o aportar a este repo usted puede mirar los issues en los que puedes ayudar o trabajar. Asimismo, si en este proyecto se ve algún error o mejora se puede mandar un pull request con esas mejoras.
 En el archivo citas.txt puedes introducir algunas frases "celebres" o graciosas para que el bot los pueda escribir.
 Si eres streamer, pon tu canal en el archivo "Streamers.txt".

# EN:
 A chatbot for Twitch streamers TwitchIO and Python

# What is Chatbot and which is its function?
 Chatbot is a bot which allows you to moderate chat's room. This bot make easer streamers work, because it provides you with schedule messages,for example greeting the new subs. 

# How to run this project
 First of all, you need to install the dependencies using poetry:
 ```
 poetry shell
 python src/main.py
 ```
 Next, you can run the main script with the following command:
 ```shell
 poetry run python src/main.py
 ```

```shell
poetry install
```
 or

Next, you can run the main script with the following command:
 ```shell
 poetry shell
 python src/main.py
 ```

```shell
poetry run python src/main.py
```
 Once the bot is installed. When you're into your Twitch account, it is going to ask you the name of the account in which you'll use it. Then, you have to introduce a token. You can get it in the web: https://twitchapps.com/tmi/

or

```shell
poetry shell
python src/main.py
```
# How can you help in this repo?
 You can help in this repo looking the open issues. Moreover, if in the project you see errors, or things that you can improve, do a pull request with these improvements.
 In citas.txt you can put some famous or funny phrases, so that the bot can write them.
 If you are a streamer, write your channel in the file "Streamers.txt"
