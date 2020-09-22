from invoke import run


class CLI:
    def run_command(self, command):
        cmd = self.parse_command(command)

        try:
            return run(cmd)
        except Exception as e:
            print(e)
            raise Exception("Error on command " + str(cmd))

    def parse_command(self, raw):
        if isinstance(raw, str):
            return raw

        if isinstance(raw, list):
            return " ".join(raw)

        raise Exception("Invalid command: " + str(raw))
