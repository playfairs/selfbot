from discord import Client, Message
from discord.ext import commands
from discord.ext.commands import Cog, command, Context

class SelfReact(Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.reactions = {}

    @command(name="reaction", aliases=['ar', 'autoreact', 'selfreact'])
    async def selfreact(self, ctx: Context, user: discord.Member, emoji: str):
        if ctx.author.id not in PERMITTED_USERS:
            return

        self.reactions[user.id] = emoji

        await ctx.send(f"Set reaction '{emoji}' for {user.mention}.")

    @Cog.listener()
    async def on_message(self, message: Message):
        if message.author.id in self.reactions:
            try:
                await message.add_reaction(self.reactions[message.author.id])
            except discord.Forbidden:
                pass

    @command(name="reset")
    async def reset(self, ctx: Context):
        if ctx.author.id not in PERMITTED_USERS:
            return

        self.reactions = {}
        await ctx.send("Reset reactions.")