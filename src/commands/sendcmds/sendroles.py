import discord
from discord.ext import commands


@commands.command()
async def sendroles(ctx):
    try:
        if ctx.message.author.guild_permissions.manage_guild == False:
            raise Exception("You don't have permission to run this command.")

        # send the transfer embed
        send_embed = discord.Embed(
            title = "Server Roles",
            description = "These are all the roles in the server!",
            color = 0x7289da,
            )

        # add new fields
        send_embed.add_field(name = "Staff Roles", value = "<:greendot:1195602781139107880> <@&roleID> - Owner & Developer of Bloxlink" + "\n" + 
        "<:greendot:1195602781139107880> <@&roleID> - Youtuber & COO of Bloxlink" + "\n" +
        "<:greendot:1195602781139107880> <@&roleID> - Manages the server and staff team" + "\n" +
        "<:greendot:1195602781139107880> <@&roleID> - Keeps the Discord server safe and friendly for everyone. Report all issues and ask questions to anyone with this role." + "\n" +
        "<:greendot:1195602781139107880> <@&roleID> - Monitors the Youtube stream chatroom by enforcing the rules and keeping it clean.", inline = False)

        send_embed.add_field(name = "Special Roles", value = "<:blackdot:1195602750487150592> <@&roleID> - Special people! Bloxlink developers, bot owners, popular game developers, and more." + "\n" + 
        "<:blackdot:1195602750487150592> <@&roleID> - Helps in running our social media accounts like video editors, graphic designers, managers, and asset creators." + "\n" +
        "<:blackdot:1195602750487150592> <@&roleID> - Creators of awesome Roblox UGC items. Some created the items in <#1195211738715537476>" + "\n" +
        "<:blackdot:1195602750487150592> <@&roleID> - Content Creators with a minimum of 10,000 subscribers on Youtube. If you meet this requirement, open a ticket in <#1195211738962989111> and ask about the role!" + "\n" +
        "<:blackdot:1195602750487150592> <@&roleID> - Boosters of BloxlinkLIVE! Gets access to a custom channel + a pink shiny role." + "\n" +
        "<:blackdot:1195602750487150592> <@&roleID> - Member with a birthday today! Run ``/set`` to add your birthday to the bot.", inline = False)

        send_embed.add_field(name = "Community Roles", value = "<:yellowdot:1195602675304247296> <@&roleID> - Members who reached level 30 on the Miki bot, long time chatters!" + "\n" + 
        "<:yellowdot:1195602675304247296> <@&roleID> - Member who reached level 20 on the Miki bot, they're less shy now!" + "\n" +
        "<:yellowdot:1195602675304247296> <@&roleID> - Members who reached level 10 on the Miki bot, they chat every once n while!" + "\n" +
        "<:yellowdot:1195602675304247296> <@&roleID> - Member of this server. Everyone gets this role, get new roles by chatting!", inline = False)

        send_embed.add_field(name = "Notification Roles", value = "<:greydot:1195602718123896843> <@&roleID> - Gets notified when we go live on Youtube or upload Youtube & TikTok videos." + "\n" + 
        "<:greydot:1195602718123896843> <@&roleID> - Gets notified when we release UGC items, usually at a lower price." + "\n" +
        "<:greydot:1195602718123896843> <@&roleID> - Gets notified when we post server updates, tweets, giveaways, and everything else." + "\n" +
        "<:greydot:1195602718123896843> <@&roleID> - Gets notified when we post in <#1195211738962989107>, host game nights, movie nights, and more.", inline = False)
                   
        await ctx.send(embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)



# connecting to main file

async def setup(bot):
    bot.add_command(sendroles)