import os
import discord
from dotenv import load_dotenv
from config import PREFIX, PERMITTED_USERS

load_dotenv()

TOKEN = os.getenv('TOKEN')

class SelfBot(discord.AutoShardedClient):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user or message.author.id not in PERMITTED_USERS:
            return
        if message.content.startswith(PREFIX):
            pass

if __name__ == "__main__":
    bot = SelfBot(shard_count=1)
    for file in os.listdir('cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')

    bot.run(TOKEN)