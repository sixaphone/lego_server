from bricks.brick import Brick
from utils.path_resolver import brick_path
from os import listdir
from settings import REMOTE_CONF_DIR, REMOTE_SCRIPT_DIR


class Setup(Brick):
    _commands = [
        f"rm -rf {REMOTE_CONF_DIR} && mkdir {REMOTE_CONF_DIR}",
        f"rm -rf {REMOTE_SCRIPT_DIR} && mkdir {REMOTE_SCRIPT_DIR}",
    ]

    def __init__(self, name, description, cli):
        super(Setup, self).__init__(name, description, cli)

    def run(self):
        super(Setup, self).run()
        self.put_recursive("config", REMOTE_CONF_DIR)
        self.put_recursive("scripts", REMOTE_SCRIPT_DIR)

    def put_recursive(self, source, destination):
        for file in listdir(brick_path(source)):
            self.cli.connection.put(brick_path(source, file), destination)