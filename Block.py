import datetime
from operator import *
import hashlib
import Bencodex

class Block():

    _TimestampFormat = "yyyy--MM-ddTHH:mm:ss.ffffffZ"
    _TimestampThreshold = datetime.timedelta(seconds=900)

    # initialization 
    def __init__(self, rb = None, **kwargs):
        if rb == None:
            self._index = kwargs[index]
            self._difficulty = kwargs[difficulty]
            self._nonce = kwargs[nonce]
            self._miner = kwargs[miner]
            self._previousHash = kwargs[previousHash]
            self._timestamp = kwargs[timestamp]
            self._transactions = sorted(kwargs[transcations], key=lambda transcation: transcation.Id)
            self._hash = hashlib.sha256(ToBencodex(bytearray(self)))


        else:
            _block(rb)

    def _block(rb):
        self._index =rb._index,
        self._difficulty=rb._difficulty,
        self._nonce=Nonce(rb._nonce),
        self._miner=None if rb._miner == None else Address(rb._miner),
        self._previousHash=None if rb._previousHash == None else rb._previousHash,
        self._timestamp=rb._timestamp,
        self._transactions=rb._transactions
        self._hash = hashlib.sha256(ToBencodex(bytearray(self)))


    @property
    def Hash(self):
        return self._hash

    @property
    def Index(self):
        return self._index

    @property
    def Difficulty(self):
        return self._difficulty

    def Nonce(self):
        return self._nonce

    def Miner(self):
        return self._miner

    def PreviousHash(self):
        return self._previousHash

    def Timestamp(self):
        return self._timestamp

    def Transcations(self):
        return self._transactions

    def Mine(self, index, difficulty, miner, previousHash, timestamp, transactions, cancellationToken): #여기서 원래 libplanet 코드는 offset 찾아서 논스만 바꿔주는 방식임 -=> 이걸 어떻게 바꿀지는 생각좀
        txs = ToimmutableList(sorted(transactions, key = lambda tx: tx.Id))

        def MakeBlock(n):
            return Block(index, difficulty, n, miner, previousHash, timestamp, txs)

        emptyNonce = MakeBlock(bytearray(0)).ToBencodex(false, flase)
        oneByteNoce = MakeBlock(bytearray(1)).ToBencodex(false, false)
        offset = 0
        while offset < len(emptyNonce) and emptyNonce[offset] == oneByteNoce[offset]:
            offset = offset + 1

        stampPrefix = emptyNonce[0:offset]
        stampSuffix = emptyNonce[offset:len(emptyNonce)]

        nLen = len(bytearray(n))

        nLenStr = str(nLen).encode()
        totalLen = len(stampPrefix) + len(nLenStr) + len(stampSuffix) + 1
        stamp = bytearray(totalLen)
        stamp = copy.deepcopy(stampPrefix) + copy.deepcopy(nLenSter) + bytearray(0x3a) + copy.deepcopy(stampSuffix)

        nonce = Hashcash.Answer(stamp)

        return MakeBlock(nonce)


    def FromBencodex(encoded):
        serializer = BencodexFormatter()

    def ToBencodex(hash, transactionData):  # bencodex.py 모듈 보고 마저 수정
        return;


    def ToString():
        return str(self._hash)

    class BlockSerializationContext():
        def __init__(self, hash, transactionData):
            self._includeHash = hash
            self._includeTransactionData = transactionData

        @property
        def IncludeHash(self):
            return self._includeHash

        @property
        def includeTransactionData(self):
            return self._includeTransactionData

    def GetObjectData(info, context):
        includeHash = False
        includeTransactionData = False
        if (serialCtx = context.Context) != None:
            includeHash = serialCtx.IncludeHash
            includeTransactionData = serialCtx.includeTransactionData
        rawBlock = ToRawBlock(includeHash, includeTransactionData)
        rawBlock,.GetObjectData(info, context)

    def Validate(currentTime):
        if currentTime + this._TimestampThreshold < this._timestamp:

            raise Exception(
                "The block {}'s timestamp ({}) is later than now ({}, threshold: {}).".format(self._index,
                                                                                              self._timestamp,
                                                                                              currentTime,
                                                                                              self._TimestampThreshold))
        if self.Index < 0:
            raise Exception("index must be 0 or more, but its index is {}".format(self.Index))

        elif self.Index == 0:
            if self.Difficulty != 0:
                raise Exception(
                    "difficulty must bt 0 for the genesis block, but its difficuly is {}.".format(self.Difficulty))

            if self.PreviousHash != None:
                raise Exception("previous hash must be empty for the genesis block.")

        else:
            if self.Difficulty < 1:
                raise Exception(
                    "difficulty must be more than 0 (except of the genesis block), but its difficulty is {}.".format(
                        self.Difficulty))

            if self.PreviousHash == None:
                raise Exception("previous hash must be present except of the genesis block.")

        if self.Hash.Satisfies(self._difficulty):
            raise Exception(
                "hash ({}) with the nonve ({}) does not satisfy its difficulty level {}".format(self.Hash, self.Nonce,
                                                                                                self.Difficulty))

        for tx in self.Transaction:
            tx.Validate
















