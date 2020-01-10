import datetime
import hashlib
from Bencodex import *

class Block():

    __TimestampFormat = "yyyy--MM-ddTHH:mm:ss.ffffffZ"
    __TimestampThreshold = datetime.timedelta(seconds=900)

    # initialize
    def __init__(self, rb = None, index,difficulty, nonce, miner, previousHash,timestamp,txs):
        if rb == None:
            self.____index = index
            self.____difficulty = difficulty
            self.____nonce = nonce
            self.__miner = miner
            self.__previousHash = previousHash
            self.__timestamp = timestamp
            self.__transactions = sorted(txs, key=lambda transcation: transcation.Id)
            self.__hash = hashlib.sha256(ToBencodex(bytearray(self)))

        else:
            __block(rb)


        def __block(rb):
        self.__index =rb.__index,
        self.__difficulty=rb.__difficulty,
        self.__nonce=Nonce(rb.__nonce),
        self.__miner=None if rb.__miner == None else Address(rb.__miner),
        self.__previousHash=None if rb.__previousHash == None else rb.__previousHash,
        self.__timestamp=rb.__timestamp,
        self.__transactions=rb.__transactions
        self.__hash = hashlib.sha256(ToBencodex(bytearray(self)))

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
 
    def Mine(self, index, difficulty, miner, previousHash, timestamp, transactions): #여기서 원래 libplanet 코드는 offset 찾아서 논스만 바꿔주는 방식임 -=> 이걸 어떻게 바꿀지는 생각좀
        txs = ToimmutableList(sorted(transactions, key = lambda tx: tx.Id))

        def MakeBlock(n):
            return Block(index, difficulty, n, miner, previousHash, timestamp, txs)

        emptyNonce = MakeBlock(bytearray(0)).ToBencodex(false, flase)
        oneByteNoce = MakeBlock(bytearray(1)).ToBencodex(false, false)
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
]

    def FromBencodex(encoded): #yet
        serializer = BencodexFormatter()

    def ToBencodex(hash, transactionData): #yet
        return;

    ##inner class
    class BlockSerializationContext():
        def __init__(self, hash, transactionData):
            self.__includeHash = hash
            self.__includeTransactionData = transactionData

        @property
        def IncludeHash(self):
            return self.__includeHash

        @property
        def includeTransactionData(self):
            return self.__includeTransactionData


    # def GetObjectData(info, context):
    #     includeHash = False
    #     includeTransactionData = False
    #     if (serialCtx = context.Context) != None:
    #         includeHash = serialCtx.IncludeHash
    #         includeTransactionData = serialCtx.includeTransactionData
    #     rawBlock = ToRawBlock(includeHash, includeTransactionData)
    #     rawBlock,.GetObjectData(info, context)

    def Validate(currentTime):
        if currentTime + this.__TimestampThreshold < this.__timestamp:

            raise Exception(
                "The block {}'s timestamp ({}) is later than now ({}, threshold: {}).".format(self.__index,
                                                                                              self.__timestamp,
                                                                                              currentTime,
                                                                                              self.__TimestampThreshold))
        if self.Index < 0:
            raise Exception("index must be 0 or more, but its index is {}".format(self.Index()))

        elif self.Index == 0:
            if self.Difficulty != 0:
                raise Exception(
                    "difficulty must bt 0 for the genesis block, but its difficuly is {}.".format(self.Difficulty()))

            if self.PreviousHash != None:
                raise Exception("previous hash must be empty for the genesis block.")

        else:
            if self.Difficulty < 1:
                raise Exception(
                    "difficulty must be more than 0 (except of the genesis block), but its difficulty is {}.".format(
                        self.Difficulty()))

            if self.PreviousHash == None:
                raise Exception("previous hash must be present except of the genesis block.")

        if self.Hash.Satisfies(self.__difficulty):
            raise Exception(
                "hash ({}) with the nonve ({}) does not satisfy its difficulty level {}".format(self.Hash(), self.Nonce(),
                                                                                                self.Difficulty()))

        for tx in self.Transaction():
            tx.Validate
















