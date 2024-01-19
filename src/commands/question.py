import discord
from discord.ext import commands
import constants

@commands.command()
async def question(ctx, *, question):
    try:
        if constants.ADMIN_ROLES in [role.id for role in ctx.message.author.roles]:
            return await ctx.send("You don't have permission to run this command.")
        # send the question embed
        send_embed = discord.Embed(
            title = "Question of the Day",
            description = question + "\n\nTell me in <#993990816693506110>!",
            color = 0x7289da,
            )

        # add new fields
        send_embed.add_field(name = "Sent by", value = ctx.author.mention, inline = False)
        channel = ctx.guild.get_channel(constants.QUESTION_CHANNEL)          
        await channel.send(content="<@&923787096018255953>",embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)
# connecting to main file

async def setup(bot):
    bot.add_command(question)