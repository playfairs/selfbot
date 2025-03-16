import discord
from discord import commands
from discord.ext import commands, tasks
from discord.ext.commands import Cog, command, Context
from config import MASSDM_CHANNEL_ID

class MassDM(Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.massdm_channel = self.bot.get_channel(MASSDM_CHANNEL_ID)

    @command(name="massdm")
    async def massdm(self, ctx: Context, *, message: str):
        if ctx.author.id not in PERMITTED_USERS:
            return

        friends = await ctx.author.create_dm().recipient_ids
        for user_id in friends:
            user = self.bot.get_user(user_id)
            if user is not None:
                try:
                    await user.send(message)
                except discord.Forbidden:
                    await ctx.send(f"Unable to message {user.name}")

    @command(name="spamdm")
    async def spamdm(self, ctx: Context, *, message: str):
        if ctx.author.id not in PERMITTED_USERS:
            return

        friends = await ctx.author.create_dm().recipient_ids
        for user_id in friends:
            user = self.bot.get_user(user_id)
            if user is not None:
                try:
                    await user.send(message)
                except discord.Forbidden:
                    await ctx.send(f"Unable to message {user.name}")