from utils.cli import CLI
from utils.cli_factory import CLIFactory
from utils.cli_provider import CLIProvider
from fabric import Connection


class ConnectionFactory:
    connections = {}

    @staticmethod
    def create_connection(config):
        if config["name"] in ConnectionFactory.connections:
            return ConnectionFactory.connections[config["name"]]

        port = 22
        key_filename = None

        if "port" in config:
            port = config["port"]

        if "key_filename" in config:
            key_filename = config["key_filename"]

        connection = Connection(
            user=config["user"],
            host=config["host"],
            port=port,
            connect_kwargs={
                "password": config["password"],
                "key_filename": key_filename,
            },
        )
        ConnectionFactory.connections[config["name"]] = connection

        return connection
