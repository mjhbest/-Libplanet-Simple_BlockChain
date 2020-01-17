from coincurve import PublicKey, PrivateKey
from bencodex import dumps
import pickle

class Transaction:

     def __init__(self,id, privateKey, data=None):
         self.id = id
         self.data = data
         self.nonce = 0
         self.publicKey = privateKey.public_key
         self.signature = privateKey.sign(dumps(self.TxBencodeFormatter()))

     def Validate(self):
         if not self.publicKey.verify(self.signature,self.TxBencodex()):
            raise Exception("The signature is invalid")

     def TxBencodex(self):
         return dumps(self.TxBencodeFormatter())

     def TxBencodeFormatter(self):
         dic = {
             'id': self.id,
             'data': self.data,
             'nonce': self.nonce,
             'publicKey': self.publicKey
         }
         return dic