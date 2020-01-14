import hashlib
from datetime import datetime
from Block import Block
from rwlock import RwLock
from random import getrandbits
import coincurve

class BlockChain():

    def __init__(self,policy, store, id, genesisBlock):
        self.__Id = id
        self.__Policy = policy
        self.__Store = store
        self.__Transaction = store.txs
        self._Blocks = list(store.blks)
        self.__Rwlock = RwLock()
        self.__IdChain = []

        if Count == 0:
            Append(genesisBlock)
        elif self._Blocks[self.__IdChain[0]] != genesisBlock:
            msg = "Genesis Block Error"
            raise Exception(msg)

    def __del__(self):
        del self.__Rwlock

    def __getitem__(self, item):
        if isinstance(item, int):
            self.Locker().acquire_r()
            try:
                blockHash = hashlib.sha256()
                blockHash.update(self.Store().Blo[item])

                if blockHash == None:
                    raise IndexError
                return self._Blocks[blockHash.digest()]
            finally:
                self.Locker().release_r()

        elif isinstance(item, hashlib.sha256()):

            if not item in Store:
                raise KeyError

            self.Locker().acquire_r()
            try:
                return self._Blocks[blockHash]
            finally:
                self.__Rwlock.release_r()

    def MakeGenesisBlck(self, privateKey = None, timestamp = None):
        if privateKey == None:
            privatekey = PrivateKey()
        txs = []
        return geneBlock.Mine(0,0,privateKey,None, timestamp,txs)


    def containBlock(self, blockHash):
        self.__Rwlock.acquire_r()
        try:
            return blockHash in self._Blocks.keys() and self._Blocks[blockHash].Index() <= self.Tip().Index
        finally:
                self.rwlock.release_r()


    def getTransaction(self, txId):
        self.Locker().acquire_r()
        try:
            return self.__Transaction[txId]
        finally:
            self.Locker().release_r()


    def Append(self, block, currentTime = None):
        evaluation = True #evaluation check
        for tx in block.Transcations():
            evaluation = evaluation and tx.iseval

        if not evaluations:
            raise Exception("Argument Exception : Evaluation have to be done before the rendering")
        if currentTime == None:
            Append(block, datetime.utcnow())


        self.Locker().acquire_r()
        if not self.Policy().ValidateNextBlock(self,block):
            raise ValueError("Append Failed. The block is invalid")

        for tx in block.Transcations(): #No Case handling for chainging nonce within appending
            tx.nonce = tx.nonce + 1
        self.Locker().release_r()

        #modification
        self.__Rwlock.acquire_w()
        if block.PreviousHash() != self.Tip().Hash():
            raise Exception("Late Append")

        self._Blocks[block.Hash()] = block
        self.__Store.AddBlock(block.Hash())
        #No consdieration for Tx evaluation & NonceChanged issues

        self.__Rwlock.acquire_r()
        print("Appending Block{} succeed".format(block.Hash()))


    def Tip(self):
        try:
            return self.__IdChain[-1]
        except IndexError:
            return None

    def Locker(self):
        return self.__Rwlock

    def Policy(self):
        return self.__Policy

    def Genesis(self):
        return this[0]

    def Id(self):
        return self.__Id

    def BlockHahses(self):
        return IterateBlockHashes()

    def Count(self):
        return len(self.__IdChain)

    def Store(self):
        return self.__Store

    def BlockList(self):
        return self.__IdChain











