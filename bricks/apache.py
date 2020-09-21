from bricks.brick import Brick
from os import path, getcwd


class ApacheUbuntu20(Brick):
    _commands = [
        "apt install apache2 -y",
        f'cp {path.join(path.dirname(path.realpath(__file__)), "config/apache2.conf")} /etc/apache2/apache2.conf',
    ]

    def __init__(self, name, description, cli):
        super(ApacheUbuntu20, self).__init__(name, description, cli)
