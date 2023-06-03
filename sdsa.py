import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot olarak giriş yapıldı: {bot.user.name}')

@bot.event
async def on_voice_state_update(member, before, after):
    if member.id == 707329534600675329:
        if before.channel != after.channel:
            if after.channel is not None:  # Kullanıcı bir ses kanalına katıldıysa
                current_channel_id = 1113896222852395028
                current_channel = bot.get_channel(current_channel_id)
                target_channel_id = 1114488605755326514  # Değiştirmeniz gereken kısım
                target_channel = bot.get_channel(target_channel_id)
                if current_channel:
                    await member.move_to(target_channel)

bot.run('MTExNDE0NjQ2ODUxMzcyMjM4OQ.GhU2R8.wY3Uw7C0OCnHXQt2SJUKPL17vUULlmBWOCiOPU')  # Değiştirmeniz gereken kısım
