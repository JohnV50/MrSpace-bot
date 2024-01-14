# env stuff
import datetime
import os
from typing import Callable

import discord
from discord.ext import commands
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
        self.mongo: AsyncIOMotorClient = AsyncIOMotorClient(os.getenv("MONGO_URL"))

    async def setup_hook(self):
        # reaction roles
        await self.load_extension("commands.reaction_roles")

        # sendcmd stuff
        await self.load_extension("commands.sendcmds.sendroles")
        await self.load_extension("commands.sendcmds.sendrulestwo")
        await self.load_extension("commands.sendcmds.sendrules")
        await self.load_extension("commands.sendcmds.sendfaq")
        await self.load_extension("commands.sendcmds.sendsocial")
        await self.load_extension("commands.sendcmds.sendserver")
        await self.load_extension("commands.sendcmds.sendlink")
        await self.load_extension("commands.sendcmds.sendinfo")

        # regular cmds
        await self.load_extension("commands.ping")
        await self.load_extension("commands.youtube")
        await self.load_extension("commands.tiktok")
        await self.load_extension("commands.twitter")
        await self.load_extension("commands.roblox")

        bot.remove_command("help")  # remove the default help command
        await self.load_extension("commands.help")  # add my own help command

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

bot = MyBot(command_prefix=".", intents=intents)


# on_message
@bot.event
async def on_message(message):
    if not message.author.bot:  # check to make sure the author isn't a bot
        await bot.process_commands(message)


# token
if __name__ == "__main__":
    token = os.getenv("token")
    bot.run(token)
