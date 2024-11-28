import logging
from asyncio import sleep
from enum import IntEnum

import discord
from discord.ext import commands

import constants
from main import MyBot

logger = logging.getLogger("Reaction Roles")


class ReactionRole(IntEnum):
    """Represents all the potential reaction role options the bot can post."""

    MINECRAFT_ROLE = 1209001740461019166

    @property
    def emoji(self) -> discord.PartialEmoji:
        """The emoji that corresponds with this ReactionRole enum."""
        match self:
            case self.MINECRAFT_ROLE:
                return discord.PartialEmoji(name="🎱")


class ReactionRoles(commands.Cog):
    """Everything related to reaction roles. Both the command for triggering, and handling."""

    def __init__(self, bot) -> None:
        self.bot: MyBot = bot

    @commands.command(aliases=["rp"])
    async def reaction_prompt(self, ctx: commands.Context):
        # Restrict the command to admin roles. Uses sets to check ~~bc why not~~
        member_roles = {role.id for role in ctx.author.roles}
        if constants.ADMIN_ROLES.isdisjoint(member_roles):
            return

        embed = discord.Embed(
            title="◇・SELECT YOUR ROLES",
            color=0x546E7A,
        )

        # Build the embed description
        description = ["These roles open new channels!\n"]
        for emote in ReactionRole:
            description.append(f"{emote.emoji} ・ <@&{emote}>")
        embed.description = "\n".join(description)

        # Send the embed.
        try:
            prompt = await ctx.send(embed=embed)
        except (discord.HTTPException, discord.Forbidden):
            logger.error("Could not send a message in that channel. Make sure the bot has permissions first.")
            return

        # Save the message ID of the prompt in the database.
        await self.bot.update_database_item(ctx.guild.id, prompt_message=str(prompt.id))

        # Add reactions.
        for emote in ReactionRole:
            await prompt.add_reaction(emote.emoji)
            await sleep(0.5)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if not payload.guild_id:
            return

        await self.handle_reaction_event(
            user_id=payload.user_id,
            message_id=payload.message_id,
            guild_id=payload.guild_id,
            emoji=payload.emoji,
            member=payload.member,
            is_adding=True,
        )

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if not payload.guild_id:
            return

        await self.handle_reaction_event(
            user_id=payload.user_id,
            message_id=payload.message_id,
            guild_id=payload.guild_id,
            emoji=payload.emoji,
            member=payload.member,
            is_adding=False,
        )

    async def handle_reaction_event(
        self,
        user_id: int,
        message_id: int,
        guild_id: int,
        emoji: discord.PartialEmoji,
        member: discord.Member | None = None,
        is_adding: bool = True,
    ):
        """The logic for adding/removing reaction roles."""

        # Get message ID from database and check first.
        data = await self.bot.fetch_database_data(dict, guild_id, "prompt_message")

        if data.get("prompt_message", None) != str(message_id):
            return

        # Get the guild so we can get the member
        guild = self.bot.get_guild(guild_id)
        if not guild:
            try:
                guild = await self.bot.fetch_guild(guild_id)
            except (discord.Forbidden, discord.HTTPException):
                logger.warning("Could not retrieve the guild for this reaction.")
                return

        if not member:
            member = guild.get_member(user_id)
            if not member:
                try:
                    member = await guild.fetch_member(user_id)
                except (discord.Forbidden, discord.HTTPException, discord.NotFound):
                    logger.warning("Could not retrieve the member reacting.")
                    return

        # Bot listens to itself, stop that
        if member.bot:
            return

        # Figure out which role the user chose
        role_to_change = None
        for rr_emoji in ReactionRole:
            if emoji == rr_emoji.emoji:
                role_to_change = rr_emoji
                break

        if not role_to_change:
            return

        # Only adjust roles where applicable.
        role_ids = [role.id for role in member.roles]

        if (is_adding and role_to_change in role_ids) or (not is_adding and role_to_change not in role_ids):
            return

        role_to_change = discord.Object(id=role_to_change)
        try:
            if is_adding:
                await member.add_roles(role_to_change)
            else:
                await member.remove_roles(role_to_change)
        except (discord.Forbidden, discord.HTTPException):
            logger.warning(f"Could not adjust the roles for {member}.")


async def setup(bot: MyBot):
    await bot.add_cog(ReactionRoles(bot))
