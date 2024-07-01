from web3 import Web3
from web3.middleware import geth_poa_middleware
from .basic_instruments.self_check import Prepare_to_start
from web3.contract import Contract
from web3.types import TxParams
from icecream import ic

class Full_dive_into_W3(Prepare_to_start):
    def __init__(self, address,rpc, w3, private_key):
        super().__init__(address=address, w3=w3)
        self.rpc = rpc
        self.private_key = private_key


    def approve(self, token_address, spender_address):









full_dive = Full_dive_into_W3('ваша_адреса', 'URL_RPC_Berachain')

base_fee = full_dive.get_base_fee()
print(f"Base fee: {base_fee} Wei")

recommended_gas_prices = full_dive.get_recommended_gas_price()
print(f"Recommended gas prices: {recommended_gas_prices}")

average_gas_price = full_dive.get_average_gas_price()
print(f"Average gas price: {average_gas_price} Wei")

transaction = {
    'to': '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
    'value': Web3.to_wei(0.1, 'ether'),
    'gas': 21000,
    'gasPrice': full_dive.web3.eth.gas_price,
    'nonce': full_dive.get_transaction_count(),
}
estimated_gas = full_dive.estimate_gas_price_for_transaction(transaction)
print(f"Estimated gas for transaction: {estimated_gas}")



