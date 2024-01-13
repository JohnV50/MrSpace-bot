import discord
from discord.ext import commands


@commands.command(aliases = ["x"])
async def twitter(ctx):
    # send the transfer embed
    send_embed = discord.Embed(
        title = "Follow our Twitter/X Channel!",
        description = "https://twitter.com/bloxlink",
        color = 0xe91e63,
    )

    # set the server icon
    send_embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/1195211738962989113/1195822229498380440/UbWw9SPb_400x400.jpg?ex=65b5633c&is=65a2ee3c&hm=2a6dd9ef4561ffb0c79eb0623a33125166f70429f43417c42d722910dc5891c3&")
                   
    await ctx.send(embed=send_embed)


# connecting to main file

async def setup(bot):
    bot.add_command(twitter)