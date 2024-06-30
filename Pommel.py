from Direction import Direction

from PommelError import PommelError
from Tape import Tape
from TapeIndex import TapeIndex
from ValidationUtils import ValidationUtils


class Pommel:

    def __init__(self, tape, startTapeIndex, emptyPiece):
        ValidationUtils.mustBeTrue(0 <= startTapeIndex < len(tape), "startTapeIndex is not valid. Object with this index doesn't exist on the tape!", PommelError)
        self.tape = Tape(tape, emptyPiece)
        self.tapeIndex = TapeIndex(startTapeIndex)

    def getTape(self):
        return self.tape.getTape()

    def getEmptyPieceCharacter(self):
        return self.tape.getEmptyPieceCharacter()

    def isReadValueEmpty(self):
        return self.readValue() == self.getEmptyPieceCharacter()

    def readValue(self):
        return self.tape.getCharacter(self.tapeIndex)

    def writeValue(self, value):
        self.tape.substituteCharacter(self.tapeIndex, value)

    def makeMove(self, direction):
        if direction == Direction.LEFT:
            self.tapeIndex.decrement()
        elif direction == Direction.RIGHT:
            self.tapeIndex.increment()
        else:
            raise PommelError("Cannot find valid direction.")