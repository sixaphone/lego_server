from utils.cli import CLI
from utils.cli_factory import CLIFactory
from utils.cli_provider import CLIProvider
from utils.connection_factory import ConnectionFactory
from utils.watchers_factory import WatchersFactory


class BrickBuilder:
    def __init__(self):
        self.bricks_module = __import__("bricks")

    def build(self, brick_config, connection_config):
        brick_conn_config = connection_config

        if "connection" in brick_config:
            brick_conn_config = brick_config["connection"]

        watchers = []

        if "watchers" in brick_conn_config:
            watchers = WatchersFactory.create_watchers(brick_conn_config["watchers"])

        class_module = getattr(self.bricks_module, brick_config["module"])
        instance = getattr(class_module, brick_config["class"])(
            brick_config["name"],
            brick_config["description"],
            CLIFactory.create_cli(
                provider=CLIProvider.FABRIC,
                connection=ConnectionFactory.create_connection(brick_conn_config),
                watchers=watchers,
            ),
        )

        if "env" in brick_config:
            instance.update_env(brick_config["env"])

        return instance