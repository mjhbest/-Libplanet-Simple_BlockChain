import datetime

class BlockPolicy:

    def __init__(self,blockInterval=None, minimumDiffifulty = 1024, DifficultyBoundDivisor =128):
        self.blockInterval = blockInterval
        self.minimumDifficulty = minimumDiffifulty
        self.DifficultyBoundDivisor = DifficultyBoundDivisor
        datetime.timedelta(seconds = self.blockInterval)


    def GetNextBlockDifficulty(self, blocks):
        index = blocks.Count()
        if index < 0:
            raise Exception("Index must be 0 or more")
        elif index <=1:
            if index ==1:
                index  = self.minimumDiffifulty
            return

        prevBlock  = blocks._Blocks[index -1]
        prevPrevTimeStamp = blocks._Blocks[index -2].Timestamp()
        prevTimeStamp = prevBlock.Timestamp()
        timeDifference = prevTimeStamp - prevPrevTimeStamp
        minimumMultiplier = -99

        multiplier = max([1 - (timeDifference/self.blockInterval), minimumMultiplier])

        prevDifficulty = prevBlock.Difficulty()
        offset = prevDifficulty / self.DifficultyBoundDivisor

        nextDifficulty = prevDifficulty + offset*multiplier

        return max([nextDifficulty, minimumMultiplier])


    def ValidateNextBlock(self,blocks,nextBlock):

        index = blocks.Count()
        difficulty = self.GetNextBlockDifficulty(blocks)

        if index >=1:
            lastBlock = blocks[index-1]
            prevHash = lastBlock.Hash()
            prevTimeStamp = lastBlock.Timestamp()
        else:
            lastBlock = None


        if nextBlock.Index() != index:
            raise Exception("the expected block index and real index is different")

        if nextBlock.Difficulty() < difficulty:
            raise Exception("difficulty is not correctly evaluated")

        if nextBlock.PreviousHash() != prevHash:
            if prevHash == None:
                raise Exception("genesisBlock must have no previous block")

            raise Exception("Hash Equivalent Error")

        if nextBlock.Timestamp() < prevTimeStamp:
            raise Exception("Current TimeStamp is ealrlier than before one.")

        return None









