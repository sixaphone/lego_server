from utils.executor import Executor
import argparse
from os import path, getcwd
from bricks.apache import ApacheUbuntu20
import yaml


def get_file():
    arg_parser = argparse.ArgumentParser(description="Run pipeline")
    arg_parser.add_argument(
        "--file", required=True, type=str, help="Config file to load pipeline"
    )
    arguments = arg_parser.parse_args()

    return path.join(getcwd(), "builds", arguments.file)


if __name__ == "__main__":
    config_file = get_file()
    config = None
    with open(config_file, "r") as stream:
        config = yaml.safe_load(stream)

    executor = Executor()
    executor.build_brickset(config)
    executor.run()