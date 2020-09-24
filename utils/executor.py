from utils.brick_builder import BrickBuilder


class Executor:
    bricks = []

    def __init__(self):
        self.brick_builder = BrickBuilder()

    def build_brickset(self, config):
        setup_brick = self.brick_builder.build(
            {
                "name": "Setup",
                "description": "Initialize config and scripts",
                "module": "setup",
                "class": "Setup",
            },
            config["connection"],
        )

        clean_up_brick = self.brick_builder.build(
            {
                "name": "Clean up",
                "description": "Remove config and scripts",
                "module": "clean_up",
                "class": "CleanUp",
            },
            config["connection"],
        )

        self.bricks.append(setup_brick)

        for b in config["bricks"]:
            self.bricks.append(self.brick_builder.build(b, config["connection"]))

        self.bricks.append(clean_up_brick)

    def run(self):
        for brick in self.bricks:
            brick.run()
