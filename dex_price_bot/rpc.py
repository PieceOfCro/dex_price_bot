import json
import math

from log import logger
from web3 import HTTPProvider, Web3


class RPCUtils:
    def __init__(self, json_rpc_url: str):
        self.rpc = json_rpc_url
        self.w3 = Web3(HTTPProvider(json_rpc_url))
        logger.info(f"RPC url set as: {json_rpc_url}")
        self.abi = json.load(open("erc20.json", "r"))

    def decimals(self, token: str) -> int:
        contract = self.w3.eth.contract(token, abi=self.abi)
        return contract.functions.decimals().call()

    def symbol(self, token: str) -> str:
        contract = self.w3.eth.contract(token, abi=self.abi)
        return contract.functions.symbol().call()

    def balanceOf(self, lp_token: str, lp_contract: str) -> int:
        contract = self.w3.eth.contract(lp_token, abi=self.abi)
        return contract.functions.balanceOf(lp_contract).call()

    def get_balance(self, lp_token: str, lp_contract: str) -> float:
        balance_of = self.balanceOf(lp_token, lp_contract)
        decimals = self.decimals(lp_token)
        return balance_of / math.pow(10, decimals)
