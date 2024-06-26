from web3 import Web3
from web3.middleware import geth_poa_middleware
from .basic_instruments.self_check import Prepare_to_start


class Full_dive_into_W3(Prepare_to_start):
    def __init__(self, rpc, w3):
        super().__init__()
        self.rpc = rpc
        self.web3 = w3

    # async def check_connection(self):
    #     return await self.web3.is_connected()












