import discord
from discord.ext import commands

import constants


@commands.command()
async def whitelist(ctx, id):
    try:
        member_roles = {role.id for role in ctx.author.roles}
        if constants.ADMIN_ROLES.isdisjoint(member_roles):
            return await ctx.send("You don't have permission to run this command.")    
        
        if id.isdigit() == False or len(id) < 18:
            return await ctx.send("Provide a valid discord id.")
        
        data = await ctx.bot.fetch_database_data(
            dict, ctx.guild.id, "question_whitelist"
        )
        whitelist_data = data.get("question_whitelist")
        
        if whitelist_data is None:
            await ctx.bot.update_database_item(
                ctx.guild.id, question_whitelist=[id]
            )
            return await ctx.send("User whitelisted.")
        
        if id in whitelist_data:
            whitelist_data.remove(id)
            await ctx.bot.update_database_item(
                ctx.guild.id, question_whitelist=whitelist_data
            )
            return await ctx.send("User unwhitelisted.")
        
        whitelist_data.append(id)
        await ctx.bot.update_database_item(
            ctx.guild.id, question_whitelist=whitelist_data
        )
        return await ctx.send("User whitelisted.")

    # exception handling
    except Exception as Error:
        await ctx.send(Error)


# connecting to main file


async def setup(bot):
    bot.add_command(whitelist)
