import math


class Tape:

    def __init__(self, tape, emptyPiece):
        self.tape = tape
        self.emptyPiece = emptyPiece

    def getTape(self):
        return self.tape

    def getEmptyPieceCharacter(self):
        return self.emptyPiece

    def substituteCharacter(self, tapeIndex, newValue):
        self.valid(tapeIndex)
        self.tape[tapeIndex.index] = newValue

    def getCharacter(self, tapeIndex):
        self.valid(tapeIndex)
        return self.tape[tapeIndex.index]

    def valid(self, tapeIndex):
        if tapeIndex.index < 0:
            for i in range(0, int(math.fabs(tapeIndex.index))):
                self.tape = [self.emptyPiece] + self.tape
                tapeIndex.increment()
        elif tapeIndex.index >= len(self.tape):
            for i in range(-1, tapeIndex.index - len(self.tape)):
                self.tape = self.tape + [self.emptyPiece]
