from pilotTools import CommandBase


class GreenHello(CommandBase):

    def __init__(self, pilotParams):

        super().__init__(pilotParams)

    def execute(self):

        self.log.info("################################")
        self.log.info("### GREEN HELLO FROM MAZEN ###")
        self.log.info("################################")

        return 0
