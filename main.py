import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logado como {bot.user}')

@bot.command()
async def brinquedos(ctx):
    etapas = [
        {
            "titulo": "Apresentação",
            "descricao": "Bem-vindo! Vamos montar um avião motorizado.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/aviao-palitodesorvete.png-1-400x300.png"
        },
        {
            "titulo": "Materiais necessários",
            "descricao": "• 3 palitos de sorvete\n• 1 palito de madeira\n• 2 rodinhas\n• 1 motorzinho\n• 2 pilhas\n• 1 botão liga/desliga\n• Fios\n• Abraçadeiras\n• 1 suporte de pilhas\n• 1 hélice\n• Cola, fita e tesoura",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/aviao-motorizado-800x1298.webp"
        },
        {
            "titulo": "Etapa 1",
            "descricao": "O motor é o coração do avião. Ele gira a hélice para impulsionar o brinquedo. Teste-o antes de montar!",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/ligacao-motor-pilhas-fabricadebrinquedos-600x600.webp"
        },
        {
            "titulo": "Etapa 2",
            "descricao": "O suporte de pilhas é onde as pilhas serão inseridas para alimentar o motor. Ele geralmente tem espaço para duas pilhas. Certifique-se de que o suporte esteja limpo e sem corrosão.",
            "imagem": "https://cdn.awsli.com.br/800x800/2599/2599375/produto/21641961083e11b94b1.jpg"
        }, # Chave fechada aqui
        {
            "titulo": "Etapa 3",
            "descricao": "O botão liga/desliga é essencial para controlar o motor. Ele permite ligar e desligar o motor conforme necessário. Certifique-se de que o botão esteja funcionando e bem fixado.  Os fios conectam o motor ao suporte de pilhas e ao botão liga/desliga. Use fios de cores diferentes para facilitar a identificação",
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROf5OdthdLrywA613ZHR5cgYHR8nL8_FZuMA&s"
        }, # Chave fechada aqui
        {
            "titulo": "Etapa 4",
            "descricao": "Comece posicionando um pedaço de palito de sorvete para determinar a distância entre as rodas dianteiras. Você precisará de duas peças com cerca de 4 cm cada. Use as duas pontas do palito de sorvete para aproveitar o formato arredondado do corte.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/1-1-826x464.webp"
        }, # Chave fechada aqui
        {
            "titulo": "Etapa 5",
            "descricao": "Depois de definir os espaços, faça furos nas pontas dos palitos (peça ajuda de um adulto). Isso permitirá que você una as duas partes com fita adesiva.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/2-1-826x464.webp"
        }, # Chave fechada aqui
        {
            "titulo": "Etapa 6",
            "descricao": "Corte um pedaço de palito de churrasco com 4 cm de comprimento. Verifique se os furos têm espaço suficiente para a passagem do palito, com um pouco de folga para não atrapalhar o movimento das rodas.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/4-1-826x464.webp"
        }, # Chave fechada aqui
        {
            "titulo": "Etapa 7",
            "descricao": "Cole a asa traseira na estrutura, conforme mostrado na foto.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/5-1-826x464.webp"
        }, # Chave fechada aqui
        {
            "titulo": "Etapa 8",
            "descricao": "Reforce a fixação da asa traseira com fita crepe.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/6d-1-826x464.webp"
        }, # Chave fechada aqui
        {
            "titulo": "Etapa 9",
            "descricao": "Pinte a estrutura do avião. A asa dianteira também pode ser pintada separadamente.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/7b-1-826x464.webp"
        },
        {
            "titulo": "Etapa 10",
            "descricao": "Confira a posição da asa dianteira, deixando espaço para encaixar o motor. Cole a hélice no lugar após verificar a posição correta.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/9-1-826x464.webp"
        },
        {
            "titulo": "Etapa 11",
            "descricao": "Encaixe o motor e prenda-o com uma abraçadeira. Siga o passo a passo para montar o motor, conectando os fios, o suporte das pilhas e o botão liga/desliga.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/10-1-826x464.webp"
        },
        {
            "titulo": "Etapa 12",
            "descricao": "Corte as sobras da abraçadeira.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/11-1-826x464.webp"
        },
        {
            "titulo": "Etapa 13",
            "descricao": "Cole o suporte das pilhas. Você pode usar fita dupla face ou cola quente, mas peça ajuda de um adulto.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/12-1-826x464.webp"
        },
        {
            "titulo": "Etapa 14",
            "descricao": "Prenda o botão liga/desliga com fita crepe colorida.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/13-1-826x464.webp"
        },
        {
            "titulo": "Etapa 15",
            "descricao": "Coloque as pilhas no suporte e teste o motor para verificar se está funcionando corretamente (pode haver pequenas falhas nos encaixes dos fios).",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/14-1-826x464.webp"
        },
        {
            "titulo": "Etapa 16",
            "descricao": "Coloque as rodas conforme mostrado na foto. Se elas começarem a soltar, reforce o encaixe com um pequeno pedaço de fita.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/15-1-826x464.webp"
        },
        {
            "titulo": "Etapa 17",
            "descricao": "Encaixe a hélice na ponta do motor. Tome cuidado para não bloquear o movimento.",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/16-1-826x464.webp"
        },
        {
            "titulo": "Etapa 18",
            "descricao": "Faça mais um teste do motor com a hélice, para ver se está girando corretamente. Ela não pode ficar solta, senão \"sai voando sozinha\". Se estiver tudo certo, é só brincar. Está pronto!",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/17-1-826x464.webp"
        },
        # ... (mantenha as outras etapas aqui)
        {
            "titulo": "Vídeo tutorial",
            "descricao": "Assista aqui: https://youtu.be/bQEfrUVI7PY",
            "imagem": "https://www.fabricadebrinquedos.com.br/assets/images/aviao-palitodesorvete.png-1-400x300.png"
        }
    ]

    for etapa in etapas:
        embed = discord.Embed(
            title=etapa["titulo"],
            description=etapa["descricao"],
            color=discord.Color.green()
        )
        embed.set_image(url=etapa["imagem"])
        # CORREÇÃO: Enviar o embed de fato
        await ctx.send(embed=embed)

# Iniciar o bot fora de qualquer classe para simplificar
bot.run('TOKEN')
