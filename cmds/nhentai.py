from discord.ext import commands
from core.classess import Cog_Extension as CE

class nhentai(CE):


    @commands.command()
    async def n(self,ctx):
        base_url = "https://nhentai.net/g/"
        await ctx.send("base_ur/l"+ctx)