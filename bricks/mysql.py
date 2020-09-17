from .brick import Brick


class MysqlUbuntu20(Brick):
    _commands = [
        "apt install mysql-server mysql-client -y",
    ]

    def __init__(self, name, description, cli):
        super(MysqlUbuntu20, self).__init__(name, description, cli)
