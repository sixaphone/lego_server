from .brick import Brick
from bricks.brick_path import brick_path


class UFW(Brick):
    _commands = [
        brick_path("scripts/ufw.sh"),
    ]

    def __init__(self, name, description, cli):
        super(UFW, self).__init__(name, description, cli)
