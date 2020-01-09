import hashlib
from datetime import datetime
from Block import Block


class BlockChain():

    def __init__(policy, store, id, genesisBlock):
        self._Id = id
        self._Policy = policy
        self._Store = store
        self._transaction = store.txs
        self._blocks = store.blks
        self._rwlock = RwLock()
        self._IdChain = []


        if Count == 0:
            Append(genesisBlock)
        elif Genesis != genesisBlock:
            msg = "Genesis Block Error"
            raise Exception(msg)

    def __del__(self):
        del self._rwlock

    def __getitem__(self, item):

        if isinstance(item, int):
            self._rwlock.acquire_r()
            try:
                blockHash = hashlib.sha256()
                blockHash.update(Store.Blocks[item])

                if blockHash == None:
                    raise IndexError
                return self._blocks[blockHash.digest()]
            finally:
                self._rwlock.release_r()

        elif isinstance(item, hashlib.sha256()):

            if not item in Store:
                raise KeyError

            self._rwlock.acquire_r()
            try:
                return self._blocks[blockHash]
            finally:
                self._rwlock.release_r()

    def MakeGenesisBlck(self, action = None, privateKey = None, timestamp = None):
        if privateKey == None:
            privateKey = PrivateKey()
        if action == None:
            action = []
        geneBlock = Block()
        return geneBlock.Mine(0,0,privateKey,None, timestamp) #Tx 제외시킴


    def containBlock(self, blockHash):
        self._rwlock.acquire_r()
        try:
            return (blockHash in self._blocks) and self._blocks[blockHash] <= Tip.Index and blockHash == this[]
        finally:
                self.rwlock.release_r()

    def getTransaction(self, txId):
        self._rwlock.acquire_r()
        try:
            return self._transaction[txId]
        finally:
            self._rwlock.release_r()

    def Append(self, block, currentTime = None):
        if currentTime == None:
            Append(block, datetime.utcnow())

        if not self.Policy().ValidateNextBlock(self,block):
            raise ValueError("Append Failed. The block is invalid")
        self._rwlock.release_w()
        prevTip = self.Tip()
        self._blocks[block.Hash()] = block







    def Tip(self):
        try:
            return this[-1]
        except IndexError:
            return None

    def Policy(self):
        return self._Policy

    def Genesis(self):
        return this[0]

    def Id(self):
        return self._Id

    def BlockHahses(self):
        return IterateBlockHashes()

    def Count(self):
        return len(self.IdChain)

    def Store(self):
        return self._Store











