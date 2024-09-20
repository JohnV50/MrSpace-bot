import logging

import discord
from discord.ext import commands

import constants
from main import MyBot

logger = logging.getLogger("Welcome Event")

ROLE_SELECTION_CHANNEL = 923784956436676690
GENERAL_CHAT_CHANNEL = 919666442872442950


class WelcomeModule(commands.Cog):
    """Everything related to welcoming users. Both the command for triggering, and handling."""

    def __init__(self, bot) -> None:
        self.bot: MyBot = bot

    @commands.command(aliases=["welcome"])
    async def welcome_channel(self, ctx: commands.Context):
        """Set the channel where people will be welcomed. Run it in the channel you want to use."""
        # Restrict the command to admin roles. Uses sets to check ~~bc why not~~
        member_roles = {role.id for role in ctx.author.roles}
        if constants.ADMIN_ROLES.isdisjoint(member_roles):
            return

        # Save the welcome channel in the database.
        await self.bot.update_database_item(ctx.guild.id, welcome_channel=str(ctx.channel.id))
        await ctx.reply(content=f"The welcome channel has been set to {ctx.channel.mention}")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        db_data = await self.bot.fetch_database_data(dict, member.guild.id, "welcome_channel")
        welcome_channel = db_data.get("welcome_channel")

        if not welcome_channel:
            return

        guild = member.guild
        embed = discord.Embed(color=0x7289DA, title=f"Welcome to **{guild.name}**, {member.name}")
        embed.description = (
            f"Hey {member.mention}! Welcome to **{guild.name}**! "
            f"Select your custom roles on the onboarding screen.\n\n"
            f"Chat with our community in <#{GENERAL_CHAT_CHANNEL}>!"
        )
        embed.set_footer(text=f"There are now {guild.member_count} members.")
        embed.set_author(name=guild.name, icon_url=guild.icon.url)
        embed.set_thumbnail(url=member.avatar.url or member.default_avatar.url)

        channel = self.bot.get_channel(int(welcome_channel)) or await self.bot.fetch_channel(
            int(welcome_channel)
        )
        if not channel:
            logger.warning("Could not get the set welcome channel for %s", guild.name)
            return

        await channel.send(
            embed=embed,
            allowed_mentions=discord.AllowedMentions(
                everyone=False,
                users=False,
                roles=False,
            ),
        )


async def setup(bot: MyBot):
    await bot.add_cog(WelcomeModule(bot))
