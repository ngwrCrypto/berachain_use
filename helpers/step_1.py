from web3 import Web3
from web3.middleware import geth_poa_middleware


class Full_dive_into_W3:
    def __init__(self, rpc, w3):
        self.rpc = rpc
        self.web3 = w3

    # async def check_connection(self):
    #     return await self.web3.is_connected()

    async def gas_price(self):
        return self.web3.eth.gas_price

    async def get_block_number(self):
        return self.web3.eth.block_number










