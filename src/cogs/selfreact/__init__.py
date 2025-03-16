from .selfreact import SelfReact

async def setup(bot: commands.Bot):
    await bot.add_cog(SelfReact(bot))