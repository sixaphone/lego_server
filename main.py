from utils.executor import Executor
from utils.build_schema import build_schema
from utils.arg_reader import ArgReader
from utils.yaml_parser import YamlParser
from bricks import *


def main(arg_reader, yaml_parser):
    config_file = arg_reader.get_file()
    config = yaml_parser.parse(config_file)
    # executor = Executor()
    # executor.build_brickset(config)
    # executor.run()


if __name__ == "__main__":
    try:
        main(ArgReader(), YamlParser())
    except Exception as e:
        print(str(e))
        exit(1)