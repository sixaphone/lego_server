import subprocess
from invoke import run


class CLI:
    def run_command(self, command):
        try:
            cmd = None

            if isinstance(command, str):
                cmd = command

            if isinstance(command, list):
                cmd = " ".join(command)

            if not cmd:
                raise Exception("Invalid command.")

            try:
                result = run(cmd)
            except Exception as e:
                print(e)
                raise Exception("Error on command " + cmd)

            return result
        except Exception as e:
            print(str(e))
            exit()
