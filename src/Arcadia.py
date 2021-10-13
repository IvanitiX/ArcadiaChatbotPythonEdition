from re import split
from dotenv import load_dotenv
import os
import random
from twitchio.ext import commands
from twitchio.ext.commands.core import command
from TextParser import TextParser

class Arcadia(commands.Bot):

    def __init__(self) -> None:
        self.parser = TextParser()

        load_dotenv()
        if (os.getenv('BOT_USERNAME') is None):
            print("[>>] Introduce el nombre de tu cuenta bot:\n")
            cuenta = input(">> : ")
            with open(".env","a") as entorno:
                entorno.write(f"\nBOT_USERNAME={cuenta}")

        if (os.getenv('OAUTH_TOKEN') is None):
            print("[>>] Introduce el token de tu cuenta bot (entra a esta página: https://twitchapps.com/tmi/ ):\n")
            token = input(">> : ")
            with open(".env","a") as entorno:
                entorno.write(f"\nOAUTH_TOKEN={token}")

        load_dotenv()
        self.config = {
            'username' : os.getenv('BOT_USERNAME'),
            'password' : os.getenv('OAUTH_TOKEN'),
            'channels' : self.parser.parseChannels(os.getenv('STREAMERS_FILE')),
            'quotes' : self.parser.parseQuotes(os.getenv('QUOTES_FILE'))
        }



        super().__init__(token=self.config['password'], prefix='!', initial_channels=self.config['channels'])
    

    def saludar(self, ctx: commands.Context):
        return f'Hola {ctx.author.display_name}, ¿qué tal?'

    def randomizarNumero(self, max):
        return self.randomizarNumeroArray(max - 1) + 1

    def randomizarNumeroArray(self, max):
        return random.randint(0,max)

    async def event_ready(self):
        print(f'>> {self.nick} ha entrado al chat')

    @commands.command()
    async def hola(self, ctx: commands.Context):
        await ctx.send(self.saludar(ctx))

    @commands.command()
    async def Hola(self, ctx: commands.Context):
        await ctx.send(self.saludar(ctx))

    @commands.command()
    async def dado(self, ctx: commands.Context):
        lados = 6
        numero = self.randomizarNumero(lados)
        await ctx.send(f'/me {ctx.author.display_name}, has sacado un {numero} en el dado')

    @commands.command()
    async def examen(self, ctx: commands.Context):
        if(ctx.message.content != "!examen"):
            asignatura = split(string=ctx.message.content,pattern=" ",maxsplit=1)
            notaMax = 10
            nota = self.randomizarNumero(notaMax)
            await ctx.send(f'/me {ctx.author.display_name} , vas a sacar un {nota} en el examen de {asignatura[1]}')
        else:
            await ctx.send(f'/me {ctx.author.display_name} , necesito que me digas de qué asignatura es ese examen')

    @commands.command()
    async def coinflip(self, ctx: commands.Context):
        caras = 2
        caraFinal = self.randomizarNumeroArray(caras)

        if(caraFinal == 0):
            await ctx.send(f'/me {ctx.author.display_name}, has sacado cara')
        if(caraFinal == 1):
            await ctx.send(f'/me {ctx.author.display_name}, has sacado cruz')

    @commands.command()
    async def dollars(self, ctx: commands.Context):
        await ctx.send('/me Dollars, chavales, DOOOOOLLARSSS!')

    @commands.command()
    async def arcadia(self,ctx: commands.Context):
        await ctx.send('/me ¡Hola, soy Arcadia! Soy una IA que interactúa con vosotros en los chats de Twitch')

    @commands.command()
    async def amor(self, ctx: commands.Context):
        if(ctx.message.content != "!amor"):
            amante = split(string=ctx.message.content,pattern=" ",maxsplit=1)
            amorMax = 100
            amor = self.randomizarNumero(amorMax)

            totalMensajes = 5
            mensaje = self.randomizarNumero(totalMensajes)

            if(mensaje == 1):
                await ctx.send(f'/me {ctx.author.display_name} , hay un {amor}% de probabilidades de que {amante[1]} te ame en secreto')
            if(mensaje == 2):
                await ctx.send(f'/me {ctx.author.display_name} , hay un {amor}% de probabilidades de que {amante[1]} te busque por Tinder')
            if(mensaje == 3):
                await ctx.send(f'/me {ctx.author.display_name} , hay un {amor}% de probabilidades de que {amante[1]} y tú acabéis en el cuarto')
            if(mensaje == 4):
                await ctx.send(f'/me {ctx.author.display_name} , hay un {amor}% de probabilidades de que {amante[1]} esté rehorny por ti')
            if(mensaje == 5):
                await ctx.send(f'/me {ctx.author.display_name} , hay un {amor}% de probabilidades de que {amante[1]} te diga que sí si se lo propones.')
        else:
            await ctx.send(f'/me {ctx.author.display_name} , necesito que me digas quién es el minito o la muchacha')

        
    @commands.command()
    async def citar(self,ctx: commands.Context):
        cita = split(string=ctx.message.content,pattern=" ",maxsplit=1)[1]
        with open(os.getenv('QUOTES_FILE'),'a') as archivoCitas:
            archivoCitas.write(f"\n{cita} - Citado por {ctx.author.display_name}")
        self.config['quotes'] = self.parser.parseQuotes(os.getenv('QUOTES_FILE'))
        await ctx.send(f"La cita ha sido guardada con éxito")

    @commands.command()
    async def cita(self,ctx: commands.Context):
        numeroCitas = len(self.config['quotes']) - 1
        if(numeroCitas > 0):
            cita = self.randomizarNumeroArray(numeroCitas)
            cita = self.config['quotes'][cita]
            await ctx.send(f"/me {cita}")
        else:
            await ctx.send(f"/me No hay citas -  Pero puedes animarte a ponerlas con !citar <Algo>")



