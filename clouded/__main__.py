import os
from bot.bot import Bot

if os.name != "nt":
    import uvloop

    uvloop.install()

def main() -> None:
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()