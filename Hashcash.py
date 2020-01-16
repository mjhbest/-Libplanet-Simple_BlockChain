from hashlib import sha256
from random import Random

class Hashcash:

    def __init__(self):
        self.hash = sha256()

    def Hash(self, bytes):
        self.hash.update(bytes)
        return self.hash.digest()

    def Digest(self):
        return self.hash.digest()

    def Answer(self,stamp,difficulty):

        nonceSize =  10
        nonceBytes = [None]*10
        self.RandomBytes(nonceBytes, nonceSize)
        while True:
            self.RandomBytes(nonceBytes,nonceSize)
            digest = self.Hash(stamp(nonceBytes))
            if self.Satisfy(difficulty, digest):
                return bytearray(nonceBytes)


    def RandomBytes(self,nonceBytes,size):
        for i in range(size):
            nonceBytes[i] = bytearray(Random().getrandbits(8))


    def Satisfy(self,difficulty,digest):

        if digest == 0:
            return True

        maxTarget = pow(2,256)
        target = int(maxTarget/difficulty)
        result = int.from_bytes(bytearray(self.Digest()).append(0),byteorder="big")
        return result < target







