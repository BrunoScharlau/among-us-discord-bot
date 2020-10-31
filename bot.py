import discord
from discord.ext import commands
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

commands_channel_id = int(config["discord"]["commands_channel_id"]) 
voice_chat_id = int(config["discord"]["voice_chat_id"]) #YOUR VOICE CHAT ID


client = commands.Bot(command_prefix = ".")

def in_channel(channel_id):
    def predicate(ctx):
        return ctx.message.channel.id == channel_id
    return commands.check(predicate)

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
@in_channel(commands_channel_id)
async def mute(ctx):
    channel = client.get_channel(voice_chat_id)
    for member in channel.members:
        await member.edit(mute=True)

    embed = discord.Embed(title = "Muted", color= 0xff0000)
    embed.add_field(name="Muted "+ channel.name, value="You can now kill in peace.")
    
    await ctx.send(embed =embed)


@client.command()
@in_channel(commands_channel_id)
async def unmute(ctx):
    channel = client.get_channel(voice_chat_id)
    for member in channel.members:
        await member.edit(mute=False)

        
    embed = discord.Embed(title = "Unmuted", color= 0x00ff00)
    embed.add_field(name="Unmuted "+ channel.name, value="Time to talk")

    await ctx.send(embed=embed)

client.run(config["bot"]["id"])