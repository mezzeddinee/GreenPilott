from pilotTools import CommandBase


class GreenHello(CommandBase):

    def __init__(self, pilotParams):

        self.pp = pilotParams
        self.log = pilotParams.log

    def execute(self):

        print("################################")
        print("### GREEN HELLO FROM MAZEN ###")
        print("################################")

        return 0
