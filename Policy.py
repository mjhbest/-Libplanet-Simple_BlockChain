import datetime

class BlockPolicy():

    def __init__(self,**kwargs):
        self.blockInterval = kwargs[blockInterval]
        datetime.timedelta(seconds = self.blockInterval)


    def GetNextBlcokDifficulty(self, block):



    def ValidateNextBlock(self,blocks,nextBlock):








