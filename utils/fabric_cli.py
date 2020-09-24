from invoke import run
from utils.cli import CLI


class FabricCLI(CLI):
    def __init__(self, connection, watchers):
        self.connection = connection
        self.watchers = watchers

    def run_command(self, command):
        cmd = self.parse_command(command)

        try:
            return self.connection.run(cmd, pty=True, watchers=self.watchers)
        except Exception as e:
            print(e)
            raise Exception("Error on command " + str(cmd))
