from invoke import run
from utils.cli import CLI


class InvokeCLI(CLI):
    def run_command(self, command):
        cmd = super(InvokeCLI, self).parse_command(command)

        try:
            return run(cmd)
        except Exception as e:
            print(e)
            raise Exception("Error on command " + str(cmd))