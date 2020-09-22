import argparse
from os import path, getcwd


class ArgReader:
    def get_file(self):
        arg_parser = argparse.ArgumentParser(description="Run pipeline")
        arg_parser.add_argument(
            "--file", required=True, type=str, help="Config file to load pipeline"
        )
        arguments = arg_parser.parse_args()

        return path.join(getcwd(), "builds", arguments.file)
