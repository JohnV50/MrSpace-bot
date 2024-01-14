import logging
from asyncio import sleep
from enum import IntEnum

import discord
from discord.ext import commands

logger = logging.getLogger()


class ReactionRole(IntEnum):
    UPLOAD_ROLE = 1
    UGC_ROLE = 2
    FEED_ROLE = 3
    FUN_ROLE = 4

    @property
    def emoji(self) -> discord.PartialEmoji:
        match self:
            case self.UPLOAD_ROLE:
                return discord.PartialEmoji(name="youtube", id=1195878401085554819)
            case self.UGC_ROLE:
                return discord.PartialEmoji(name="🎁")
            case self.FEED_ROLE:
                return discord.PartialEmoji(name="📰")
            case self.FUN_ROLE:
                return discord.PartialEmoji(name="🎱")


class ReactionRoles(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command(aliases=["rp"])
    async def reaction_prompt(self, ctx: commands.Context):
        embed = discord.Embed(
            title="◇・PINGS",
            color=0x546E7A,
        )

        # Build the embed description
        description = []
        for emote in ReactionRole:
            description.append(f"{emote.emoji} ・ <@&{emote}>")
        embed.description = "\n".join(description)

        # Send the embed and add emojis.
        prompt = await ctx.send(embed=embed)
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
        # Get message ID from database and check first.

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
        if emoji.is_custom_emoji and emoji.id == ReactionRole.UPLOAD_ROLE.emoji.id:
            role_to_change = ReactionRole.UPLOAD_ROLE

        if not role_to_change:
            match emoji.name:
                case ReactionRole.UGC_ROLE.emoji:
                    role_to_change = ReactionRole.UGC_ROLE

                case ReactionRole.FEED_ROLE.emoji:
                    role_to_change = ReactionRole.FEED_ROLE

                case ReactionRole.FUN_ROLE.emoji:
                    role_to_change = ReactionRole.FUN_ROLE

                case _:
                    logger.warning("Unsupported emoji reaction.")

        role_ids = [role.id for role in member.roles]

        # Only adjust roles where applicable.
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


async def setup(bot: commands.Bot):
    await bot.add_cog(ReactionRoles(bot))
