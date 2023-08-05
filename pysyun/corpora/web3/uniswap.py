from web3 import Web3
from pysyun.corpora.web3.abi import UniswapPairABI


class UniswapPairMetadata:

    def __init__(self, node_uri):
        self.node_uri = node_uri

    def process(self, addresses):
        web3 = Web3(Web3.HTTPProvider(self.node_uri))
        pair_abi = UniswapPairABI.get()

        result = []

        # List requested pairs
        for pair_contract_address in addresses:
            pair_contract = web3.eth.contract(address=pair_contract_address, abi=pair_abi)
            token0_address = pair_contract.functions.token0().call()
            token1_address = pair_contract.functions.token1().call()
            name0 = web3.eth.contract(address=token0_address, abi=pair_abi).functions.name().call()
            name1 = web3.eth.contract(address=token1_address, abi=pair_abi).functions.name().call()

            result.append({
                "name0": name0,
                "name1": name1
            })

        return result
