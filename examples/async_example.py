import nextcord
from nextcord.ext import commands

from DiscordActivity import AsyncActivity


bot = commands.Bot(command_prefix="!")
activity = AsyncActivity(token='your-bot-token')

@bot.command()
async def fishing(ctx):
    await ctx.send(f"Go fishing!\nhttps://discord.gg/{await activity.get_activity(activity_name='fishing', author=ctx.author)}")

bot.run("your-bot-token")
