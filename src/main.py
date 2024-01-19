# env stuff
import datetime
import os
from typing import Callable

import discord
import certifi
from discord.ext import commands
from discord.ext.commands import CheckFailure, CommandError, CommandNotFound, Context, MissingRequiredArgument
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

# for bot uptime tracking
start_time = []

# intent

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


# connect other commands


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.started_at: datetime.datetime = datetime.datetime.utcnow()
        self.mongo: AsyncIOMotorClient = AsyncIOMotorClient(os.getenv("MONGO_URL"), tlsCAFile=certifi.where())

    async def setup_hook(self):

        # sendcmd stuff
        sendcmd_files = os.listdir("src/commands/sendcmds")
        for file in sendcmd_files:
            if file.endswith(".py"):
                await self.load_extension(f"commands.sendcmds.{file[:-3]}")
        print("Loaded sendcmds")
        # regular cmds
        bot.remove_command("help")
        files = os.listdir("src/commands")
        for file in files:
            if file.endswith(".py"):
                await self.load_extension(f"commands.{file[:-3]}")
        print("Loaded commands")
    async def on_ready(self):
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name=".help")
        )  # change bot status
    
    @property
    def uptime(self) -> datetime.timedelta:
        return datetime.datetime.utcnow() - self.started_at

    async def fetch_database_data(
        self, constructor: Callable, item_id: str, *aspects, domain: str = "guilds"
    ) -> object:
        item_id = str(item_id)

        item = await self.mongo.bloxlinkLIVE[domain].find_one(
            {"_id": item_id}, {x: True for x in aspects}
        ) or {"_id": item_id}

        if item.get("_id"):
            item.pop("_id")

        item["id"] = item_id

        return constructor(**item)

    async def update_database_item(self, item_id: str, domain: str = "guilds", **aspects) -> None:
        item_id = str(item_id)

        unset_aspects = {}
        set_aspects = {}
        for key, val in aspects.items():
            if val is None:
                unset_aspects[key] = ""
            else:
                set_aspects[key] = val

        # update database
        await self.mongo.bloxlinkLIVE[domain].update_one(
            {"_id": item_id}, {"$set": set_aspects, "$unset": unset_aspects}, upsert=True
        )


# prefix

bot: MyBot = MyBot(command_prefix=".", intents=intents)


# on_message
@bot.event
async def on_message(message):
    if not message.author.bot:  # check to make sure the author isn't a bot
        await bot.process_commands(message)


@bot.event
async def on_command_error(ctx: Context, error: CommandError):
    if (ctx.command is not None and ctx.command.has_error_handler()) or (
        ctx.cog is not None and ctx.cog.has_error_handler()
    ):
        # Ignore commands that have their own error handlers.
        return

    match error:
        case CommandNotFound():
            # Get the logger to shush when people mistype a command
            return

        case CheckFailure():
            await ctx.reply(
                content="You do not have permissions to use this command!",
                mention_author=False,
                delete_after=5.0,
                ephemeral=True,
            )

            if not ctx.interaction:
                await ctx.message.delete()

        case MissingRequiredArgument():
            param = error.param.name
            message = f"You're missing the required {param} argument!"

            await ctx.reply(
                content=message,
                mention_author=False,
                delete_after=5.0,
                ephemeral=True,
            )

            if not ctx.interaction:
                await ctx.message.delete()

        case _ as err:
            await ctx.reply(
                content=err,
                mention_author=False,
                ephemeral=True,
            )
            raise err


# token
if __name__ == "__main__":
    token = os.getenv("token")
    bot.run(token)
