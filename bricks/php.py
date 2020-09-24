from bricks.brick import Brick
from os.path import join
from settings import REMOTE_SCRIPT_DIR


class Php72Ubuntu20(Brick):
    _commands = [
        join(REMOTE_SCRIPT_DIR, "php7_2.sh"),
    ]

    def __init__(self, name, description, cli):
        super(Php72Ubuntu20, self).__init__(name, description, cli)
