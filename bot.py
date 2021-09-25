
import discord
import random

client = discord.Client()

bad_words = ["goblog", "goblok", "bangsat", "ngentot", "ngewe", "ngocok", 
            "memek", "kontol","coli", "tolol","ajg", "anj", "bego","tete", "buceng", "bacot", "anjing", "ngentod", "gblg"]

bkp_words = ["porn", "hentai", "sex"]

wibu_words = ["hinata", "wibu", "emilia", "akame", "hanabi", "hyuga","shiritori", "shaqiri", "waifu" ]
    

sad_words = ["sedih", "nangis", "pasrah", "depresi","sakit","pusing", "stress", "marah"]

balasan_sad = ["hahaha mending mati aja!!", "mampus lu ajg!!","hahaha mampus!!!", "lu tolol sih"]

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('TiTiT!'))
    print('bot is ready')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('putra'):
        await message.channel.send('putra goblog')
    if any(word in message.content for word in bkp_words):
        await message.channel.send ('tobatlah wahai manusia')
    if any(word in message.content for word in bad_words):
        await message.channel.send ('jangan ngomong kasar')
    if any(word in message.content for word in wibu_words):
        await message.channel.send ('awas ada wibuu lari!!!')
    
    if any(word in message.content for word in sad_words):
        await message.channel.send (random.choice(balasan_sad))

client.run('ODQ5MjkxMzk2NDUxNDAxODU5.YLZCPw.RzzpEWMF85R26d7ZQ-nLTddz1eA')
