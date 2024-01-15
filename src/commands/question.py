import discord
from discord.ext import commands


@commands.command()
async def question(ctx, *, question):
    try:
        if ctx.message.author.guild_permissions.manage_guild == False:
            return await ctx.send("You don't have permission to run this command.")
        # send the question embed
        send_embed = discord.Embed(
            title = "Question of the Day",
            description = question + "\n\nTell me in answers",
            color = 0x7289da,
            )

        # add new fields
        send_embed.add_field(name = "Sent by", value = ctx.author.mention, inline = False)
                   
        await ctx.send(content="<@194962036784889858> L",embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)
# connecting to main file

async def setup(bot):
    bot.add_command(question)