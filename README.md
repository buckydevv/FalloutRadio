# Fallout Radio (A discord.py Music Bot)

A Fallout Radio themed discord bot to bring the wasteland to your server!

### Prerequisites

- Have python and discord installed. Go [here](https://www.python.org/downloads/) for the latest release of python and go [here](https://discord.com/download) for the latest version of Discord.

## Getting Started & Installtion

To Install on your system check the wiki. For Windows installtion go [here](https://github.com/POPE44/FalloutRadio/wiki/Windows-Installation) and for linux installtion go [here](https://github.com/POPE44/FalloutRadio/wiki/Linux-Installation)

## Test Server

- Join my discord server [here](https://discord.gg/qr4pyDB8cv) .
- Invite my bots to your server [Fallout](https://discord.com/api/oauth2/authorize?client_id=770963714387214337&permissions=7409409&scope=bot) [ModBot](http://bit.ly/383IjtK)


### An Extensive Help Menu and List of Stations

[](https://i.ibb.co/jhb9VTY/Capture1.png)

[](https://i.ibb.co/ZXyTzyH/Capture2.png)




## Hosting

- I dont know how to host this on heroku (yet) but will attempt to learn. As of now i have it deployed on a windows machine on AWS free 1 year trial.

### Code For Playing a Staion

- An example code of a staion
 
 ```python 
@client.command()
async def diamondcity(ctx):
    guild = ctx.guild
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("Tuning in to Diamond City Radio!")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    mp3_path = "D:\\Bot\\4.DiamondCity"
    exc_path = "D:\\Bot\\ffmpeg\\bin\\ffmpeg.exe"
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
```


## Built With

* [Discord.py](https://discordpy.readthedocs.io/en/latest/) - The web framework used 
* [FFmpeg](https://ffmpeg.org/) - Audio
* [Python](phttps://www.python.org/) - Langauge

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors

* **Pope** - *All Work* - [Grizz#7690](https://discord.gg/qr4pyDB8cv)


## Acknowledgments

- Special Thanks to Xhiro for helping (a lot) with this project
- The People in the python Discord
- & Zxcer who helped a little
