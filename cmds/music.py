import discord
from discord.ext import commands
from core.classess import Cog_Extension as CE
import youtube_dl

class music(CE):
    
    @commands.command()
    async def j(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You are not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()     

    @commands.command()
    async def p(self,ctx,url):
        ctx.voice_client.stop() 
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',}  

        YTDL_OPTIONS = {
        'format': 'bestaudio',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
        }

        vc = ctx.voice_client

        
        with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ydl:
            info =  ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
        
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("pause")
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resumee()
        await ctx.send("resume")   
    # @commands.command()
    # async def skip(self,ctx):
    #     if not ctx.voice_state.is_playing
    #     await ctx.voice_client.pause()
    #     await ctx.send("pause")





def setup(bot):
    bot.add_cog(music(bot))
        




# @bot.event
# async def on_ready():
#     print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

# bot.run('Token')