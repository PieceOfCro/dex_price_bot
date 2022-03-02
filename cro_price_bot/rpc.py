import math

import aiohttp
from log import logger
from web3 import Web3


class RPCUtils:
    def __init__(self, json_rpc_url: str):
        self.rpc = json_rpc_url
        logger.info(f"RPC url set as: {json_rpc_url}")

    async def decimals(self, token: str) -> int:
        func_selector = Web3.sha3(text="decimals()").hex()[:10]
        padded_nft_holder = func_selector + "0" * 64
        request_json = {
            "jsonrpc": "2.0",
            "method": "eth_call",
            "params": [{"to": token, "data": padded_nft_holder}, "latest"],
            "id": 67,
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.post(self.rpc, json=request_json) as r:
                res = await r.json()
                return Web3.toInt(hexstr=res["result"])

    async def symbol(self, token: str) -> str:
        func_selector = Web3.sha3(text="symbol()").hex()[:10]
        padded_nft_holder = func_selector + "0" * 64
        request_json = {
            "jsonrpc": "2.0",
            "method": "eth_call",
            "params": [{"to": token, "data": padded_nft_holder}, "latest"],
            "id": 67,
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.post(self.rpc, json=request_json) as r:
                res = await r.json()
                bytes = Web3.toBytes(hexstr=res["result"])
                bytes = bytes.replace(b"\x00", b"")
                return bytes.decode()[2:]

    async def get_balance(self, lp_token: str, lp_contract: str) -> int:
        decimals = await self.decimals(lp_token)
        func_selector = Web3.sha3(text="balanceOf(address)").hex()[:10]
        padded_nft_holder = func_selector + lp_contract[2:].zfill(64)
        request_json = {
            "jsonrpc": "2.0",
            "method": "eth_call",
            "params": [{"to": lp_token, "data": padded_nft_holder}, "latest"],
            "id": 67,
        }
        async with aiohttp.ClientSession() as cs:
            async with cs.post(self.rpc, json=request_json) as r:
                res = await r.json()
                return Web3.toInt(hexstr=res["result"]) / math.pow(10, decimals)
