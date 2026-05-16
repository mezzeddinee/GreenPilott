from pilotTools import CommandBase
import traceback


class GreenHello(CommandBase):

    def __init__(self, pilotParams):

        try:
            CommandBase.__init__(self, pilotParams, "GreenHello")
            print("GREENHELLO INIT OK")

        except Exception as e:
            print("GREENHELLO INIT FAILED")
            print(str(e))
            traceback.print_exc()
            raise

    def execute(self):

        print("################################")
        print("### GREEN HELLO FROM MAZEN ###")
        print("################################")

        return 0
