import discord
from discord.ext import commands


@commands.command()
async def sendfaq(ctx):
    try:
        if ctx.message.author.guild_permissions.manage_guild == False:
            raise Exception("You don't have permission to run this command.")

        # send the transfer embed
        send_embed = discord.Embed(
            title = "Frequently Asked Questions",
            description = "Here are the most common questions we receieved, read below before asking a mod.",
            color = 0x7289da,
            )

        # add new fields
        send_embed.add_field(name = "• How do I apply for moderator?", value = "Ask a moderator if applications are open or check <#918212006430011392> for updates.", inline = False)

        send_embed.add_field(name = "• Can I get free ROBUX?", value = "No, asking does not get you any robux. We do giveaways, prizes, and events all the time though!", inline = False)

        send_embed.add_field(name = "• How do I report a user or ask a question?", value = "Open a ticket in <#1197739394023571476> for all reports and questions.", inline = False)

        send_embed.add_field(name = "• When is the next video?", value = "No clue tbh, I just post it whenever I have a good video idea!", inline = False)

        send_embed.add_field(name = "• Can you play my game?", value = "We don't make any promises! You can suggest your game in <#1020418191471677481> and give us a reason to play it.", inline = False)

        send_embed.add_field(name = "• Where can I post video ideas?", value = "You can post all video and server suggestions in <#1020418191471677481>.", inline = False)
                   
        await ctx.send(embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)



# connecting to main file

async def setup(bot):
    bot.add_command(sendfaq)