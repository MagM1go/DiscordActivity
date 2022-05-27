<h1 align="center">DiscordActivity</h1>

<h1>Discord activities on disnake (d.py fork).</h1> 


### pip install DiscordActivity


```Python
import disnake
from disnake.ext import commands
from DiscordActivity import Activity

bot = commands.Bot(command_prefix="!")
activities = Activity(bot=bot)

@bot.command()
async def fishing(ctx, voice: disnake.VoiceChannel, name: str):
    activity = await activities.send_activity(name=name, voice=voice)
    await ctx.reply(f"Go fishing!\nhttps://discord.gg/{activity['code']}")

bot.run("your-bot-token")
```
