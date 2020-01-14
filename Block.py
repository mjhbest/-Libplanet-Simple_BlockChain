import datetime
import hashlib
from bencodex import *

class Block:

    __TimestampFormat = "yyyy--MM-ddTHH:mm:ss.ffffffZ"
    __TimestampThreshold = datetime.timedelta(seconds=900)

    # initialize
    def __init__(self, index=None,difficulty=None, nonce=None, miner=None, previousHash=None,timestamp=None,txs=None, rb = None):
        if rb == None:
            self.__index = index
            self.__difficulty = difficulty
            self.__nonce = nonce
            self.__miner = miner
            self.__previousHash = previousHash
            self.__timestamp = timestamp
            self.__transactions = txs
            self.__hash = hashlib.sha256(self.ToBencodex())

        else:
            __block(rb)


    def __block(self,rb):
        self.__index = rb.__index
        self.__difficulty=rb.__difficult
        self.__nonce=Nonce(rb.__nonce)
        self.__miner=None if rb.__miner == None else Address(rb.__miner)
        self.__previousHash=None if rb.__previousHash == None else rb.__previousHash
        self.__timestamp=rb.__timestamp
        self.__transactions=rb.__transactions
        self.__hash = hashlib.sha256(self.ToBencodex())

    def Hash(self):
        return self.__hash

    def Index(self):
        return self.__index

    def Difficulty(self):
        return self.__difficulty

    def Nonce(self):
        return self.__nonce

    def Miner(self):
        return self.__miner

    def PreviousHash(self):
        return self.__previousHash

    def Timestamp(self):
        return self.__timestamp

    def Transcations(self):
        return self.__transactions
 
    def Mine( self, index, difficulty, miner,previousHash , timestamp, transactions):

        def MakeBlock(n):
            return Block(index, difficulty, n, miner, previousHash, timestamp, transactions)

        emptyNonce = MakeBlock(0).ToBencodex()
        oneByteNoce = MakeBlock(1).ToBencodex()
        offset = 0 #find location of Nonce
        while offset < len(emptyNonce) and emptyNonce[offset] == oneByteNoce[offset]:
            offset = offset + 1

        stampPrefix = emptyNonce[0:offset]
        stampSuffix = emptyNonce[offset:len(emptyNonce)]

        def Stamp(n):
            nLen = len(bytearray(n))

            nLenStr = str(nLen).encode()
            stamp = copy.deepcopy(stampPrefix) + copy.deepcopy(nLenSter) + bytearray(0x3a) + copy.deepcopy(stampSuffix)
            return stamp

        nonce = Hashcash.Answer(Stamp(n),self.__difficulty)

        return MakeBlock(nonce)


    def FromBencodex(self,encoded):
        return loads(encoded)

    def ToBencodex(self): #hash usage in original codes
        return dumps(self.ToDictFormatter())

    def ToDictFormatter(self):
        d = {
            'index': self.__index,
            'difficulty': self.__difficulty,
            'nonce': self.__nonce,
            'miner': self.__miner,
            'previousHash': self.__previousHash,
            'timestamp': self.__timestamp,
            'transactions': self.__transactions
        }
        return d


    def Validate(self,currentTime):
        if currentTime + self.__TimestampThreshold < self.__timestamp:

            raise Exception(
                "The block {}'s timestamp ({}) is later than now ({}, threshold: {}).".format(self.__index,
                                                                                              self.__timestamp,
                                                                                              currentTime,
                                                                                              self.__TimestampThreshold))
        if self.Index() < 0:
            raise Exception("index must be 0 or more, but its index is {}".format(self.Index()))

        elif self.Index == 0:
            if self.Difficulty != 0:
                raise Exception(
                    "difficulty must bt 0 for the genesis block, but its difficuly is {}.".format(self.Difficulty()))

            if self.PreviousHash != None:
                raise Exception("previous hash must be empty for the genesis block.")

        else:
            if self.Difficulty() < 1:
                raise Exception(
                    "difficulty must be more than 0 (except of the genesis block), but its difficulty is {}.".format(
                        self.Difficulty()))

            if self.PreviousHash == None:
                raise Exception("previous hash must be present except of the genesis block.")

        if self.Hash.Satisfy(self.__difficulty,self):
            raise Exception(
                "hash ({}) with the nonve ({}) does not satisfy its difficulty level {}".format(self.Hash(), self.Nonce(),
                                                                                                self.Difficulty()))

        for tx in self.Transaction():
            tx.Validate
















