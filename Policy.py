import datetime
import bencodex


class BlockPolicy:

    def __init__(self, blockInterval=1024, minimumDiffifulty=1024, DifficultyBoundDivisor=128):
        self.blockInterval = datetime.timedelta(seconds=self.blockInterval)\
            if isinstance(int, type(blockInterval))\
            else blockInterval

        self.minimumDifficulty = minimumDiffifulty
        self.DifficultyBoundDivisor = DifficultyBoundDivisor

    def GetNextBlockDifficulty(self, blocks):
        index = blocks.Count()
        if index < 0:
            raise Exception("Index must be 0 or more")
        elif index <= 1:
            if index == 1:
                index = self.minimumDifficulty
            return index

        prevBlock = blocks[index - 1]
        prevPrevTimeStamp = blocks[index - 2].Timestamp()
        prevTimeStamp = prevBlock.Timestamp()
        timeDifference = prevTimeStamp - prevPrevTimeStamp
        minimumMultiplier = -99
        multiplier = max([1 - (int(timeDifference.total_seconds()) / self.blockInterval), minimumMultiplier])

        prevDifficulty = prevBlock.Difficulty()
        offset = prevDifficulty / self.DifficultyBoundDivisor
        nextDifficulty = prevDifficulty + offset * multiplier

        return max([nextDifficulty, minimumMultiplier])

    def ValidateNextBlock(self, blocks, nextBlock):

        index = blocks.Count()
        difficulty = self.GetNextBlockDifficulty(blocks)

        if nextBlock.Index() != index:
            raise Exception("the expected block index and real index is different")

        if nextBlock.Difficulty() < difficulty:
            raise Exception("difficulty is not correctly evaluated")

        if index>=1:
            lastBlock = blocks[index - 1]
            prevHash = lastBlock.Hash()
            prevTimeStamp = lastBlock.Timestamp()

            if nextBlock.PreviousHash() != prevHash:
                if prevHash is None:
                    raise Exception("genesisBlock must have no previous block")
                raise Exception("Hash Equivalent Error")

            if nextBlock.Timestamp() < prevTimeStamp:
                raise Exception("Current TimeStamp is ealrlier than before one.")
        print(index)
        return True

    def ToBencodex(self):
        d = {
            'blockInterval' : self.blockInterval,
            'minimumDifficulty' : self.minimumDifficulty,
            'DifficultyBoundDivisor': self.DifficultyBoundDivisor

        }
        return  dumps(d)


