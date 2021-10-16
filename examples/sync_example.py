import nextcord
from nextcord.ext import commands

from DiscordActivity import SyncActivity


bot = commands.Bot(command_prefix="!")
activity = SyncActivity(token='your-bot-token')

@bot.command()
async def fishing(ctx):
    await ctx.send(f"Go fishing!\nhttps://discord.gg/{activity.get_activity(activity_name='fishing', author=ctx.author)}")

bot.run("your-bot-token")
