import datetime
from bencodex import *
from Hashcash import Hashcash
from copy import deepcopy
import pickle


class Block:
    __TimestampFormat = "yyyy--MM-ddTHH:mm:ss.ffffffZ"
    __TimestampThreshold = datetime.timedelta(seconds=900)

    # initialize
    def __init__(self, index=None, difficulty=None, nonce=None, previousHash=None, timestamp=None, txs=None,
                 rb=None):
        if rb == None:
            self.__index = index
            self.__difficulty = difficulty
            self.__nonce = nonce
            self.__previousHash = previousHash
            self.__timestamp = timestamp
            self.__transactions = txs
            self.__hash = Hashcash().Hash(self.ToBencodex())

        else:
            self.__block(rb)

    def __block(self, rb):
        self.__index = rb.Index()
        self.__difficulty = rb.Difficulty
        self.__nonce = rb.Nonce()
        self.__previousHash = None if rb.__previousHash is None else rb.__previousHash
        self.__timestamp = rb.__timestamp
        self.__transactions = rb.__transactions
        self.__hash = Hashcash().Hash(self.ToBencodex())

    def Mine(self, index, difficulty, previousHash, timestamp, transactions):

        def MakeBlock(n):
            return Block(index, difficulty, n, previousHash, timestamp, transactions)

        emptyNonce = MakeBlock(0).ToBencodex()
        oneByteNoce = MakeBlock(1).ToBencodex()
        offset = 0  # find location of Nonce
        while offset < len(emptyNonce) and emptyNonce[offset] == oneByteNoce[offset]:
            offset = offset + 1

        stampPrefix = deepcopy(emptyNonce[0:offset])
        stampSuffix = deepcopy(emptyNonce[offset:len(emptyNonce)])

        def Stamp(nonce):
            nLen = len(nonce)
            nLenStr = str(nLen).encode()
            stamp = deepcopy(stampPrefix)\
                    +nLenStr\
                    +(bytes(0x3a))\
                    +nonce\
                    +deepcopy(stampSuffix)
            return stamp

        nonce = Hashcash().Answer(Stamp, difficulty)

        return MakeBlock(nonce)

    def FromBencodex(self, encoded):
        return loads(encoded)

    def ToBencodex(self):
        return dumps(self.BlockBencodeFormatter())

    def BlockBencodeFormatter(self):
        d = {
            'index': self.__index,
            'difficulty': pickle.dumps(self.__difficulty),
            'nonce': self.__nonce,
            'previousHash': self.__previousHash,
            'timestamp': pickle.dumps(self.__timestamp),
            'transactions': self.__transactions
        }
        return d

    def Validate(self, currentTime):
        if currentTime + self.__TimestampThreshold < self.__timestamp:
            raise Exception(
                "The block {}'s timestamp ({}) is later than now ({}, threshold: {}).".format(self.__index,
                                                                                              self.__timestamp,
                                                                                              currentTime,
                                                                                              self.__TimestampThreshold))
        if self.Index() < 0:
            raise Exception("index must be 0 or more, but its index is {}".format(self.Index()))

        elif self.Index() == 0:
            if self.Difficulty != 0:
                raise Exception(
                    "difficulty must bt 0 for the genesis block, but its difficuly is {}.".format(self.Difficulty()))

            if self.PreviousHash() is not None:
                raise Exception("previous hash must be empty for the genesis block.")

        else:
            if self.Difficulty() < 1:
                raise Exception(
                    "difficulty must be more than 0 (except of the genesis block), but its difficulty is {}.".format(
                        self.Difficulty()))

            if self.PreviousHash is None:
                raise Exception("previous hash must be present except of the genesis block.")

        if self.Hash.Satisfy(self.__difficulty, self):
            raise Exception(
                "hash ({}) with the nonve ({}) does not satisfy its difficulty level {}".format(self.Hash(),
                                                                                                self.Nonce(),
                                                                                                self.Difficulty()))

        for tx in self.Transactions():
            tx.Validate()

    def Hash(self):
        return self.__hash

    def Index(self):
        return self.__index

    def Difficulty(self):
        return self.__difficulty

    def Nonce(self):
        return self.__nonce

    def PreviousHash(self):
        return self.__previousHash

    def Timestamp(self):
        return self.__timestamp

    def Transactions(self):
        return self.__transactions
