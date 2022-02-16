import discord
from discord.ext import commands
from discord.ext.commands.bot import Bot
import os
import json

mytoken = os.environ.get('TOKEN')
verfy1 = os.environ.get('verfy1')


<<<<<<< HEAD
with open('setting.json','r',encoding='UTF-8') as jfile:
    jdata = json.load(jfile)
=======
# with open('setting.json','r',encoding='UTF-8') as jfile:
#     jdata = json.load(jfile)
>>>>>>> e8f0596534cd8135abd99b18231f6e72b6b376da

bot = commands.Bot(command_prefix='[', intents = discord.Intents.all())

for filename in os.listdir(r'D:\Vscode\Github\Discordbot\cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.event
async def on_ready():
    activity = discord.Game(name="و(*`▽´)٩")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(">>Bot is online<<")

@bot.command()
async def load(ctx,ext,verfy : str = None):
    if verfy == verfy1 :
        bot.load_extension(f'cmds.{ext}')
        await ctx.send(f'Load{ext} success.')
    elif verfy == None:
        await ctx.send('Who are you! ')
    else :
        await ctx.send('You are not Tatar, go away! 	(ﾒ｀ﾛ´)/')

@bot.command()
async def unload(ctx,ext,verfy : str = None):
    if verfy == verfy1 :
        bot.unload_extension(f'cmds.{ext}')
        await ctx.send(f'Unload{ext} success.')
    elif verfy == None:
        await ctx.send('Who are you! ')
    else :
        await ctx.send('You are not Tatar, go away! 	(ﾒ｀ﾛ´)/')

@bot.command()
async def reload(ctx,ext,verfy : str = None):
    if verfy == verfy1 :
        bot.reload_extension(f'cmds.{ext}')
        await ctx.send(f'ReLoad{ext} success.')
    elif verfy == None:
        await ctx.send('Who are you! ')
    else :
        await ctx.send('You are not Tatar, go away! 	(ﾒ｀ﾛ´)/')
    

if __name__ ==  "__main__":
<<<<<<< HEAD
    bot.run(mytoken)
=======
    bot.run('NzY5MjE0OTYxNjYyNTU4MjE4.X5LxQg.CEV9xVfwJNM_-AzC88Pc7aHd7dM')
>>>>>>> e8f0596534cd8135abd99b18231f6e72b6b376da



































# @bot.event
# async def on_menber_join(menber):
#     channal = bot.get_channal(int(jdata['hollow_channal']))
#     await channal.send(f'{member}join!')
