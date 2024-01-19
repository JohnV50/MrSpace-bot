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
    send_embed.set_thumbnail(url = "https://media.discordapp.net/attachments/923791634372632577/1195822898389200906/BloxlinkSpace_logo.jpg?ex=65b563dc&is=65a2eedc&hm=582111ca407a416266e5be90ba7b295170ac2836683773a9c3ed379608fe3327&=&format=webp&width=1060&height=1016")
                   
    await ctx.send(embed=send_embed)


# connecting to main file

async def setup(bot):
    bot.add_command(youtube)