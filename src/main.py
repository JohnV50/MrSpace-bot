# env stuff
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# for bot uptime tracking
start_time = []

# intent

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


# connect other commands


class MyBot(commands.Bot):
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
