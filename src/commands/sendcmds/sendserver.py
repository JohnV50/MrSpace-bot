import discord
from discord.ext import commands


@commands.command()
async def sendserver(ctx):
    try:
        if ctx.message.author.guild_permissions.manage_guild == False:
            raise Exception("You don't have permission to run this command.")

        # send the transfer embed
        send_embed = discord.Embed(
            title = "Discord Servers",
            description = "Join our Discord servers!",
            color = 0x7289da,
            )

        # add new fields
        send_embed.add_field(name = "<:discord:1195587180328927332> Bloxlink Space", value = "https://discord.gg/bloxlinkspace", inline = False)

        send_embed.add_field(name = "<:discord:1195587180328927332> Bloxlink Support", value = "https://discord.gg/bloxlink", inline = False)

        send_embed.add_field(name = "<:discord:1195587180328927332> Bloxlink Community Servers", value = "https://discord.gg/mFbGzr6rYu", inline = False)
                   
        await ctx.send(embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)



# connecting to main file

async def setup(bot):
    bot.add_command(sendserver)