import sys
import os

from web3 import Web3

from web3.middleware import geth_poa_middleware
from helpers.basic_instruments.self_check import Prepare_to_start
from abi.ABIs_manager import ABImanager
from web3.contract import Contract
from web3.types import TxParams, ChecksumAddress, HexBytes
from icecream import ic
from dotenv import load_dotenv

load_dotenv()
# import environ
#
# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )

d = os.getenv("WALLET")
ic(d)

class Full_dive_into_W3(Prepare_to_start):
    def __init__(self, address, private_key):
        super().__init__(address=address)
        self.abi_manager = ABImanager()
        self.private_key = private_key

    def approve(self, token_address, spender_address, amount, approve_token_address):
        token_contract = self.web3.eth.contract(address=self.web3.to_checksum_address(token_address),
                                                abi=self.abi_manager.get_abi('ERC20_ABI'))
        allowance: int = token_contract.functions.allowance(self.address, spender_address).call()
        ic(allowance)
        dict_transaction: TxParams = {
            'gas': 210000,
            'gasPrice': self.web3.eth.gas_price * 10,
            'nonce': self.web3.eth.get_transaction_count(self.address),
        }
        approve_amount: int = 2 ** 256 - 1

        transaction = token_contract.functions.approve(
            spender_address, approve_amount
        ).build_transaction(dict_transaction)

        signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        txn_hash: HexBytes = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        ic(txn_hash.hex())
        return txn_hash.hex()


c = Full_dive_into_W3(address=os.getenv('WALLET'), private_key=os.getenv('PRIVATE_KEY'))
print(c)
