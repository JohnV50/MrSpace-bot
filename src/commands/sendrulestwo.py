import discord
from discord.ext import commands


@commands.command()
async def sendrulestwo(ctx):
    try:
        if ctx.message.author.guild_permissions.manage_guild == False:
            raise Exception("You don't have permission to run this command.")

        # send the transfer embed
        send_embed = discord.Embed(
            color = 0x7289da,
            )

        # add new fields
        send_embed.add_field(name = "", value = "**11.** If you have any issues or questions, you may ping the @Merry Moderators role. Only ping once" + "\n" +
        "**12.** Keep talking in a different language other than English to a minimum. We prefer English as it’s the language we can moderate in." + "\n" +
        "**13.** Do not ask for Bloxlink bot support here, head to the support server at https://blox.link/support and ask for help there."
        "**14.** Copy pasted and chain mail are prohibited." + "\n" +
        "**15.** Don't spread misinformation." + "\n" +
        "**16.** Using alternative accounts for an unfair advantage in bots, events, giveaways, or anything along those lines is prohibited." + "\n" +
        "**17.** Do not make anyone feel uncomfortable, be respectful to all.", inline = False)
                   
        await ctx.send(embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)



# connecting to main file

async def setup(bot):
    bot.add_command(sendrulestwo)