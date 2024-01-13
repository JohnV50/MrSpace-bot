import discord
from discord.ext import commands


@commands.command()
async def sendsocial(ctx):
    try:
        if ctx.message.author.guild_permissions.manage_guild == False:
            raise Exception("You don't have permission to run this command.")

        # send the transfer embed
        send_embed = discord.Embed(
            title = "Social Media",
            description = "fill in here",
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
    bot.add_command(sendsocial)