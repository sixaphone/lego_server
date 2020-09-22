from bricks.brick import Brick
from bricks.brick_path import brick_path


class ApacheUbuntu20(Brick):
    _commands = [
        "apt install apache2 -y",
        f'cp {brick_path("config/apache2.conf")} /etc/apache2/apache2.conf',
    ]

    def __init__(self, name, description, cli):
        super(ApacheUbuntu20, self).__init__(name, description, cli)
