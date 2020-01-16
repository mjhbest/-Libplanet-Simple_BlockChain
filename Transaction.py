from coincurve import *
import
class Transaction:

     def __init__(self,id, privateKey, data=None):
         self.id = id
         self.data = data
         self.nonce = 0
         self.publicKey = privateKey.public_key()
         self.signature = privateKey.sign()

     def Validate(self):
         if not self.publicKey.verify(self.signature,self.ToBencodex())
            raise Exception("The signature is invalid")함

         if

     #기존 코드의 Create 메소드의 필요성 확인해야

     def ToBencodex(self):
         return dumps(self.TxBencodeFormatter())


     def TxBencodeFormatter(self):

         dic = {
             'id': self.id,
             'data': self.data,
             'nonce': self.nonce,
             'publicKey': self.publicKey,
             'signature': self.signature
         }
         return dic