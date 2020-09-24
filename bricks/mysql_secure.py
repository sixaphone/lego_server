from .brick import Brick


class MysqlSecureUbuntu20(Brick):
    _commands = [
        "mysql -u root -e UPDATE mysql.user SET Password=PASSWORD('{{ MYSQL_ROOT_PASSWORD }}') WHERE User='root';",
        "mysql -u root -e DELETE FROM mysql.user WHERE User=" ";",
        "mysql -u root -e DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');",
        "mysql -u root -e DROP DATABASE IF EXISTS test;",
        "mysql -u root -e DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';",
        "mysql -u root -e FLUSH PRIVILEGES;",
    ]

    _env = {"MYSQL_ROOT_PASSWORD": "password"}

    def __init__(self, name, description, cli):
        super(MysqlSecureUbuntu20, self).__init__(name, description, cli)