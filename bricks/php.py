from .brick import Brick
from brick_path import brick_path


class Php72Ubuntu20(Brick):
    _commands = [
        brick_path("scripts/php7_2.sh"),
    ]

    def __init__(self, name, description, cli):
        super(Php72Ubuntu20, self).__init__(name, description, cli)
