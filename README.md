# Lego server 

A plug and play structure to automate your server deployment. Build a set of bricks and watch your application go up and running.

### Requirements

```
python >= 3.6.2
an account with sudo permissions
```

### Installation

Clone the repository using `git cli` or a GUI tool.

### Folder structure

```
├── bricks
│   └── config
├── builds
├── main.py
└── utils
```

- `bricks`

  All steps are categorized as bricks. each brick contains a set of commands for a part in your pipeline. For example, you might have a brick to install `apache` and `MySQL` or `PHP` with `composer`. In bricks, you have some predefined classes, but you can customize your own for use.

  You can also use predefined configurations and files such as `apache2.conf` to include during your pipeline. They are stored in the `config` folder.

- `utils`

  Here lie helper classes and methods such as the main executor, cli helper, and cli factory.

- `builds`

  The app uses `yaml` configuration to run your pipeline. Configs are defined in the build folder and resolved to it on app start. The standard format for the configuration file is:


  ```yaml
  build_set: "LAMP stack deployment setup"
  bricks:
    - name: Apache
      description: Install apache2 on ubuntu 20
      class: ApacheUbuntu20
      module: apache

    - name: UFW
      description: Setup UFW rules
      class: UFW
      module: ufw

    - name: Mysql 
      description: Install mysql server
      class: MysqlUbuntu20
      module: mysql

    - name: Mysql Secure
      description: Run mysql_secure_installation
      class: MysqlSecureUbuntu20
      module: mysql_secure
      env:
        MYSQL_ROOT_PASSWORD: password

    - name: PHP7.2
      description: Install php7.2 and deps
      class: Php72Ubuntu20
      module: php
  ``` 

--- 

## Defining bricks

A brick is a class that encapsulates all your logic for a step in the pipeline. Every brick should inherit from the base `Brick` class.

```python
# brick.py
from abc import ABC


class Brick(ABC):

    _env = {}
    _commands = []

    def __init__(self, name, description, cli):
        self.name = name
        self.description = description
        self.cli = cli

    def __str__(self):
        return f"{self.name}: {self.description}"

    def run(self):
        for cmd in self._commands:
            print(self.cli.run_command(cmd))

    def update_env(self, overrides):
        self._env = {**self._env, **overrides}

```

The base brick class defines methods to update env variables and run commands. Each of these methods can be overridden in child classes. We can make the most use of it for the `run` method (will be later shown).

Example of a child brick class:

```python
class MysqlSecureUbuntu20(Brick):
    _env = {"MYSQL_ROOT_PASSWORD": "password"}

    def __init__(self, name, description, cli):
        super(MysqlSecureUbuntu20, self).__init__(name, description, cli)

    def run(self):
        _commands = [
            "mysql -u root -e UPDATE mysql.user SET Password=PASSWORD({}) WHERE User='root';".format(
                self._env["MYSQL_ROOT_PASSWORD"]
            ),
            "mysql -u root -e DELETE FROM mysql.user WHERE User=" ";",
            "mysql -u root -e DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');",
            "mysql -u root -e DROP DATABASE IF EXISTS test;",
            "mysql -u root -e DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';",
            "mysql -u root -e FLUSH PRIVILEGES;",
        ]
        super(MysqlSecureUbuntu20, self).run()

```

This brick contains all commands required to run `mysql_secure_installation`. Every brick should define a list of commands that they execute. They can also define a set of environment variables to use during the deployment. We see that run was overridden to defined commands using env values.

Another useful thing is the brick composition. We can make bricks that use other bricks as commands.

```python
from .brick import Brick
from os import path, getcwd
from utils.brick_builder import BrickBuilder


builder = BrickBuilder()


class MysqlUbuntu20(Brick):
    _commands = [
        "apt install mysql-server mysql-client -y",
    ]

    def __init__(self, name, description, cli):
        super(MysqlUbuntu20, self).__init__(name, description, cli)


class ApacheUbuntu20(Brick):
    _commands = [
        "apt install apache2 -y",
        f'cp {path.join(path.dirname(path.realpath(__file__)), "config/apache2.conf")} /etc/apache2/apache2.conf',
    ]

    def __init__(self, name, description, cli):
        super(ApacheUbuntu20, self).__init__(name, description, cli)


class ApacheMysqlUbuntu20(Brick):
    _commands = [
        builder.build(
            {
                "name": "Apache2",
                "description": "Install Apache2",
                "module": "apache_mysql",
                "class": "ApacheUbuntu20",
            }
        ),
        builder.build(
            {
                "name": "Mysql",
                "description": "Install Mysql",
                "module": "apache_mysql",
                "class": "MysqlUbuntu20",
            }
        ),
    ]

    def __init__(self, name, description, cli):
        super(ApacheMysqlUbuntu20, self).__init__(name, description, cli)

    def run(self):
        for brick in self._commands:
            brick.run()

```

Here we defined two bricks in a file we call `mysql_apache.py`, the bricks can be defined in their separate folder ofc. Using brick builder we can provide a config object to instantiate a command like we would in yml files. After that, we need to override the `run` method to execute the run methods of its containing bricks.

--- 

## Usage
<br>

  1. Create all the required bricks for your set in the `bricks` folder. You can also make use of predefined bricks.

  2. Define a YAML file in the `builds` folder. The required part of the file is the bricks array containing the definition for all the steps in the pipeline. For each brick `name`, `description`, `class` and `module` are required. You can also define `env` variables in this file which will override and append to the base env variables in the brick.

  3. Run your configuration with `python main.py --file <file>`
      
      Example: `python main.py --file lamp.yml`

--- 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Prefer to use conventional commits for your branches and messages.

--- 

## License
[MIT](https://choosealicense.com/licenses/mit/)

