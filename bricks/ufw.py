from bricks.brick import Brick
from os.path import join
from settings import REMOTE_SCRIPT_DIR


class UFW(Brick):
    _commands = [
        join(REMOTE_SCRIPT_DIR, "ufw.sh"),
    ]

    def __init__(self, name, description, cli):
        super(UFW, self).__init__(name, description, cli)
