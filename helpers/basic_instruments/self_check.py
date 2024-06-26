from web3 import Web3
from web3.middleware import geth_poa_middleware
# from B_Chain.tools import RPC
RPC = {
    'BERACHAIN_RPC': {
        "network": "Berachain bArtio Testnet",
        "rpc_url": "https://bartio.rpc.berachain.com/",
        "ChainID": 80084,
        "symbol": "BERA",
        "block_explorer": "https://bartio.beratrail.io/",
    },

}
class Prepare_to_start:
    def __init__(self, address):
        self.web3 = Web3(Web3.HTTPProvider(RPC['BERACHAIN_RPC']['rpc_url']))
        self.address = self.web3.to_checksum_address(address)
        # async def check_connection(self):
        #     return await self.web3.is_connected()

    def is_valid_adress(self):
        return self.web3.is_address(self.address)

    def check_connection(self):
        return self.web3.is_connected()

    def latest_block(self):
        return self.web3.eth.get_block('latest')

    def gas_price(self):
        return self.web3.eth.gas_price

    def get_balance(self):
        return self.web3.eth.get_balance(self.address)

    def get_transaction_count(self):
        return self.web3.eth.get_transaction_count(self.address)


