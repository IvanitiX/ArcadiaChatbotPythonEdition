from re import split
from dotenv import load_dotenv
import os
import random
from twitchio.ext import commands
from twitchio.ext.commands.core import command
from TextParser import TextParser
import time


class Arcadia(commands.Bot):

    TiempoAnterior = 0
    Tiempo = 0

    def __init__(self) -> None:
        self.parser = TextParser()

        load_dotenv()
        if os.getenv("BOT_USERNAME") is None:
            print("[>>] Introduce el nombre de tu cuenta bot:\n")
            cuenta = input(">> : ")
            with open(".env", "a") as entorno:
                entorno.write(f"\nBOT_USERNAME={cuenta}")

        if os.getenv("OAUTH_TOKEN") is None:
            print(
                "[>>] Introduce el token de tu cuenta bot (entra a esta página: https://twitchapps.com/tmi/ ):\n"
            )
            token = input(">> : ")
            with open(".env", "a") as entorno:
                entorno.write(f"\nOAUTH_TOKEN={token}")

        """
        Se carga desde un archivo de entorno los parámetros del bot (usuario, token y archivos de streamer y de citas).
        El token se genera en la página https://twitchapps.com/tmi/
        """
        load_dotenv()
        self.config = {
            "username": os.getenv("BOT_USERNAME"),
            "password": os.getenv("OAUTH_TOKEN"),
            "channels": self.parser.parseChannels(os.getenv("STREAMERS_FILE")),
            "quotes": self.parser.parseQuotes(os.getenv("QUOTES_FILE")),
        }

        super().__init__(
            token=self.config["password"],
            prefix="!",
            initial_channels=self.config["channels"],
        )

    def saludar(self, ctx: commands.Context):
        return f"Hola {ctx.author.display_name}, ¿qué tal?"

    def randomizarNumero(self, max):
        return self.randomizarNumeroArray(max - 1) + 1

    def randomizarNumeroArray(self, max):
        return random.randint(0, max)

    async def event_ready(self):
        print(f">> {self.nick} ha entrado al chat")

    """
    Función hola:
    Esta función saluda al usuario que invoca el comando.
    """

    @commands.command()
    async def hola(self, ctx: commands.Context):
        await ctx.send(self.saludar(ctx))

    """
    Función Hola:
    Es la misma función que hola pero con la hache mayúscula.
    """

    @commands.command()
    async def Hola(self, ctx: commands.Context):
        await ctx.send(self.saludar(ctx))

    """
    Función dado:
    Esta función muestra un número entre uno y seis.
    """

    @commands.command()
    async def dado(self, ctx: commands.Context):
        lados = 6
        numero = self.randomizarNumero(lados)
        await ctx.send(
            f"/me {ctx.author.display_name}, has sacado un {numero} en el dado"
        )

    """
    Funcion examen:
    Esta funcion necesita una asignatura como argumento, si no se introduce, la pide de nuevo.
    Devuelve una nota del 1 al 10 junto con el nombre de la asignatura.
    """

    @commands.command()
    async def examen(self, ctx: commands.Context):
        if ctx.message.content != "!examen":
            asignatura = split(string=ctx.message.content, pattern=" ", maxsplit=1)
            notaMax = 10
            nota = self.randomizarNumero(notaMax)
            await ctx.send(
                f"/me {ctx.author.display_name} , vas a sacar un {nota} en el examen de {asignatura[1]}"
            )
        else:
            await ctx.send(
                f"/me {ctx.author.display_name} , necesito que me digas de qué asignatura es ese examen"
            )

    """
    Función coinflip:
    Esta función simula el tirar una moneda, muestra por el chat si ha salido cara o cruz.
    """

    @commands.command()
    async def coinflip(self, ctx: commands.Context):
        caras = 2
        caraFinal = self.randomizarNumeroArray(caras)

        if caraFinal == 0:
            await ctx.send(f"/me {ctx.author.display_name}, has sacado cara")
        if caraFinal == 1:
            await ctx.send(f"/me {ctx.author.display_name}, has sacado cruz")

    """
    Función dollars:
    La función muestra el mensaje de abajo en el chat.
    """

    @commands.command()
    async def dollars(self, ctx: commands.Context):
        await ctx.send("/me Dollars, chavales, DOOOOOLLARSSS!")

    """
    Función help:
    Envía por susurro una lista de los comandos que se pueden ejecutar.
    """

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send(
            f"""/w {ctx.author.display_name} 
        Los comandos disponibles son:
        !hola Recibes un saludo del bot en el chat.
        !coinflip Lanzas una moneda al aire, puede salir cara o cruz.
        !dado Lanzas un dado y sale un número entre 1 y 6.
        !examen Pide una asignatura y te dice qué nota sacarás en ese examen.
        !dollars ¿Por qué no lo pruebas?
        !arcadia El bot se presenta.
        !amor Te dice el porcentaje de amor que tienes con la persona que le digas.
        """
        )

        await ctx.send(
            f"""/w {ctx.author.display_name}
        !duelo Relata un duelo entre tú y la persona que menciones.
        !citar Guarda en una lista las frases que le digas.
        !cita Elige entre tus citas una aleatoria y te la dice.
        """
        )

    """
    Función arcadia:
    La función muestra el mensaje de abajo en el chat (una presentación del bot).
    """

    @commands.command()
    async def arcadia(self, ctx: commands.Context):
        await ctx.send(
            "/me ¡Hola, soy Arcadia! Soy una IA que interactúa con vosotros en los chats de Twitch"
        )

    """
    Funcion amor:
    La función pide el nombre de el o la amante, si no se introduce, lo pide.
    Esta función genera un numero aleatorio entre 1 y 100 que equivale al nivel de amor,
    a continuación genera un número entre uno y cinco para elegir uno de los cinco mensajes
    y muestra el mensaje elegido junto al nivel de amor.
    """

    @commands.command()
    async def amor(self, ctx: commands.Context):
        if ctx.message.content != "!amor":
            amante = split(string=ctx.message.content, pattern=" ", maxsplit=1)
            amorMax = 100
            amor = self.randomizarNumero(amorMax)

            totalMensajes = 5
            mensaje = self.randomizarNumero(totalMensajes)

            if mensaje == 1:
                await ctx.send(
                    f"/me {ctx.author.display_name} , hay un {amor}% de probabilidades de que {amante[1]} te ame en secreto"
                )
            if mensaje == 2:
                await ctx.send(
                    f"/me {ctx.author.display_name} , hay un {amor}% de probabilidades de que {amante[1]} te busque por Tinder"
                )
            if mensaje == 3:
                await ctx.send(
                    f"/me {ctx.author.display_name} , hay un {amor}% de probabilidades de que {amante[1]} y tú acabéis en el cuarto"
                )
            if mensaje == 4:
                await ctx.send(
                    f"/me {ctx.author.display_name} , hay un {amor}% de probabilidades de que {amante[1]} esté rehorny por ti"
                )
            if mensaje == 5:
                await ctx.send(
                    f"/me {ctx.author.display_name} , hay un {amor}% de probabilidades de que {amante[1]} te diga que sí si se lo propones."
                )
        else:
            await ctx.send(
                f"/me {ctx.author.display_name} , necesito que me digas quién es el minito o la muchacha"
            )

    """
    Funcion citar:
    Esta función pide como argumento una frase (la cita que se quiere guardar).
    La función guarda en un documento de texto las citas de los usuarios junto con sus nicks.
    """

    @commands.command()
    async def citar(self, ctx: commands.Context):
        cita = split(string=ctx.message.content, pattern=" ", maxsplit=1)[1]
        with open(os.getenv("QUOTES_FILE"), "a") as archivoCitas:
            archivoCitas.write(f"\n{cita} - Citado por {ctx.author.display_name}")
        self.config["quotes"] = self.parser.parseQuotes(os.getenv("QUOTES_FILE"))
        await ctx.send(f"La cita ha sido guardada con éxito")

    """
    Funcion cita:
    Busca en el archivo de texto una cita aleatoria (si la hay) y la muestra por el chat,
    si no hay ninguna cita de ese usuario le propondrá crear una.
    """

    @commands.command()
    async def cita(self, ctx: commands.Context):
        numeroCitas = len(self.config["quotes"]) - 1
        if numeroCitas > 0:
            cita = self.randomizarNumeroArray(numeroCitas)
            cita = self.config["quotes"][cita]
            await ctx.send(f"/me {cita}")
        else:
            await ctx.send(
                f"/me No hay citas -  Pero puedes animarte a ponerlas con !citar <Algo>"
            )

    """
    Funcion Duelo:
    Duela a la persona mencionada en el chat y relata la pelea.
    Necesita como argumento el nombre del retado.
    """

    def victoria(self, atacante, defensor):
        enviar = self.randomizarNumeroArray(4)
        if enviar == 1:
            return f"/me {atacante} ha golpeado a {defensor} con la fuerza de un gorila africano."
        elif enviar == 2:
            return f"/me {atacante} ha conseguido impactar un derechazo a {defensor} que le deja temblando."
        elif enviar == 3:
            return f"/me {atacante} lanza un puño hacia la cara de {defensor} que le salta varios dientes."
        elif enviar == 4:
            return f"/me {atacante} hace un barrido a {defensor} tirándole sin miramientos contra el suelo."
        elif enviar == 0:
            return f"/me {atacante} deja la marca de su mano en la cara de {defensor} tras un manotazo."

    def derrota(self, atacante, defensor):
        enviar = self.randomizarNumeroArray(4)
        if enviar == 1:
            return f"/me {defensor} ha fallado su ataque contra {atacante}."
        elif enviar == 2:
            return f"/me {defensor} esquiva con facilidad el ataque de {atacante} ."
        elif enviar == 3:
            return f"/me {defensor} da un salto hacia atrás, lejos del rango de {atacante} ."
        elif enviar == 4:
            return f"/me {defensor} consigue correr lejos de {atacante} antes de que le golpee."
        elif enviar == 0:
            return f"/me {defensor} recibe el golpe de {atacante} pero es tan débil que ni lo nota..."

    @commands.command()
    async def duelo(self, ctx: commands.Context):

        if (round(time.time()) - self.TiempoAnterior) >= 60:
            if ctx.message.content != "!duelo":
                contrincante = split(
                    string=ctx.message.content, pattern=" ", maxsplit=1
                )
                await ctx.send(
                    f"/me Atención, {ctx.author.display_name} ha retado a un duelo a {contrincante[1]}, preparense."
                )
                ataque = self.randomizarNumeroArray(1)
                contrataque = self.randomizarNumeroArray(1)
                duelista1 = 0
                duelista2 = 0

                await ctx.send(f"/me Ataque: ")
                if ataque == 0:
                    await ctx.send(
                        self.victoria(ctx.author.display_name, contrincante[1])
                    )
                    duelista1 += 1
                elif ataque == 1:
                    await ctx.send(
                        self.derrota(ctx.author.display_name, contrincante[1])
                    )

                await ctx.send(f"/me Contraataque: ")
                if contrataque == 0:
                    await ctx.send(
                        self.victoria(contrincante[1], ctx.author.display_name)
                    )
                    duelista2 += 1
                elif contrataque == 1:
                    await ctx.send(
                        self.derrota(contrincante[1], ctx.author.display_name)
                    )

                if duelista1 > duelista2:
                    await ctx.send(
                        f"/me {ctx.author.display_name} es el ganador de este duelo"
                    )
                elif duelista1 < duelista2:
                    await ctx.send(f"/me {contrincante[1]} es el ganador de este duelo")
                else:
                    await ctx.send(
                        f"/me Al parecer se han tumbado el uno al otro... ¡Doble KO!"
                    )
                self.TiempoAnterior = round(time.time())
            else:
                await ctx.send(
                    f"/me No puedes retar a todo el chat, necesito que digas a quien quieres enfrentarte."
                )
