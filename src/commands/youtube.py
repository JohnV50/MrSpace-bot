import discord
from discord.ext import commands


@commands.command()
async def youtube(ctx):
    # send the transfer embed
    send_embed = discord.Embed(
        title = "Subscribe to our Youtube Channel!",
        description = "https://www.youtube.com/@bloxlink",
        color = 0xe91e63,
    )

    # set the server icon
    send_embed.set_thumbnail(url = ctx.guild.icon)
                   
    await ctx.send(embed=send_embed)


# connecting to main file

async def setup(bot):
    bot.add_command(youtube)