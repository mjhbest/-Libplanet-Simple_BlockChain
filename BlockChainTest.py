from BlockChain import BlockChain
from Policy import BlockPolicy
from Store import Store
from Block import Block
from datetime import timedelta, datetime
from random import randint
from Transaction import Transaction

class BlockChainTest:
    def __init__(self,policy,store,id,n):
        genesisBlock = Block().Mine(0, 0,  None, datetime.utcnow(), [])
        self.blockChain = BlockChain(policy,store,id,genesisBlock)
        for i in range(n):
            print("-----------------------------------------------------------")
            print("_________",i+1,"' block Mining & Appending Start_________")
            block = self.MakeNewBlock(self.blockChain)
            self.blockChain.Append(block)
        print(self.blockChain)
    def MakeNewBlock(self,blocks):
        prevBlock = blocks.Tip()
        index = prevBlock.Index()+1
        txs = []
        difficulty = BlockPolicy().GetNextBlockDifficulty(blocks)
        return Block().Mine(index,difficulty,prevBlock.Hash(),(prevBlock.Timestamp()+timedelta(seconds=5000)),txs)

    def MakeTransactions(self,startTime):
        randtime = randint(1000,10000)
        while(datetime.utcnow()-startTime<=timedelta(seconds=randtime)):
         tx = Transaction()


if __name__ == '__main__':
    #n = input()
    store = Store()
    policy = BlockPolicy()
    BlockChainTest(BlockPolicy(),Store(),"Test",10)
