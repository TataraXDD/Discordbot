from discord.ext import commands
from core.classess import Cog_Extension as CE
import re

class nhentai(CE):


    @commands.command()
    async def n(self,ctx,num):
        base_url = "https://nhentai.net/g/"
        rnum = re.compile(r'\d\d\d\d\d\d')
        booknum = rnum.search(num)
        url = base_url+booknum.group()
        await ctx.send(url)









def setup(bot):
    bot.add_cog(nhentai(bot))