from tools.rpc import RPC

from dataclasses import dataclass

from web3 import Web3 as w3

b_url = RPC['BERACHAIN_RPC']['rpc_url']  # rpc url
w3 = w3(w3.HTTPProvider(b_url))


# save addresses with dataclass
@dataclass
class TokenAddresses:
    BERA: str
    WBERA: str
    HONEY: str
    WETH: str
    WBTC: str
    DAI: str
    USDT: str
    BGT: str
    USDC: str


contracts_checksum_addresses = TokenAddresses(
    BERA=w3.to_checksum_address("0x0000000000000000000000000000000000000000"),
    WBERA=w3.to_checksum_address("0x7507c1dc16935B82698e4C63f2746A2fCf994dF8"),
    HONEY=w3.to_checksum_address("0x0E4aaF1351de4c0264C5c7056Ef3777b41BD8e03"),
    WETH=w3.to_checksum_address("0x6E1E9896e93F7A71ECB33d4386b49DeeD67a231A"),
    WBTC=w3.to_checksum_address("0x286F1C3f0323dB9c91D1E8f45c8DF2d065AB5fae"),
    DAI=w3.to_checksum_address("0x806Ef538b228844c73E8E692ADCFa8Eb2fCF729c"),
    USDT=w3.to_checksum_address("0x05D0dD5135E3eF3aDE32a9eF9Cb06e8D37A6795D"),
    BGT=w3.to_checksum_address("0xbDa130737BDd9618301681329bF2e46A016ff9Ad"),
    USDC=w3.to_checksum_address("0xd6D83aF58a19Cd14eF3CF6fe848C9A4d21e5727c"),
)

bex_swap_address = w3.to_checksum_address("0x0d5862FDbdd12490f9b4De54c236cff63B038074")
honey_swap_address = w3.to_checksum_address("0x09ec711b81cD27A6466EC40960F2f8D85BB129D9")
usdc_pool_address = w3.to_checksum_address("0x36Af4FBAb8ebE58b4EfFE0D5d72CeFfc6eFc650A")
usdc_pool_liquidity_address = w3.to_checksum_address(
    "0x5479FbDef04302D2DEEF0Cc78f7D503d81fDFCC9"
)
weth_pool_liquidity_address = w3.to_checksum_address(
    "0x101f52c804C1C02c0A1D33442ecA30ecb6fB2434"
)
bex_approve_liquidity_address = w3.to_checksum_address(
    "0x0000000000000000000000000000000000696969"
)
weth_pool_address = w3.to_checksum_address("0xD3C962F3F36484439A41d0E970cF6581dDf0a9A1")
bend_borrows_address = w3.to_checksum_address(
    "0xfb618D1e361C362adDE4E148A4Dc85465a0A4A22"
)
bend_pool_address = w3.to_checksum_address("0x40C33CcbF44F554E1Bf8379BE1a5151Ab0F80f65")
ooga_booga_address = w3.to_checksum_address("0x6553444CaA1d4FA329aa9872008ca70AE6131925")
bera_name_address = w3.to_checksum_address('0x8D20B92B4163140F413AA52A4106fF9490bf2122')
