from datetime import datetime
from coincurve import PrivateKey
from Block import Block
from Hashcash import Hashcash


class BlockChain:

    def __init__(self, policy=None, store=None, id=None, genesisBlock=None):
        self.__Id = id
        self.__Policy = policy
        self.__Store = store
        self.__Transaction = store.Txs
        self._Blocks = store.Blocks
        self.__IdChain = []
        self.Append(genesisBlock)

        if self.__IdChain[0] != genesisBlock:
            msg = "Genesis Block Error"
            raise Exception(msg)

    def __getitem__(self, item):
        if isinstance(item, int):
            blockHash = Hashcash()
            blockHash.Hash(self.__IdChain[item])

            if blockHash is None:
                raise IndexError
            return self.Blocks()[blockHash.Digest()]

        elif isinstance(item, Hashcash):

            if not item in Store:
                raise Exception()
            return self.Blocks()[Hashcash.Digest()]


    def MakeGenesisBlock(self, timestamp=None):
        return Block().Mine(0, 0,  None, timestamp, [])

    def containBlock(self, blockHash):
        return blockHash.Digest() in self.Blocks().keys() \
               and self.Blocks()[blockHash.Digest()].Index() <= self.Tip().Index()


    def getTransaction(self, txId):
        return self.__Transaction[txId]

    def Append(self, block):

        print(block.BlockBencodeFormatter())
        print("Appending Block :{} ".format(block.Hash()))
        if not self.Policy().ValidateNextBlock(self, block):
            raise ValueError("Append Failed. The block is invalid")
        print(">>> Validate_Done")
        for tx in block.Transactions():
            tx.nonce = tx.nonce + 1

        if block.Index() != 0 and block.PreviousHash() != self.Tip().Hash():
            raise Exception("Late Append")

        self.Blocks()[block.Hash()] = block
        self.__IdChain.append(block)
        self.__Store.AddBlock(block)
        print(">>> Appending_Succeed\n")

    def Tip(self):
        try:
            return self.__IdChain[-1]
        except IndexError:
            return None

    def Policy(self):
        return self.__Policy

    def Genesis(self):
        return self[0]

    def Id(self):
        return self.__Id

    def Count(self):
        return len(self.__IdChain)

    def Store(self):
        return self.__Store

    def Blocks(self):
        return self._Blocks
