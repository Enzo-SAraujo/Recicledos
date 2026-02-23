import discord
from discord.ext import commands
import random
import os
import requests
# Certifique-se que este arquivo existe no mesmo diretório
# from transmissor_recicledos import ClienteSecundario 

description = 'Bot de exemplo para construção de brinquedos.'
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logado como {self.user} (ID: {self.user.id})')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('?brinquedos'):
            await message.reply('Bem-vindo! Esse é um bot de construção de brinquedos recicláveis!', mention_author=True)
            # Nota: Evite instanciar outros clientes/loops aqui dentro se eles forem bloqueantes.
            #cliente = ClienteSecundario()
            #cliente.iniciar()

client = MyClient(intents=intents)
client.run('TOKEN')
