import discord, os, keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name='Redirecting messages'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.id == int(os.getenv('SENDER_ID')):
        channel = client.get_channel(int(os.getenv('CHANNEL_ID')))
        await channel.send(message.content)
        await message.delete()

keep_alive.keep_alive()

client.run(os.getenv('CLIENT_TOKEN'))
