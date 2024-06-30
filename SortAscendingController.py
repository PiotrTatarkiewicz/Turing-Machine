from Controller import Controller
from Direction import Direction


class SortAscendingController(Controller):

    def takeAction(self) -> str:
        rawValue = str(self.pommel.readValue())
        currentState = self.state

        if self.stateStartsWith(Controller.CONTROLLER_INIT_STATE):
            suffix = currentState[len(Controller.CONTROLLER_INIT_STATE):]

            if len(suffix) == 0:
                self.pommel.makeMove(Direction.LEFT)
                self.state = Controller.CONTROLLER_INIT_STATE + "-MOVE_TO_LEFT_SIDE"

                return "{0}, {1}, {2}, {3}, {4}".format(rawValue, currentState, rawValue, self.state, "L")
            elif suffix == "-MOVE_TO_LEFT_SIDE":
                if self.pommel.isReadValueEmpty():
                    self.pommel.makeMove(Direction.RIGHT)
                    self.state = "SORT"
                    return "{0}, {1}, {2}, {3}, {4}".format(rawValue, currentState, rawValue, self.state, "R")
                else:
                    self.pommel.makeMove(Direction.LEFT)
                    return "{0}, {1}, {2}, {3}, {4}".format(rawValue, currentState, rawValue, self.state, "L")

        elif self.stateStartsWith("SORT"):
            suffix = currentState[len("SORT"):]

            if len(suffix) == 0:
                if self.pommel.isReadValueEmpty():
                    self.pommel.makeMove(Direction.RIGHT)
                    return "{0}, {1}, {2}, {3}, {4}".format(rawValue, currentState, rawValue, self.state, "R")

                self.state = "SORT-LAST_PIECE-" + rawValue
                self.pommel.makeMove(Direction.RIGHT)
                return "{0}, {1}, {2}, {3}, {4}".format(rawValue, currentState, rawValue, self.state, "R")

            if suffix.startswith("-LAST_PIECE-"):
                if self.pommel.isReadValueEmpty():
                    self.state = "ENDED"
                    return "ENDED"

                try:
                    rawLastPieceValue = suffix[len("-LAST_PIECE-"):]
                    lastPieceValue = int(rawLastPieceValue)
                except ValueError:
                    raise ValueError("Value \"{0}\" from the tape is not an integer!".format(rawLastPieceValue))

                try:
                    value = int(rawValue)
                except ValueError:
                    raise ValueError("Value \"{0}\" from the tape is not an integer!".format(rawValue))

                if lastPieceValue > value:
                    self.state = "SORT-MOVE_TO_LEFT-" + rawValue
                    self.pommel.writeValue(rawLastPieceValue)
                    self.pommel.makeMove(Direction.LEFT)
                    return "{0}, {1}, {2}, {3}, {4}".format(rawValue, currentState, rawLastPieceValue, self.state, "L")
                else:
                    self.state = "SORT-LAST_PIECE-" + rawValue
                    self.pommel.makeMove(Direction.RIGHT)
                    return "{0}, {1}, {2}, {3}, {4}".format(rawValue, currentState, rawValue, self.state, "R")

            if suffix.startswith("-MOVE_TO_LEFT-"):
                try:
                    rawSwapValue = suffix[len("-MOVE_TO_LEFT-"):]
                except ValueError:
                    raise ValueError("Value \"{0}\" from the tape is not an integer!".format(rawSwapValue))

                self.state = "SORT"
                self.pommel.writeValue(rawSwapValue)
                self.pommel.makeMove(Direction.LEFT)
                return "{0}, {1}, {2}, {3}, {4}".format(rawValue, currentState, rawSwapValue, self.state, "L")

            # TODO Write it.
        elif self.hasEndedWork():
            raise Exception("Controller has already ended his work!")
        else:
            raise Exception("Not known controller state!")

    def hasEndedWork(self) -> bool:
        return self.stateEquals("ENDED")
