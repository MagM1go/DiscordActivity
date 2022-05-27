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
