from hashlib import sha256
from random import random

class Hashcash(sha256):

    #Stamp ??

    def Answer(self,stamp,difficulty):
        nonceSize =  10
        nonceBytes = [None]*10
        self.RandomBytes(nonceBytes, nonceSize)
        while True:
            self.RandomBytes(nonceBytes,nonceSize)
            digest = sha256(stamp(nonceBytes))
            if self.Satisfy(difficulty, digest):
                return bytearray(nonceBytes)


    def RandomBytes(self,nonceBytes,size):

        for i in size:
            nonceBytes[i] = bytearray(random.getrandbits(8))



    def Satisfy(self,difficulty,digest):

        if digest == 0:
            return True

        maxTarget = pow(2,256)
        target = maxTarget/difficulty
        #Question


