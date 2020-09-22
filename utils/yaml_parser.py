from os import path, getcwd
from jsonschema import validate
from utils.build_schema import build_schema
import argparse
import yaml


class YamlParser:
    def parse(self, config_file):
        config = None
        with open(config_file, "r") as stream:
            config = yaml.safe_load(stream)

        validate(instance=config, schema=build_schema)

        return config