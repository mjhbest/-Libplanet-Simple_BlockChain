class Store():
    def __init__(self,blks = None, txs = None):
        self.Blocks = blks
        self.Txs = txs
        if blks == None:
            self.Blocks = dict()
        if txs == None:
            self.Txs = dict()

    def AddBlock(self,block):
        self.Blocks[blokc.]

    def AddTx(self,Tx):

