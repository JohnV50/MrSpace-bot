import discord
from discord.ext import commands


@commands.command()
async def sendlink(ctx):
    try:
        if ctx.message.author.guild_permissions.manage_guild == False:
            raise Exception("You don't have permission to run this command.")

        # send the transfer embed
        send_embed = discord.Embed(
            title = "Our Links",
            description = "These are all the links we're affiliated with!",
            color = 0x7289da,
            )

        # add new fields
        send_embed.add_field(name = "<:roblox:1195589248041111573> Roblox Group", value = "https://www.roblox.com/groups/3587262/Bloxlink-Space", inline = False)

        send_embed.add_field(name = "<:roblox:1195589248041111573> Roblox Game", value = "https://www.roblox.com/games/8361082694/CATALOG-Bloxlink-HQ-WIP", inline = False)

        send_embed.add_field(name = "<:bloxlink:1195589398104911903> Bloxlink Website", value = "https://www.blox.link/", inline = False)
                   
        await ctx.send(embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)



# connecting to main file

async def setup(bot):
    bot.add_command(sendlink)