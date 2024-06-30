from Controller import Controller
from Pommel import Pommel
from ValidationUtils import ValidationUtils


class TuringMachine:

    """

    Turing Machine is used to process tape by controller.

    Args:
        controllerClass: Controller class for which the controller instance will be created.
        tape: Tape represented by the table.
        startTapeIndex: Start index for the pommel (initial pommel location).
        emptyPiece: Character for undefined parts of the tape.

    Attributes:
        pommel (Pommel): Pommel, which is being controlled.
        controller (Controller): Controller, which makes actions on the tape.
    """
    def __init__(self, controllerClass, tape, startTapeIndex, emptyPiece):
        ValidationUtils.isNone(controllerClass, "controllerClass is undefined.", Exception)
        ValidationUtils.isNone(tape, "tape is undefined.", Exception)
        ValidationUtils.isNone(startTapeIndex, "startTapeIndex is undefined.", Exception)
        ValidationUtils.isNone(emptyPiece, "emptyPiece is undefined.", Exception)

        ValidationUtils.isSubclassOf(controllerClass, Controller, "controllerClass is not subclass of Controller.")

        ValidationUtils.isInstanceOf(tape, list, "controllerClass is not instance of list.")
        ValidationUtils.isInstanceOf(startTapeIndex, int, "startTapeIndex is not instance of int.")
        ValidationUtils.isInstanceOf(emptyPiece, str, "emptyPiece is not instance of str.")

        for element in tape:
            ValidationUtils.isInstanceOf(element, str, "One of table elements is not instance of str.")

        self.pommel = Pommel(tape, startTapeIndex, emptyPiece)
        self.controller = controllerClass(self.pommel)

    def enable(self):
        """ Enables this machine """
        print("Enabled", self.__class__.__name__, " by Piotr Tatarkiewicz and Weronika Skoczylas\n")

        counter = 0

        while True:
            response = self.controller.takeAction()

            counter += 1

            print("[ACTION #{0}] ({1})".format(counter, response))
            if self.controller.hasEndedWork():
                break

        print("\nTurning Machine has ended work!")

        if not counter == 1:
            action = "actions!"
        else:
            action = "action!"

        print("Made", counter, action)
        print("Processed tape:", self.pommel.getTape())
