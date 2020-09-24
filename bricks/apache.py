from bricks.brick import Brick
from utils.path_resolver import brick_path
from settings import REMOTE_CONF_DIR
from os.path import join


class ApacheUbuntu20(Brick):
    _commands = [
        "apt install apache2 -y",
        f'cp {join(REMOTE_CONF_DIR, "apache2.conf")} /etc/apache2/apache2.conf',
    ]

    def __init__(self, name, description, cli):
        super(ApacheUbuntu20, self).__init__(name, description, cli)
