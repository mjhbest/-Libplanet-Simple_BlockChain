
class Transaction():

     def __init__(self,id, isEval= false, data=None):
         self.isEval = isEval
         self.Id = id
         self.data = data
         self.nonce = 0

     def Eval(self,tx):
         tx.isEval = true