from invoke import run
from abc import ABC, abstractmethod


class CLI(ABC):
    @abstractmethod
    def run_command(self, command):
        pass

    def parse_command(self, raw):
        if isinstance(raw, str):
            return raw

        if isinstance(raw, list):
            return " ".join(raw)

        raise Exception("Invalid command: " + str(raw))
