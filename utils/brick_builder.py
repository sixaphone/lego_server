from utils.cli import CLI
from utils.cli_factory import CLIFactory


class BrickBuilder:
    def __init__(self):
        self.bricks_module = __import__("bricks")

    def build(self, config):
        class_module = getattr(self.bricks_module, config["module"])
        instance = getattr(class_module, config["class"])(
            config["name"], config["description"], CLIFactory.create_cli()
        )

        if "env" in config:
            instance.update_env(config["env"])

        return instance