import BlockChain
import Policy
import Store
from Block import *
import Transaction
import datetime
from coincurve import *

class BlockChainTest:
    def __init__(self,policy,store,id,genesisBlock,n):
        self.blockChain = BlockChain(policy,store,id,genesisBlock)
        for i in range(n):
            self.Attach()
        # print(self._Blocks)

    #임의의 블럭을 생성해서 BlockChain에 Append 시키는 method
    def Attach(self,previousBlock = None, txs = list(), nonce = None, difficulty = 1, miner = None, blockInterval = None):
        prevBlock = self.blockChain.Tip() if previousBlock == None else previousBlock
        index = prevBlock.Index()+1
        timestamp = prevBlock.__timestamp + blockInterval

        #nonce Handling 필요 nonce 가 0인경우
        new_block = Block().Mine(index,difficulty,miner,prevBlock.Hash(),timestamp,txs)

        selfblockChain.Append(new_block)


if __name__ == '__main__':
    #n = input()
    geneBlock = Block().Mine(0,0,None,None,None,list())
    store = Store()
    policy = BlockPolicy()
    BlockChainTest(BlockPolicy(),Store(),"Test",geneBlock,3)
