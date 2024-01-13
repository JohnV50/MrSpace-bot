import discord
from discord.ext import commands


@commands.command()
async def help(ctx):
    try:
        # send the transfer embed
        help_embed = discord.Embed(
            description = "Here's a list of all our commands and how to use them.",
            color = 0x546e7a,
            )
    
        # title and profile icon
        help_embed.set_author(name = "BloxlinkLIVE Help Page", icon_url = ctx.bot.user.avatar)

        help_embed.add_field(name = "Information", value = "test", inline = False)
                   
        await ctx.send(embed=help_embed)
    
    except Exception as Error:
        await ctx.send(Error)


# connecting to main file

async def setup(bot):
    bot.add_command(help)