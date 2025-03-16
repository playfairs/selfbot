from .massdm import MassDM

async def setup(bot: commands.Bot):
    await bot.add_cog(MassDM(bot))