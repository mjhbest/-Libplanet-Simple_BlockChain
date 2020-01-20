from BlockChain import BlockChain
from Policy import BlockPolicy
from Store import Store
from Block import Block
from datetime import timedelta, datetime
from time import sleep
from random import *
from Transaction import Transaction
from coincurve import PrivateKey

class BlockChainTest:
    def __init__(self,policy,store,id,n):
        genesisBlock = Block().Mine(0, 0,  None, datetime.utcnow(), [])
        self.blockChain = BlockChain(policy,store,id,genesisBlock)
        for i in range(n):
            print("-----------------------------------------------------------\n","_________",i+1,"' block Mining & Appending Start_________")
            block = self.MakeNewBlock(self.blockChain)
            self.blockChain.Append(block)
        print(self.blockChain)

    def MakeNewBlock(self,blocks):
        prevBlock = blocks.Tip()
        index = prevBlock.Index()+1
        txs = self.MakeTransactions(index)
        blocks.Store().Txs.update(txs)
        difficulty = BlockPolicy().GetNextBlockDifficulty(blocks)
        return Block().Mine(index,difficulty,prevBlock.Hash(),datetime.utcnow(),txs)

    def MakeTransactions(self,index):
        startTime = datetime.utcnow()
        randtime = randint(1000,5000)
        txlst = dict()
        cnt = 0
        tx = Transaction(index, PrivateKey(), getrandbits(8))
        txlst[str(index)] = tx
        # while(datetime.utcnow()-startTime<=timedelta(seconds=randtime)):  -> 이거 시간 설정에서 오류
        #     counter = getrandbits(8)
        #     id = str(index)+"-"+str(cnt)
        #     tx = Transaction(id, PrivateKey(), counter)
        #     cnt = cnt+1
        #     txlst[id] = tx
        #     sleep(randint(500,1000))
        return txlst


if __name__ == '__main__':
    #n = input()
    store = Store()
    policy = BlockPolicy()
    BlockChainTest(BlockPolicy(),Store(),"Test",15)
