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
        send_embed.add_field(name = "", value = "**1.** Keep it classy. Don't be rude to anyone or use racist/vulgar language." + "\n" + 
        "**2.** NSFW is prohibited in all forms. keep all content family-friendly." + "\n" + 
        "**3.** Follow all Discord Guidelines & Terms of Service (https://discordapp.com/terms) - (https://discord.com/new/guidelines)" + "\n" + 
        "**4.** Don't spam members of this discord or flood the channels with unnecessary messages" + "\n" +
        "**5.** Use common sense, if you know it’s not right then don’t do it." + "\n" +
        "**6.** All rules from the main Bloxlink HQ server apply here as well." + "\n" +
        "**7.** You're required to be verified on Bloxlink to be considered for specific events." + "\n" +
        "**8.** Keep cursing to a minimum." + "\n" +
        "**9.** No advertising or promoting of any kind." + "\n" +
        "**10.** Don’t ping individual staff members or mass ping other users.", inline = False)
                   
        await ctx.send(embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)



# connecting to main file

async def setup(bot):
    bot.add_command(sendrules)