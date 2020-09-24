from abc import ABC


class Brick(ABC):

    _env = {}
    _commands = []

    def __init__(self, name, description, cli):
        self.name = name
        self.description = description
        self.cli = cli

    def __str__(self):
        return f"{self.name}: {self.description}"

    def run(self):
        print("===================================")
        print("|" + str(self) + "|")
        print("===================================")
        for step in self._commands:
            if isinstance(step, Brick):
                step.run()
            elif isinstance(step, str):
                print(self.cli.run_command(step))
            else:
                raise Exception("Unable to run step: " + str(step))
        print("\n")

    def update_env(self, overrides):
        self._env = {**self._env, **overrides}
