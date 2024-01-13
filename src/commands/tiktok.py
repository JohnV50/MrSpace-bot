import discord
from discord.ext import commands


@commands.command()
async def tiktok(ctx):
    # send the transfer embed
    send_embed = discord.Embed(
        title = "Follow our TikTok Channel!",
        description = "https://www.tiktok.com/@blox.link",
        color = 0xe91e63,
    )

    # set the server icon
    send_embed.set_thumbnail(url = "https://media.discordapp.net/attachments/923791634372632577/1195820740931498187/BloxlinkLogo2021red_2.png?ex=65b561d9&is=65a2ecd9&hm=569bfdda30bb705111958cedccac08d3392afcfa850b6389b59aa928ea4148df&=&format=webp&quality=lossless&width=1112&height=1112")
                   
    await ctx.send(embed=send_embed)


# connecting to main file

async def setup(bot):
    bot.add_command(tiktok)