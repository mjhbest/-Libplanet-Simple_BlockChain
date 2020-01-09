from hashlib import sha256
from random import random

class Hashcash(sha256):

    #Stamp ??

    def Answer(self,stamp,difficulty):
        nonceSize =  ##바이트 지정 ?? 10??
        nonceBytes = [None]*10
        while True:
            self.RandomBytes(nonceBytes,nonceSize)

            digest = sha256(Stamp(nonceBytes)) #stamp??
            if self.Satisfy(difficulty, digest):
                return bytearray(nonceBytes)


    def RandomBytes(self,nonceBytes,size):

        for i in size:
            nonceBytes[i] = bytearray(random.getrandbits(8))



    def Satisfy(self,difficulty,digest):

        if digest == 0:
            return True

        maxTarget = pow(2,256)
        target = biginteger(maxTarget/difficulty) #biginteger 구현 ? Sat
        resutl = biginteger(bytearray())
