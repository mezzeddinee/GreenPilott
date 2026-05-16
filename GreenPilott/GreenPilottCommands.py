from pilotCommands import CommandBase


class GreenHello(CommandBase):

    def __init__(self, pilotParams):

        CommandBase.__init__(self, pilotParams)
        self.log = self.pp.logger

    def execute(self):

        self.log.info("################################")
        self.log.info("### GREEN HELLO FROM MAZEN ###")
        self.log.info("################################")

        return 0
