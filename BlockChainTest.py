import BlockChain
import Block
import Transaction
import datetime
from random import randint

class BlockChainTest(BlockChain):

    def DoTest(self,n):
        store = Store()
        self.blockchain = BlockChain(store,randint(0,256),geneBlock)
        for i in range(n):
            self.Append()

        print(self._Blocks)


    def __del__(self):
        for block in self._Blocks:
            del block

    def Append(self,previousBlock, txs = None, nonce = None, difficulty = 1, miner = None, blockInterval = None):
        index = previousBlock.Index()
        timestamp = previousBlock.__timestamp + blockInterval
        txs = list() if txs == None else txs
        if nonce == None:
            new_block = block.Mine(index,difficulty,miner,previousBlock.Hash(),timestamp,txs)
        else:
            new_block = block.M
        this.Append(new_block)


if __name__ == '__main__':
    BlockChainTest(4)
