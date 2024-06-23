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
        send_embed.add_field(name = "Staff Roles", value = 
        "<:greendot:1195602781139107880> <@&927960485830201415> - Youtuber & Community Manager of Bloxlink." + "\n" +
        "<:greendot:1195602781139107880> <@&918213203434025000> - Manages the server, bots, and staff team." + "\n" +
        "<:greendot:1195602781139107880> <@&967091714529587260> - Keeps the Discord server safe and friendly for everyone. Report all issues and ask questions to anyone with this role." + "\n" +
        "<:greendot:1195602781139107880> <@&1197760912908632127> - Monitors the Youtube stream chatroom by enforcing the rules and keeping it clean." + "\n" +
        "<:greendot:1195602781139107880> <@&1004055579137941625> - Moderator in training. They're learning the ropes to become a full on mod!", inline = False)

        send_embed.add_field(name = "Special Roles", value = "<:blackdot:1195602750487150592> <@&918213411718979644> - Special people! Bloxlink developers, bot owners, popular game developers, and more." + "\n" + 
        "<:blackdot:1195602750487150592> <@&1064675925754654780> - Content Creators with a minimum of 10,000 subscribers on Youtube. If you meet this requirement, open a ticket in <#1197739394023571476>." + "\n" +
        "<:blackdot:1195602750487150592> <@&1253740805252841553> - Upcoming Content Creators with a minimum of 1,000 subscribers & Consistent views above 100 on Youtube. If you meet this requirement, open a ticket in <#1197739394023571476>." + "\n" +
        "<:blackdot:1195602750487150592> <@&934392701032472697> - Boosters of Bloxlink Space! Gets access to a private channel and a pink shiny role." + "\n" +
        "<:blackdot:1195602750487150592> <@&934392701032472697> - Winners of <#1059124890671796234>, they had the best artwork this week!" + "\n" +
        "<:blackdot:1195602750487150592> <@&998055621754617946> - Member with a birthday today! Run ``/set`` to add your birthday to the bot.", inline = False)

        send_embed.add_field(name = "Community Roles", value = "<:yellowdot:1195602675304247296> <@&1197769019500003441> - Members who reached level 30 on the Miki bot, they are true veterans!" + "\n" + 
        "<:yellowdot:1195602675304247296> <@&1081330280020848650> - Member who reached level 20 on the Miki bot, they're always around!" + "\n" +
        "<:yellowdot:1195602675304247296> <@&1059129946896875550> - Members who reached level 10 on the Miki bot, they chat every once n while!" + "\n" +
        "<:yellowdot:1195602675304247296> <@&925980438839853066> - Everyone gets this role, get new roles by chatting more often!", inline = False)

        send_embed.add_field(name = "Notification Roles", value = "<:greydot:1195602718123896843> <@&972342975726227516> - Get notified when we stream or upload Youtube & TikTok videos." + "\n" + 
        "<:greydot:1195602718123896843> <@&923787096018255953> - Get notified when we release UGC items, usually at a lower price." + "\n" +
        "<:greydot:1195602718123896843> <@&972342964313522196> - Get notified when we post server updates, giveaways, and everything else." + "\n" +
        "<:greydot:1195602718123896843> <@&972321030074929182> - Get notified when we post in <#972314536638029894>, host game nights, movie nights, and other fun stuff.", inline = False)
                   
        await ctx.send(embed=send_embed)


    # exception handling
    except Exception as Error:
        await ctx.send(Error)



# connecting to main file

async def setup(bot):
    bot.add_command(sendroles)