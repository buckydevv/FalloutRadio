import discord, os, json, youtube_dl, random, asyncio, random, praw, aiohttp, pafy
from discord.ext import commands, tasks
from discord.utils import get
from pathlib import Path
from random import choice
from discord.voice_client import VoiceClient
from discord import Embed

client = commands.Bot(command_prefix="f.")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the sun set on the Wasteland"))
    print("------------------------------------\n           Bot is Running: \n------------------------------------")
    print("Name: {}\n".format(client.user.name))
    print("ID: {}\n".format(client.user.id)) 

#f.ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Radio Strength: {round(client.latency * 1000)}ms')


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
    mp3_path = "/home/pi/Desktop/FalloutRadio/4.DiamondCity"
    path = "/home/pi/Desktop/FalloutRadio/4.DiamondCity"
    files=os.listdir(path)

    for _ in os.listdir(path):
        d = random.choice(files)

        if not voice.is_playing():
            print(f"Playing \"{d}\"")
            voice.play(
                discord.FFmpegPCMAudio(
                    os.path.join(mp3_path, d)
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
    path = "D:\\Bot\\76.applachia"
    files=os.listdir(path)

    for _ in os.listdir(path):
        d = random.choice(files)

        if not voice.is_playing():
            print(f"Playing \"{d}\"")
            voice.play(
                discord.FFmpegPCMAudio(os.path.join(mp3_path, d)
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
    mp3_path = "D:\\Bot\\fallout.2                     #Note if you want music from a folder youll need to change the filepath you will also need to force run it throught the fmmpeg .exe
    path = "D:\\Bot\\fallout.2"
    files=os.listdir(path)

    for _ in os.listdir(path):
        d = random.choice(files)

        if not voice.is_playing():
            print(f"Playing \"{d}\"")
            voice.play(
                discord.FFmpegPCMAudio(os.path.join(mp3_path, d)
                )
            )

        while voice.is_playing():
            await asyncio.sleep(0.25)

#f.gnr
@client.command()
async def GNR(ctx):
    guild = ctx.guild
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("Tuning in to Galaxy News Radio!")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    mp3_path = "/home/pi/Desktop/FalloutRadio/Fallout3_GNR"
    path = "/home/pi/Desktop/FalloutRadio/Fallout3_GNR"
    files=os.listdir(path)

    for _ in os.listdir(path):
        d = random.choice(files)

        if not voice.is_playing():
            print(f"Playing \"{d}\"")
            voice.play(
                discord.FFmpegPCMAudio(os.path.join(mp3_path, d)
                )
            )

        while voice.is_playing():
            await asyncio.sleep(0.25)



#f.Mojave
@client.command()
async def Mojave(ctx):
    guild = ctx.guild
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("Tuning in to Mojave Wasteland Radio!")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    mp3_path = "/home/pi/Desktop/FalloutRadio/Mojave"
    path = "/home/pi/Desktop/FalloutRadio/Mojave"
    files=os.listdir(path)

    for _ in os.listdir(path):
        d = random.choice(files)

        if not voice.is_playing():
            print(f"Playing \"{d}\"")
            voice.play(
                discord.FFmpegPCMAudio(os.path.join(mp3_path, d)
                )
            )

        while voice.is_playing():
            await asyncio.sleep(0.25)


#help
client.remove_command("help")
@client.command(invoke_without_command = True)
async def help(ctx):
    em = Embed(title = "Help", description = "Use f.help <command> for extended help **(type f.stations for a list of stations)**", color = ctx.author.color)
    em.add_field(name = "**Commands**", value = "Commands:\n `f.ping`  - shows bots latency\n `f.skip`  - skips song\n `snipe`  - shows last deleted message\n `f.meme`  - Shows a random meme from r/falloutmemes\n `f.play ww w.youtube.com/example`  - plays a outube video off a url\n `f.invite`  - Invite Link For The Bot\n f.author`  - My Socials\n  ")
    em.add_field(name = "**KEY NOTES**", value = "The bot is still in development as such its a bit clunky. There is currently no skip feature. To make the bot stop type f.leave (to skip type 'f.skip'). The 'f.play' feature only works with a url directly after it.")
    em.add_field(name = "**Support Me**", value = "[(Invite Fot Bot](https://discord.com/api/oauth2/authorize?client_id=770963714387214337&permissions=1677025137&scope=bot) , [Invite To Support Server](hhtps://discord.gg/VmbFGpshyP) , [My GitHub](https://github.com/POPE44/FalloutRadio)")
    await ctx.send(embed = em)

@client.group()
async def stations(ctx):
    em = Embed(title = "**Stations**", description = "Use f.station <specifc station> for extended help ", color = ctx.author.color)
    em.set_author(name="Fallout Radio", url="https://github.com/POPE44", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMgmfWEvADJKkzie4Aori3Rvdu-nIlAhqsGg&usqp=CAU")
    em.add_field(name = "__Stations__: ", value = "`diamondcity`\n`galaxynewsradio`\n`fallout2`\n`mojave`\n`appalachia`\n`classical`\n ")
    em.add_field(name = "Example ", value = "```f.stations GalaxyNewsRadio```", inline = False)
    await ctx.send(embed = em)

@stations.command()
async def diamondcity(ctx):
    em = Embed(title = "**Stations**", description = "Use f.station <specifc station> for extended help ", color = ctx.author.color)
    em.set_author(name="Fallout Radio", url="https://github.com/POPE44", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMgmfWEvADJKkzie4Aori3Rvdu-nIlAhqsGg&usqp=CAU")
    em.add_field(name = "__Diamond City radio__: ", value = "Diamond City Radio is a radio station in the Commonwealth in 2287, broadcast from Diamond City. The radio station plays a total of 37 songs, not including Magnolia's songs. (From Fallout 4) \n ")
    em.set_thumbnail(url="https://i.ibb.co/88DC7NZ/tumblr-nz6b0b-FLvl1rmysx2o1-1280-3071.jpg")
    em.add_field(name = "**Wiki: **", value = "https://fallout.fandom.com/wiki/Diamond_City_Radio", inline = False)
    em.add_field(name = "Example ", value = "```f.diamondcity```", inline = False)
    await ctx.send(embed = em)

@stations.command()
async def galaxynewsradio(ctx):
    em = Embed(title = "**Stations**", description = "Use f.station <specifc station> for extended help ", color = ctx.author.color)
    em.set_author(name="Fallout Radio", url="https://github.com/POPE44", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMgmfWEvADJKkzie4Aori3Rvdu-nIlAhqsGg&usqp=CAU")
    em.add_field(name = "**Galaxy News Radio**: ", value = "Galaxy News Radio was a pre-War radio station based in Washington, D.C. and a subsidiary of Galaxy News Network. By 2277, Galaxy News Radio had been repurposed by Three Dog into a community radio station that reported on the happenings around the Capital Wasteland. (From Fallout 3) `\n ")
    em.set_thumbnail(url="https://i.ibb.co/DgFycpX/05-Galaxy-News-Radio.png")
    em.add_field(name = "**Wiki: **", value = "https://fallout.fandom.com/wiki/Galaxy_News_Radio_(radio)", inline = False)
    em.add_field(name = "Example ", value = "```f.GNR```", inline = False)
    await ctx.send(embed = em)
 
@stations.command()
async def appalachia(ctx):
    em = Embed(title = "**Stations**", description = "Use f.station <specifc station> for extended help ", color = ctx.author.color)
    em.set_author(name="Fallout Radio", url="https://github.com/POPE44", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMgmfWEvADJKkzie4Aori3Rvdu-nIlAhqsGg&usqp=CAU")
    em.add_field(name = "**Appalachia Radio** : ", value = "Appalachia Radio is broadcast from an unknown location within West Virginia, though its exact location does not appear anywhere in-game. Radio placement in pre-War locations indicates that it was on the air before the Great War, though its history from 2077 until 2102 is uncertain. When the Vault Dwellers of Vault 76 emerged on Reclamation Day, the radio was continuously broadcasting songs on a loop, without a DJ.\nAs humans returned to the region after the Scorched Plague subsided, Julie, a young woman from the area, found the station where Appalachia Radio had its origin. She had previously listened to the station, and because the songs meant so much to her, she wanted to make sure that the radio was kept in working order.(From Fallout 76) `\n ")
    em.set_thumbnail(url="https://i.ibb.co/z4gVg4P/maxresdefault.jpg")
    em.add_field(name = "**Wiki: **", value = "https://fallout.fandom.com/wiki/Appalachia_Radio", inline = False)
    em.add_field(name = "Example ", value = "```f.appalachia```", inline = False)
    await ctx.send(embed = em)

@stations.command()
async def mojave(ctx):
    em = Embed(title = "**Stations**", description = "Use f.station <specifc station> for extended help ", color = ctx.author.color)
    em.set_author(name="Fallout Radio", url="https://github.com/POPE44", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMgmfWEvADJKkzie4Aori3Rvdu-nIlAhqsGg&usqp=CAU")
    em.add_field(name = "**Mojave/New Vegas Radio: ** ", value = "Mojave Music Radio only plays music, which consists mostly of country/western and rockabilly (some of which were actually performed and written by contemporary 21st-century musicians), with no DJ or news segments. The music played is the same as the music on Black Mountain Radio, but without the station's talk segments with Tabitha. It is unknown where the broadcast is coming from, yet its signal covers the entire Mojave.\n ")
    em.set_thumbnail(url="https://i.ibb.co/br8LMQ1/133e20cb881a81d775cdc85216246a49-500x500x1.jpg")
    em.add_field(name = "**Wiki: **", value = "https://fallout.fandom.com/wiki/Mojave_Music_Radio", inline = False)
    em.add_field(name = "Example ", value = "```f.Mojave```", inline = False)
    await ctx.send(embed = em)


@stations.command()
async def fallout2(ctx):
    em = Embed(title = "**Stations**", description = "Use f.station <specifc station> for extended help ", color = ctx.author.color)
    em.set_author(name="Fallout Radio", url="https://github.com/POPE44", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMgmfWEvADJKkzie4Aori3Rvdu-nIlAhqsGg&usqp=CAU")
    em.add_field(name = "**Fallout 2 SoundTrack **", value = "The soundtrack for Fallout 2 was composed by Mark Morgan. On May 10, 2010, it was released together with the Fallout soundtrack on Morgan's Vault Archives album.\n ")
    em.set_thumbnail(url="https://i.ibb.co/tB4Xs0N/images.jpg")
    em.add_field(name = "Example ", value = "```f.fallout2```", inline = False)
    em.add_field(name = "**Wiki**: ", value = "https://fallout.fandom.com/wiki/Fallout_2_soundtrack", inline = False)
    await ctx.send(embed = em)

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@client.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None

@client.command()
async def snipe(message):
    if snipe_message_content==None:
        await message.channel.send("Theres nothing to snipe.")
    else:
        embed = Embed(description=f"{snipe_message_content}")
        embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
        embed.set_author(name= f"<@{snipe_message_author}>")
        await message.channel.send(embed=embed)
        return

@client.command(pass_context=True) 
async def meme(ctx): 
    embed = Embed(title="", description="")
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/FalloutMemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 100)]['data']['url'])
            await ctx.send(embed=embed)
            
            
#invite
@client.command()
async def invite(ctx):
    mbed = Embed(title = "Invite Link For Bot!! Spread It Around!!", description = "[Invite Fot Bot](https://discord.com/api/oauth2/authorize?client_id=770963714387214337&permissions=1677025137&scope=bot)")
    await ctx.send(embed = mbed)
 
#invite
@client.command()
async def author(ctx):
    mbed = Embed(title = "Thanks For Checking My Socials Out!!", description = "[Github](https://github.com/POPE44) , [Twitter](https://twitter.com/POPE44644) , [Reddit](https://www.reddit.com/user/WheresWally44)")
    await ctx.send(embed = mbed)
    
    



#servercount
@client.command(pass_context = True)
async def servercount(ctx):
  await ctx.send(f"I'm in {len(client.guilds)} servers!") 


client.run("token")
