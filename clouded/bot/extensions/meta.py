import hikari
import lightbulb

meta_plugin = lightbulb.Plugin("Meta")

@meta_plugin.command()
@lightbulb.command("ping", "Get the bot's latency.")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    latency = ctx.bot.heartbeat_latency * 1_000
    await ctx.respond(
        f"Pong! Latency: {latency:,.0f} ms."
    )

def load(bot):
    bot.add_plugin(meta_plugin)

def unload(bot):
    bot.remove_plugin(meta_plugin)