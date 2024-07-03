import json
from abi import abi
from typing import List, Dict, Any
from dataclasses import dataclass, asdict


@dataclass
class TokenABI:
    name: str
    abi: List[Dict[str, Any]]


class ABImanager:
    def __init__(self):
        self.abis = {
            "BEX_ABI": TokenABI("BEX_ABI", abi.bex_abi),
            "ERC20_ABI": TokenABI("ERC20_ABI", abi.erc_20_abi),
            "HONEY_ABI": TokenABI("HONEY_ABI", abi.honey_abi),
            "BEND_ABI": TokenABI("BEND_ABI", abi.bend_abi)
        }

    def get_abi(self, token_name):
        token_abi = self.abis.get(token_name.upper())
        if token_abi:
            return token_abi.abi
        else:
            raise ValueError(f"ABI for token {token_name} not found")

    def save_abis(self, filename='abis.json'):
        with open(filename, 'w') as f:
            json.dump({k: asdict(v) for k, v in self.abis.items()}, f, indent=2)

    def load_abis(self, filename='abis.json'):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.abis = {k: TokenABI(**v) for k, v in data.items()}

    def add_abi(self, token_name, abi):
        self.abis[token_name.upper()] = TokenABI(token_name.upper(), abi)