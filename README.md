<h1 align="center">DiscordActivity</h1>

<h1>Discord activities in nextcord.</h1> 


#### pip install DicsordActivity


Sync Example
--------------

```Python
import nextcord
from nextcord.ext import commands

from DiscordActivity import SyncActivity


bot = commands.Bot(command_prefix="!")
activity = SyncActivity(token='your-bot-token')

@bot.command()
async def fishing(ctx):
    await ctx.send(f"Go fishing!\nhttps://discord.gg/{activity.get_activity(activity_name='fishing', author=ctx.author)}")

bot.run("your-bot-token")
```

Async example
--------------

```Python
import nextcord
from nextcord.ext import commands

from DiscordActivity import AsyncActivity


bot = commands.Bot(command_prefix="!")
activity = AsyncActivity(token='your-bot-token')

@bot.command()
async def fishing(ctx):
    await ctx.send(f"Go fishing!\nhttps://discord.gg/{await activity.get_activity(activity_name='fishing', author=ctx.author)}")

bot.run("your-bot-token")
```
