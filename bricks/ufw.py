from .brick import Brick


class UFW(Brick):
    _commands = [
        'ufw allow in "Apache Full"' 'ufw allow in "OpenSSH"',
        "ufw enable",
    ]

    def __init__(self, name, description, cli):
        super(UFW, self).__init__(name, description, cli)
