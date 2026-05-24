from pilotTools import CommandBase

print("GREENPILOTT MODULE IMPORTED v2026-05-23-1")

class GreenHello(CommandBase):
    def __init__(self, pilotParams):
        CommandBase.__init__(self, pilotParams, "GreenHello")
        print("GREENHELLO INIT OK v2026-05-23-1")

    def execute(self):
        print("GREENHELLO EXECUTE v2026-05-23-1")
        return 0
