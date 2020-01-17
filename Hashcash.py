from hashlib import sha256
from random import random, Random, getrandbits
import Block


class Hashcash:

    def __init__(self):
        self.hash = sha256()

    def Hash(self, data):
        if isinstance(data,bytes):
            self.hash.update(data)
        elif isinstance(data,object):
            self.hash.update(data.ToBencodex())
        return self.hash.digest()

    def Digest(self):
        return self.hash.digest()

    def Answer(self, stamp, difficulty):

        nonceSize = 10
        while True:
            nonceBytes = self.RandomBytes(nonceSize)
            digest = self.Hash(stamp(nonceBytes))
            if self.Satisfy(difficulty):
                return nonceBytes

    def RandomBytes(self,  size):
        return getrandbits(8*size).to_bytes(10,"big")

    def Satisfy(self, difficulty):

        if difficulty == 0:
            return True

        maxTarget = pow(2, 256)
        target = int(maxTarget / difficulty)
        b = self.Digest()+bytes([0])
        result = int.from_bytes(b, byteorder="big")
        return result < target
