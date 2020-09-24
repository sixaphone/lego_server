from bricks.brick import Brick
from settings import REMOTE_CONF_DIR, REMOTE_SCRIPT_DIR


class CleanUp(Brick):
    _commands = [
        f"rm -rf {REMOTE_CONF_DIR}",
        f"rm -rf {REMOTE_SCRIPT_DIR}",
    ]

    def __init__(self, name, description, cli):
        super(CleanUp, self).__init__(name, description, cli)