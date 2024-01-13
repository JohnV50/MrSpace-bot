import discord
from discord.ext import commands


@commands.command()
async def sendinfo(ctx):
    try:
        if ctx.message.author.guild_permissions.manage_guild == False:
            raise Exception("You don't have permission to run this command.")

        # send the transfer embed
        send_embed = discord.Embed(
            title = "Welcome to BloxlinkLIVE!",
            description = "Bloxlink has multiple communities across Twitter, Youtube, Tiktok, and Discord. So, we've united it one place, welcome to BloxlinkLIVE!",
            color = 0x7289da,
            )

        # set the server icon
        send_embed.set_thumbnail(url = "https://media.discordapp.net/attachments/1195211738962989113/1195593232122384384/BloxlinkSpace_logo.jpg?ex=65b48df7&is=65a218f7&hm=901c7f5cf10b7c1d2ddad880bba2d7aaa9f6ddd2120cae7fc24050a02f141140&=&format=webp&width=1060&height=1016")
                   
        await ctx.send(embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)



# connecting to main file

async def setup(bot):
    bot.add_command(sendinfo)