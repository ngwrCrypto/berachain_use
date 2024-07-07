import sys
import os

from web3 import Web3
from icecream import ic
from dotenv import load_dotenv

from web3.contract import Contract
from abi.ABIs_manager import ABImanager
from web3.middleware import geth_poa_middleware
from web3.types import TxParams, ChecksumAddress, HexBytes
from helpers.basic_instruments.self_check import Prepare_to_start

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
    def __init__(self, user_address, private_key):
        super().__init__(user_address=user_address)
        self.abi_manager = ABImanager()
        self.private_key = private_key

    def set_contract_to_interaction(self, token_address):
        return self.web3.eth.contract(address=self.web3.to_checksum_address(token_address),
                                                abi=self.abi_manager.get_abi('ERC20_ABI')
                                      )

    def get_balance_of_token(self, token_address):
        return self.web3.eth.contract(address=self.web3.to_checksum_address(token_address),
                                      abi=self.abi_manager.get_abi('ERC20_ABI')
                                      ).functions.balanceOf(self.user_address).call()

    def approve(self, token_address, spender_address, amount):
        approve_token_contract = self.set_contract_to_interaction(token_address)

        allowance_address: int = approve_token_contract.functions.allowance(self.user_address, spender_address).call()
        ic(allowance_address)
        dict_transaction: TxParams = {
            'gas': self.get_average_gas_price(),  #!!!
            'gasPrice': self.web3.eth.gas_price * 10,
            'nonce': self.web3.eth.get_transaction_count(self.user_address),
        }
        approve_amount: int = 2 ** 256 - 1 if not amount else amount

        transaction = approve_token_contract.functions.approve(
            spender_address, approve_amount
        ).build_transaction(dict_transaction)

        signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
        txn_hash: HexBytes = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        ic(txn_hash.hex())
        return txn_hash.hex()

#
# c = Full_dive_into_W3(user_address=os.getenv('WALLET'), private_key=os.getenv('PRIVATE_KEY'))
# print(c.approve())
p_key = os.getenv("PRIVATE_KEY")
w3 = Web3(Web3.HTTPProvider("https://bartio.rpc.berachain.com/"))

ic(w3.eth.get_balance(w3.eth.account.from_key(os.getenv("PRIVATE_KEY")).address))
ic(w3.from_wei((w3.eth.get_balance(w3.to_checksum_address(w3.eth.account.from_key(p_key).address))), 'Ether'))


contract: Contract = w3.eth.contract(
    address=w3.to_checksum_address('0x0000000000000000000000000000000000000000'),
    abi='[{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"address","name":"receiver","type":"address"},{"internalType":"address[]","name":"assetsIn","type":"address[]"},{"internalType":"uint256[]","name":"amountsIn","type":"uint256[]"}],"name":"addLiquidity","outputs":[{"internalType":"address[]","name":"shares","type":"address[]"},{"internalType":"uint256[]","name":"shareAmounts","type":"uint256[]"},{"internalType":"address[]","name":"liquidity","type":"address[]"},{"internalType":"uint256[]","name":"liquidityAmounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"enumIERC20DexModule.SwapKind","name":"kind","type":"uint8"},{"components":[{"internalType":"address","name":"poolId","type":"address"},{"internalType":"address","name":"assetIn","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address","name":"assetOut","type":"address"},{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"bytes","name":"userData","type":"bytes"}],"internalType":"structIERC20DexModule.BatchSwapStep[]","name":"swaps","type":"tuple[]"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"batchSwap","outputs":[{"internalType":"address[]","name":"assets","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"address[]","name":"assetsIn","type":"address[]"},{"internalType":"uint256[]","name":"amountsIn","type":"uint256[]"},{"internalType":"string","name":"poolType","type":"string"},{"components":[{"components":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"weight","type":"uint256"}],"internalType":"structIERC20DexModule.AssetWeight[]","name":"weights","type":"tuple[]"},{"internalType":"uint256","name":"swapFee","type":"uint256"}],"internalType":"structIERC20DexModule.PoolOptions","name":"options","type":"tuple"}],"name":"createPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"address","name":"baseAsset","type":"address"},{"internalType":"address","name":"quoteAsset","type":"address"}],"name":"getExchangeRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"getLiquidity","outputs":[{"internalType":"address[]","name":"asset","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"getPoolName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"getPoolOptions","outputs":[{"components":[{"components":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"weight","type":"uint256"}],"internalType":"structIERC20DexModule.AssetWeight[]","name":"weights","type":"tuple[]"},{"internalType":"uint256","name":"swapFee","type":"uint256"}],"internalType":"structIERC20DexModule.PoolOptions","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"address[]","name":"assets","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"name":"getPreviewAddLiquidityNoSwap","outputs":[{"internalType":"address[]","name":"shares","type":"address[]"},{"internalType":"uint256[]","name":"shareAmounts","type":"uint256[]"},{"internalType":"address[]","name":"liqOut","type":"address[]"},{"internalType":"uint256[]","name":"liquidityAmounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"address[]","name":"liquidity","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"name":"getPreviewAddLiquidityStaticPrice","outputs":[{"internalType":"address[]","name":"shares","type":"address[]"},{"internalType":"uint256[]","name":"shareAmounts","type":"uint256[]"},{"internalType":"address[]","name":"liqOut","type":"address[]"},{"internalType":"uint256[]","name":"liquidityAmounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"enumIERC20DexModule.SwapKind","name":"kind","type":"uint8"},{"components":[{"internalType":"address","name":"poolId","type":"address"},{"internalType":"address","name":"assetIn","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address","name":"assetOut","type":"address"},{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"bytes","name":"userData","type":"bytes"}],"internalType":"structIERC20DexModule.BatchSwapStep[]","name":"swaps","type":"tuple[]"}],"name":"getPreviewBatchSwap","outputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getPreviewBurnShares","outputs":[{"internalType":"address[]","name":"assets","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"address[]","name":"assets","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"name":"getPreviewSharesForLiquidity","outputs":[{"internalType":"address[]","name":"shares","type":"address[]"},{"internalType":"uint256[]","name":"shareAmounts","type":"uint256[]"},{"internalType":"address[]","name":"liquidity","type":"address[]"},{"internalType":"uint256[]","name":"liquidityAmounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"getPreviewSharesForSingleSidedLiquidityRequest","outputs":[{"internalType":"address[]","name":"assets","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"enumIERC20DexModule.SwapKind","name":"kind","type":"uint8"},{"internalType":"address","name":"pool","type":"address"},{"internalType":"address","name":"baseAsset","type":"address"},{"internalType":"uint256","name":"baseAssetAmount","type":"uint256"},{"internalType":"address","name":"quoteAsset","type":"address"}],"name":"getPreviewSwapExact","outputs":[{"internalType":"address","name":"asset","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"address","name":"assetIn","type":"address"},{"internalType":"uint256","name":"assetAmount","type":"uint256"}],"name":"getRemoveLiquidityExactAmountOut","outputs":[{"internalType":"address[]","name":"assets","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"address","name":"assetOut","type":"address"},{"internalType":"uint256","name":"sharesIn","type":"uint256"}],"name":"getRemoveLiquidityOneSideOut","outputs":[{"internalType":"address[]","name":"assets","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"getTotalShares","outputs":[{"internalType":"address[]","name":"assets","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"address","name":"withdrawAddress","type":"address"},{"internalType":"address","name":"assetIn","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"}],"name":"removeLiquidityBurningShares","outputs":[{"internalType":"address[]","name":"liquidity","type":"address[]"},{"internalType":"uint256[]","name":"liquidityAmounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"address","name":"withdrawAddress","type":"address"},{"internalType":"address","name":"assetOut","type":"address"},{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address","name":"sharesIn","type":"address"},{"internalType":"uint256","name":"maxSharesIn","type":"uint256"}],"name":"removeLiquidityExactAmount","outputs":[{"internalType":"address[]","name":"shares","type":"address[]"},{"internalType":"uint256[]","name":"shareAmounts","type":"uint256[]"},{"internalType":"address[]","name":"liquidity","type":"address[]"},{"internalType":"uint256[]","name":"liquidityAmounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"enumIERC20DexModule.SwapKind","name":"kind","type":"uint8"},{"internalType":"address","name":"poolId","type":"address"},{"internalType":"address","name":"assetIn","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address","name":"assetOut","type":"address"},{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swap","outputs":[{"internalType":"address[]","name":"assets","type":"address[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"}]'

)
# ic(w3.eth.get_block('latest'))
latest_block = w3.eth.get_block('latest')
if 'baseFeePerGas' in latest_block:
    base_fee = latest_block['baseFeePerGas']
    ic(base_fee)

gas_price = w3.eth.generate_gas_price()
ic(gas_price)