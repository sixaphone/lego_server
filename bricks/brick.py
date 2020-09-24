from abc import ABC
from jinja2 import Environment


class Brick(ABC):

    _env = {}
    _commands = []

    def __init__(self, name, description, cli):
        self.name = name
        self.description = description
        self.cli = cli
        self.jinja = Environment(autoescape=True)

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
                parsed = self.jinja.from_string(step).render(self._env)
                print(self.cli.run_command(parsed))
            else:
                raise Exception("Unable to run step: " + str(step))
        print("\n")

    def update_env(self, overrides):
        self._env = {**self._env, **overrides}
