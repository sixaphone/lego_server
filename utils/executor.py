from utils.brick_builder import BrickBuilder
from fabric import Connection


class Executor:
    bricks = []

    def __init__(self):
        self.brick_builder = BrickBuilder()

    def build_brickset(self, config):
        bricks = config["bricks"]

        for b in bricks:
            self.bricks.append(self.brick_builder.build(b))

    def run(self):
        for brick in self.bricks:
            brick.run()
