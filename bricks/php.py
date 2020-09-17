from .brick import Brick


class Php72Ubuntu20(Brick):
    _commands = [
        "add-apt-repository ppa:ondrej/php -y" "apt update",
        "apt install php7.2 -y",
        "apt install libapache2-mod-php7.2 -y",
        "apt install php7.2-curl -y" "apt install php7.2-gd -y",
        "apt install php7.2-recode -y",
        "apt install php7.2-tidy -y",
        "apt install php7.2-imagick -y",
        "apt install php7.2-fpm -y",
        "apt install php7.2-mbstring -y",
        "apt install php7.2-xml -y",
        "apt install php7.2-json -y",
        "apt install php7.2-common -y",
        "apt install php7.2-curl -y",
        "apt install php7.2-xmlrpc -y",
        "apt install php7.2-soap -y",
        "apt install php7.2-intl -y",
        "apt install php7.2-zip -y",
        "apt install php7.2-pgsql -y",
        "apt install php7.2-bcmath -y",
        "apt install composer -y",
    ]

    def __init__(self, name, description, cli):
        super(Php72Ubuntu20, self).__init__(name, description, cli)
