import discord
from discord.ext import commands
import constants
import datetime

@commands.command()
async def question(ctx, *, question):
    try:
        if constants.ADMIN_ROLES not in [role.id for role in ctx.message.author.roles]:
            return await ctx.send("You don't have permission to run this command.")
        # send the question embed
        send_embed = discord.Embed(
            title = "Question of the Day",
            description = question + "\n\nTell me in <#993990816693506110>!",
            color = 0x7289da,
            )
        data = await ctx.bot.fetch_database_data(dict, ctx.guild.id, "question_cooldown")
        qc = data.get("question_cooldown")
        if qc is None:
            await ctx.bot.update_database_item(ctx.guild.id, question_cooldown=datetime.datetime.utcnow())
        else:
            if (datetime.datetime.utcnow() - data["question_cooldown"]) < datetime.timedelta(hours=16):
                return await ctx.send("You can only send a question once every 24 hours.")
            await ctx.bot.update_database_item(ctx.guild.id, question_cooldown=datetime.datetime.utcnow())
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