import discord
from discord.ext import commands

# env stuff
import os
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
        await self.load_extension("commands.sendroles")
        await self.load_extension("commands.sendrulestwo")
        await self.load_extension("commands.sendrules")
        await self.load_extension("commands.sendfaq")
        await self.load_extension("commands.sendsocial")
        await self.load_extension("commands.sendserver")
        await self.load_extension("commands.sendlink")
        await self.load_extension("commands.sendinfo")
        bot.remove_command('help') # remove the default help command
        await self.load_extension("commands.help") # add my own help command

    async def on_ready(self):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help")) # change bot status


# prefix

bot = MyBot(command_prefix='.', intents=intents)


# on_message
@bot.event
async def on_message(message):
    if not message.author.bot: # check to make sure the author isn't a bot
        await bot.process_commands(message)


# token
if __name__ == "__main__":
    token = os.getenv("token")
    bot.run(token)