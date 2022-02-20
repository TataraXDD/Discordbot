from os import name
from discord.ext import commands
from core.classess import Cog_Extension as CE
import datetime
import json

# with open(r'Github\Discordbot\setting.json','r',encoding='UTF-8') as jfile:
#     jdata = json.load(jfile)
    

class React(CE):

    
    @commands.command()
    async def dounts (self,ctx):
        dount = {
            '1': '🍩',
            '2': '🍩🍩',
            '3': '🍩🍩🍩',
            '4': '🍩🍩🍩🍩',
            '5': '🍩🍩🍩🍩🍩',
            '6': '🍩🍩🍩🍩🍩🍩',
            '7': '🍩🍩🍩🍩🍩🍩🍩'
        }

        wkday = datetime.datetime.today().isoweekday() 

        new_name = dount[f'{wkday}']
        channel = self.bot.get_channel(jdata['hollow_channal']) 
        await channel.edit(name = new_name)
        await ctx.channel.send(f'I want to eat {wkday} dounts >////< {new_name}')


def setup(bot):
    bot.add_cog(React(bot))
