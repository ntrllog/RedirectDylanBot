import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name='Redirecting messages'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.id == process.env.SENDER_ID:
        channel = client.get_channel(process.env.CHANNEL_ID)
        await channel.send(message.content)
        await message.delete()

client.run(process.env.CLIENT_TOKEN)
