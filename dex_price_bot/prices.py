from typing import Any, Dict

from discord import Activity, ActivityType
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.tasks import loop
from graph import Graph
from log import logger
from rpc import RPCUtils


class PriceHandler(commands.Cog):
    def __init__(self, bot: Bot, config: Dict[Any, Any]):
        self.bot = bot
        self.initial_start.start()
        self.graph = Graph()
        self.config = config

        self.src = config["token"]
        self.dst = config["price_unit"]
        self.src_symbol = None
        self.dst_symbol = None

        self.path = None
        self.rpc = RPCUtils(config["json_rpc_url"])
        self.price = 0

        self.display_format = config["display_format"]

    @loop(count=1)
    async def initial_start(self):
        await self.bot.wait_until_ready()
        for lp, constituents in self.config["liquidity_pools"].items():
            assert (
                len(constituents) == 2
            ), "A liquidity pool should only have two constituent tokens"
            for token in constituents:
                self.graph.add_node(token)
            self.graph.add_edge(*constituents, edge=lp)
        self.path = self.graph.find_path(
            self.config["token"], self.config["price_unit"]
        )
        self.src_symbol = self.rpc.symbol(self.src)
        self.dst_symbol = self.rpc.symbol(self.dst)
        await self.bot.change_presence(
            activity=Activity(
                type=ActivityType.watching, name=f"{self.src_symbol}/{self.dst_symbol}"
            )
        )

    @initial_start.after_loop
    async def after_initial_start(self):
        self.refresh_price_display.start()

    @loop(seconds=15)
    async def refresh_price_display(self):
        logger.debug("Checking price...")
        token_price = 1
        for edge in self.path:
            src, dest = edge
            src_bal = self.rpc.get_balance(src, self.graph.edges[tuple(sorted(edge))])
            dest_bal = self.rpc.get_balance(dest, self.graph.edges[tuple(sorted(edge))])
            ratio = src_bal / dest_bal
            token_price *= ratio
        if token_price != self.price:
            logger.info(
                f"Price of {self.src_symbol} updated to ${token_price:.6f} {self.dst_symbol}"
            )
            self.price = token_price

            for guild in self.bot.guilds:
                await guild.me.edit(
                    nick=self.display_format.format(
                        token=self.src_symbol,
                        price=self.price,
                        price_unit=self.dst_symbol,
                    )
                )
