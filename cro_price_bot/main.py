from typing import Any, Dict

import click
from discord.ext.commands import Bot
from prices import PriceHandler

from config import load_config

bot = Bot("!")


def main(config: Dict[Any, Any]):
    handler = PriceHandler(bot, config)
    bot.add_cog(handler)
    bot.run(config["discord_token"])


@click.command()
@click.option(
    "-c", "--config", required=True, type=click.Path(), help="Location of config file."
)
def entrypoint(config: str):
    cfg = load_config(config)
    main(cfg)


if __name__ == "__main__":
    entrypoint()
