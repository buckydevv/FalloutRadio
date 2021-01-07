import discord, os, json, youtube_dl, random, asyncio
from discord.ext import commands
from discord.utils import get
from pathlib import Path


client = commands.Bot(command_prefix="f.")
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the sun set on the Wasteland"))
    print("------------------------------------\n           Bot is Running: \n------------------------------------")
    print("Name: {}\n".format(client.user.name))
    print("ID: {}\n".format(client.user.id)) 


#f.xhiro
@client.command()
async def xhiro(ctx):
    await ctx.send("""Ohhhh Xhiro Lay your hands on me while I'm bleeding dry :musical_note:
Break on through blue skies, I'll take you higher, higher than ever before
I’m Caught up in circles
All dreams and bright lights
Wait I'm here always, brighter than sunshine
To Xhiro I fly
Fly out
Fly out to your heart :heart:
Fly out
Fly out
Lay your hands on me
Oh xhiro Stay close by my side
Drive me so crazy
Moonlight and star shine
Faded into the setting sun :sunny:
I'll see you again I'll carry on
Feeling like I'm floating leaves in the fleeting sky :milky_way:
You can sing that song
Let it go
Move on
Let's go way out
Spaced out
Spaced out
Lay your hands on me xhiro stay close to my eyes
Drive me so crazy
Wake up in your arms can’t even tell you how I feel
oh xhiro making me act up,
oh xhiro why you gotta tug my heart :heart:
don’t make me pout lovin you is like livin free
but when they say we aren’t meant to be
ima just have to disagree
You play with my heart I don’t mind
I’ll fake it pretend I’m blind
I don’t even care
when I’m with you it all melts away
Maybe someday I’ll see what’s really going on
but I don’t want to see what’s really happening.
As long as your by my side
I’ll just let it all slide
oh xhirooooo :smiling_face_with_3_hearts::musical_note:""")

#f.ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Radio Strength: {round(client.latency * 1000)}ms')

#f.play
@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


#f.leave
@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await ctx.send("You've Tuned Out")
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

#f.skip
@client.command()
async def skip(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

#f.DiamondCity
@client.command()
async def diamondcity(ctx):
    guild = ctx.guild
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("Tuning in to Diamond City Radio!")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    mp3_path = "D:\\Bot\\4.DiamondCity"
    exc_path = "C:\\Users\\range\\Desktop\\DiscordBot\\ffmpeg\\bin\\ffmpeg.exe"
    path = "D:\\Bot\\4.DiamondCity"
    files=os.listdir(path)

    for _ in os.listdir(path):
        d = random.choice(files)

        if not voice.is_playing():
            print(f"Playing \"{d}\"")
            voice.play(
                discord.FFmpegPCMAudio(
                    executable=exc_path,
                    source=os.path.join(mp3_path, d)
                )
            )

        while voice.is_playing():
            await asyncio.sleep(0.25)

#f.Applachia
@client.command()
async def applachia(ctx):
    guild = ctx.guild
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("Tuning in to Applachian Radio!")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    mp3_path = "D:\\Bot\\76.applachia"
    exc_path = "C:\\Users\\range\\Desktop\\DiscordBot\\ffmpeg\\bin\\ffmpeg.exe"
    path = "D:\\Bot\\76.applachia"
    files=os.listdir(path)

    for _ in os.listdir(path):
        d = random.choice(files)

        if not voice.is_playing():
            print(f"Playing \"{d}\"")
            voice.play(
                discord.FFmpegPCMAudio(
                    executable=exc_path,
                    source=os.path.join(mp3_path, d)
                )
            )

        while voice.is_playing():
            await asyncio.sleep(0.25)

#f.fallout2
@client.command()
async def fallout2(ctx):
    guild = ctx.guild
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("Tuning in to the fallout 2 Radio!")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    mp3_path = "D:\\Bot\\fallout.2"
    exc_path = "C:\\Users\\range\\Desktop\\DiscordBot\\ffmpeg\\bin\\ffmpeg.exe"
    path = "D:\\Bot\\fallout.2"
    files=os.listdir(path)

    for _ in os.listdir(path):
        d = random.choice(files)

        if not voice.is_playing():
            print(f"Playing \"{d}\"")
            voice.play(
                discord.FFmpegPCMAudio(
                    executable=exc_path,
                    source=os.path.join(mp3_path, d)
                )
            )

        while voice.is_playing():
            await asyncio.sleep(0.25)

#f.gnr
@client.command()
async def Applachia(ctx):
    guild = ctx.guild
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("Tuning in to Galaxy News Radio Radio!")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    mp3_path = "D:\\Bot\\76.applachia"
    exc_path = "C:\\Users\\range\\Desktop\\DiscordBot\\ffmpeg\\bin\\ffmpeg.exe"
    path = "D:\\Bot\\76.applachia"
    files=os.listdir(path)

    for _ in os.listdir(path):
        d = random.choice(files)

        if not voice.is_playing():
            print(f"Playing \"{d}\"")
            voice.play(
                discord.FFmpegPCMAudio(
                    executable=exc_path,
                    source=os.path.join(mp3_path, d)
                )
            )

        while voice.is_playing():
            await asyncio.sleep(0.25)




#help
client.remove_command("help")
@client.command(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Use f.help <command> for extended help **(type f.stations for a list of stations)**", color = ctx.author.color)
    em.add_field(name = "**Commands**", value = "Admin commands:\n `ping`  - shows bots latency\n `kick`  - kicks a user\n `snipe`  - shows last deleted message\n `ban`  - bans a member\n `unban` unbans a member\n  ")
    await ctx.send(embed = em)

@client.group()
async def stations(ctx):
    em = discord.Embed(title = "**Stations**", description = "Use f.station <specifc station> for extended help ", color = ctx.author.color)
    em.set_author(name="Fallout Radio", url="https://github.com/POPE44", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMgmfWEvADJKkzie4Aori3Rvdu-nIlAhqsGg&usqp=CAU")
    em.add_field(name = "__Stations__: ", value = "`Diamond City`\n`Galaxy News Radio:`\n`Fallout 2 Soundtrack`\n`New Vegas (Mojave) Radio`\n`Applachian Radio`\n`Classical Radio`\n ")
    em.add_field(name = "Example ", value = "```f.stations GalaxyNewsRadio```", inline = False)
    await ctx.send(embed = em)

@stations.command()
async def DiamondCity(ctx):
    em = discord.Embed(title = "**Stations**", description = "Use f.station <specifc station> for extended help ", color = ctx.author.color)
    em.set_author(name="Fallout Radio", url="https://github.com/POPE44", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMgmfWEvADJKkzie4Aori3Rvdu-nIlAhqsGg&usqp=CAU")
    em.add_field(name = "__Diamond City radio__: ", value = "`Diamond City Radio is a radio station in the Commonwealth in 2287, broadcast from Diamond City. The radio station plays a total of 37 songs, not including Magnolia's songs. (From Fallout 4) `\n ")
    em.set_thumbnail(url="https://images.8tracks.com/cover/i/010/305/991/tumblr_nz6b0bFLvl1rmysx2o1_1280-3071.jpg?rect=0,0,999,999&q=98&fm=jpg&fit=max&w=640&h=640")
    em.add_field(name = "Example ", value = "```f.diamondcity```", inline = False)
    await ctx.send(embed = em)



#Errors
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the Perms :angry:")





client.run("token")


#f.resume
#@client.command()
#async def resume(ctx):
    #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    #if voice.is_paused():
        #voice.resume()
    #else:
        #await ctx.send("The audio is not paused.")
