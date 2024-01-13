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
            description = "Follow our social media accounts!",
            color = 0x7289da,
            )

        # add new fields
        send_embed.add_field(name = "<:youtube:1185982362945847407> Youtube", value = "https://youtube.com/c/Bloxlink", inline = False)

        send_embed.add_field(name = "<:tiktok:1195586465233633342> TikTok", value = "https://www.tiktok.com/@blox.link", inline = False)

        send_embed.add_field(name = "<:twitter:1195586490810499153> Twitter / X", value = "https://twitter.com/bloxlink", inline = False)
                   
        await ctx.send(embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)



# connecting to main file

async def setup(bot):
    bot.add_command(sendsocial)