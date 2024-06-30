class Controller:

    CONTROLLER_INIT_STATE = "START"

    """

    The Controller for Turing Machine.

    Args:
        pommel: Pommel object, which will be controlled by this controller

    Attributes:
        pommel (Pommel): Pommel, which is being controlled.
        state (str): State of controller. Init value: "START"
    """
    def __init__(self, pommel):
        self.pommel = pommel
        self.state = Controller.CONTROLLER_INIT_STATE

    def takeAction(self) -> str:
        """:returns: debug information about action. e.g.: 1,q0,0,q0,L"""
        raise NotImplementedError()

    def hasEndedWork(self) -> bool:
        """:returns: true when the work has been completed or false if didn't end yet."""
        raise NotImplementedError()

    def stateStartsWith(self, prefix):
        return self.state.startswith(prefix)

    def stateEquals(self, string):
        return self.state == string

    def stateEqualsIgnoreCase(self, string):
        return self.state.lower() == string.lower()
