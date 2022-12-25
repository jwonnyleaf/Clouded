import os
import logging
from dotenv import load_dotenv

import hikari
import lightbulb

load_dotenv()

# bot = lightbulb.BotApp(token=os.getenv("BOT_TOKEN"), prefix="+")

# @bot.listen(hikari.ShardReadyEvent)
# async def ready_listener(_):
#     print("Clouded Bot is Ready!")

# @bot.command
# @lightbulb.command("ping", "checks the bot is alive")
# @lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
# async def ping(ctx: lightbulb.Context) -> None:
#     await ctx.respond("Pong!")


# bot.run()


class Bot(lightbulb.BotApp):
    def __init__(self) -> None:
        # Establishing Bot Configs from LightBulb.BotApp
        super().__init__(
            prefix=lightbulb.when_mentioned_or("+"),
            token=os.environ["BOT_TOKEN"],
            intents=hikari.Intents.ALL,
        )
    
    def run(self) -> None:
        self.event_manager.subscribe(hikari.StartingEvent, self.on_starting)
        self.event_manager.subscribe(hikari.StartedEvent, self.on_started)

        super().run(
            activity=hikari.Activity(
                name=f" # Guilds • V0.1",
                type=hikari.ActivityType.WATCHING
            )
        )

    async def on_starting(self, event: hikari.StartingEvent) -> None:
        print("Clouded is Booting Up...")

    async def on_started(self, event: hikari.StartedEvent) -> None:
        print(f"Succesfully Booted, initialized as Clouded.")
