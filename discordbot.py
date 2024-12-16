import discord

# 必要な intents を設定
intents = discord.Intents.all()  # すべての意図を有効化
# または、特定の意図だけ有効化する場合:
# intents = discord.Intents.default()
# intents.messages = True
# intents.guilds = True

# Client に intents を渡す
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('すねげ'):
        while(1):
       	 await message.channel.send('すねげ')

# Bot のトークンで実行
client.run('TOKEN')
