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
        for cmd in self._commands:
            print(self.cli.run_command(cmd))

    def update_env(self, overrides):
        self._env = {**self._env, **overrides}
