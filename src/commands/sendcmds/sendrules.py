import discord
from discord.ext import commands


@commands.command()
async def sendrules(ctx):
    try:
        if ctx.message.author.guild_permissions.manage_guild == False:
            raise Exception("You don't have permission to run this command.")

        # send the transfer embed
        send_embed = discord.Embed(
            title = "Server Rules",
            description = "Follow all rules at all times. If you're unsure about something, ask a moderator.",
            color = 0x7289da,
            )

        # add new fields
        send_embed.add_field(name = "", value = "**1.** Be respectful to one another." + "\n" + 
        "**2.** NSFW is prohibited in all forms. keep all content family-friendly." + "\n" + 
        "**3.** Follow all Discord Guidelines & Terms of Service (https://discordapp.com/terms) - (https://discord.com/new/guidelines)" + "\n" + 
        "**4.** Don't spam members of this discord or flood the channels with unnecessary messages" + "\n" +
        "**5.** Advertising in the server or DMs is prohibited." + "\n" +
        "**6.** Offensive language in any form is prohibited." + "\n" +
        "**7.** Don’t mass ping users, spam channels, or post unwanted content." + "\n" +
        "**8.** Keep content in their respective channels." + "\n" +
        "**9.** Don’t ping individual staff members or mass ping other users.", inline = False)
                   
        await ctx.send(embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)



# connecting to main file

async def setup(bot):
    bot.add_command(sendrules)