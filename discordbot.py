import discord
import os
import openai
from openai import OpenAI
import time

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
def GPT_INPUT( input):
	try:
		messages = client.chat.completions.create(
    		messages=[
        		{
            		"role": "user",
            		"content": "やっほー",
        		}
    		],
    		model="gpt-4o-mini",
		)
	except openai.error.RateLimitError:
		print("リクエスト数の上限に達しました。少し待って再試行します。")
		time.sleep(20)  # 20秒待機
		messages = client.chat.completions.create(
        	messages=[
        		{
            		"role": "user",
            		"content": "やっほー",
        		}
    		],
    		model="gpt-4o-mini",
		)
    
# print(messages.choices[0].message.content)
# response = opena
# i.Model.list()
# print(response)
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

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith(''):
#        	 await message.channel.send(messages)

# @client.event

async def gpt_response(message):
    if message.author == client.user:
        return
    if message.content.startswith('gpt'):
        print('GPTを起動しました。プロンプトを入力してください')
        

# Bot のトークンで実行
client.run('TOKEN')
