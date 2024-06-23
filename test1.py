from helpers import Full_dive_into_W3
from web3 import Web3 as w3
from tools.rpc import RPC
import asyncio

rpc = RPC['BERACHAIN_RPC']['rpc']
w3 = w3(w3.HTTPProvider(rpc))
async def main():
    full_dive = Full_dive_into_W3(rpc, w3)
    # is_connected = await full_dive.check_connection()
    # print(f"Connected: {is_connected}")

    gas_price = await full_dive.gas_price()
    print(f"Gas Price: {gas_price}")

    block_number = await full_dive.get_block_number()
    print(f"Block Number: {block_number}")


asyncio.run(main())