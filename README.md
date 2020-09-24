# Lego server 

A plug and play structure to automate your server deployment. Build a set of bricks and watch your application go up and running.

### Requirements

```
python >= 3.6.2
pip >= 3
git
```

### Installation

Clone the repository using `git cli` or a GUI tool and open the directory.

```bash
git clone https://github.com/sixaphone/lego_server.git
cd lego_server
```

Run the `setup.sh` script.

```sh
sudo ./setup.sh $USER
```

The script needs to be executed as a sudo user, but in order to have access to venv we pass our current `$USER` as an argument and the script will set him as the owner.

Then activate the virtualenv

```sh
source ./venv/bin/activate
```

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

  If some step requires more complex bash operations you can make a script file for it in the `scripts` folder and it will be executed remotely.

- `utils`

  Here lie helper classes and methods such as the main executor, cli helper, and cli factory.

- `builds`

  The app uses `yaml` configuration to run your pipeline. Configs are defined in the build folder and resolved to it on app start. The standard format for the configuration file is:


  ```yaml
  build_set: LAMP stack deployment setup

  connection:
    name: default # custom name
    auth_type: password # supports password and key (ssh key)
    password: ee885d3b2be340f0e304e11a53 # required for sudo access
    host: 46.101.106.60 # host ip or dns 
    user: root # user with sudo privileges
    # optional array of watchers used by fabric. Consult fabric docs for more info
    watchers: 
      - pattern: '\[sudo\] password:'
        response: ee885d3b2be340f0e304e11a53

  bricks:
    - name: Apache
      description: Install apache2 on ubuntu 20
      class: ApacheUbuntu20
      module: apache
      # define custom connection for specific step
      connection:
          name: apache
          auth_type: password
          password: pass
          host: 46.101.106.61 
          user: root

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
      # override env variables
      env:
        MYSQL_ROOT_PASSWORD: SuperSecurePassword

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
class Brick(ABC):
    # ... abstract logic
```

The base brick class defines methods to update env variables and run commands. Each of these methods can be overridden in child classes. We can make the most use of it for the `run` method (will be later shown). 

By default the base method handles composition ,cli execution and env variable injection.

Example of a child brick class:

```python
from bricks.brick import Brick


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
```

This brick contains all commands required to run `mysql_secure_installation`. Every brick should define a list of commands that they execute. They can also define a set of environment variables to use during the deployment. Base class will overried the `MYSQL_ROOT_PASSWORD` property before executing. 

Another useful thing is the brick composition. We can make bricks that use other bricks as commands.

```python
# bricks/apache_mysql.py
from bricks.brick import Brick
from os import path, getcwd
from utils.brick_builder import BrickBuilder


builder = BrickBuilder()

class ApacheMysqlUbuntu20(Brick):
    _commands = [
        builder.build(
            {
                "name": "Apache2",
                "description": "Install Apache2",
                "module": "apache",
                "class": "ApacheUbuntu20",
                # "env": ...
                # "connection": ...
            }
        ),
        builder.build(
            {
                "name": "Mysql",
                "description": "Install Mysql",
                "module": "mysql",
                "class": "MysqlUbuntu20",
            }
        ),
    ]

    def __init__(self, name, description, cli):
        super(ApacheMysqlUbuntu20, self).__init__(name, description, cli)

```

Here we defined a brick in the file `apache_mysql.py`, `apache` and `mysql` bricks are defined separate. Using brick builder we can provide a config object to instantiate a command like we would in `yml` files. In our build `yml` file we would define a step:

```yaml
  - name: Apache and Mysql 
    description: Install Apache and Mysql
    class: ApacheMysqlUbuntu20
    module: apache_mysql
```

The base `run` method will determin if we are running a brick or command and based on that execute cli command or the bricks run method. Composition, however, does not provide as much freedom as simple brick.

--- 

## Usage
<br>

  1. Create all the required bricks for your set in the `bricks` folder. You can also make use of predefined bricks. Also make sure to add config files and scripts if needed.

  2. Define a YAML file in the `builds` folder. The required part of the file is the bricks array containing the definition for all the steps in the pipeline. For each brick `name`, `description`, `class` and `module` are required. You can also define `env` variables in this file which will override and append to the base env variables in the brick.

  3. Activate virtualenv if it is not active

  4. Run your configuration with `python main.py --file <file>`
      
      Example: `python main.py --file lamp.yml`

--- 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Prefer to use conventional commits for your branches and messages.

--- 

## License
[MIT](https://choosealicense.com/licenses/mit/)

