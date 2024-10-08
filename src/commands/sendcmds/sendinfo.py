import discord
from discord.ext import commands


@commands.command()
async def sendinfo(ctx):
    try:
        if ctx.message.author.guild_permissions.manage_guild == False:
            raise Exception("You don't have permission to run this command.")

        # send the transfer embed
        send_embed = discord.Embed(
            title = "Welcome to Space Cookie!",
            description = "Welcome to Space Cookie! Cozy community for all Robloxians to come and chill out, eat some cookies, and hang out!",
            color = 0x7289da,
            )

        # set the server icon
        send_embed.set_thumbnail(url = ctx.guild.icon)
                   
        await ctx.send(embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)



# connecting to main file

async def setup(bot):
    bot.add_command(sendinfo)