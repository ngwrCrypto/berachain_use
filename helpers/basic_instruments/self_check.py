from web3 import Web3
import time
from web3.gas_strategies.time_based import (
    medium_gas_price_strategy as mid_price,
    fast_gas_price_strategy as fast_price,
    slow_gas_price_strategy as low_life_price,
    glacial_gas_price_strategy as newer_willBe_price,)

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
        self._latest_block = None
        self._latest_block_time = 0
        self.BLOCK_FRESHNESS_TRESHOLD = 12
        # async def check_connection(self):
        #     return await self.web3.is_connected()

    def is_valid_adress(self):
        return self.web3.is_address(self.address)

    def check_connection(self):
        return self.web3.is_connected()

    def gas_price(self):
        return self.web3.eth.gas_price

    def get_balance(self):
        return self.web3.eth.get_balance(self.address)

    def get_transaction_count(self):
        assert self.check_connection(), 'Web3 is not connected'
        return self.web3.eth.get_transaction_count(self.address)

    def latest_block(self):
        current_time = time.time()
        if self._latest_block is None or current_time - self._latest_block_time > self.BLOCK_FRESHNESS_TRESHOLD:
            self._latest_block = self.web3.eth.get_block('latest')
            self._latest_block_time = current_time

        return self._latest_block

    def get_base_fee(self):
        latest_block = self.web3.eth.get_block('latest')
        if 'baseFeePerGas' in latest_block:
            base_fee = latest_block['baseFeePerGas']
            return base_fee
        else:
            base_fee = self.web3.eth.gas_price
            return base_fee

    def get_recommended_gas_price(self):
        base_fee = self.get_base_fee()
        gas_price = self.web3.eth.generate_gas_price()
        if gas_price and gas_price > base_fee:
            return gas_price
        else:
            return base_fee

    def get_average_gas_price(self):
        base_fee = self.get_base_fee()
        recommended_gas_price = self.get_recommended_gas_price()

        return max(recommended_gas_price, base_fee)

    def estimate_gas_for_transaction(self, transaction):
        return self.web3.eth.estimate_gas(transaction)



