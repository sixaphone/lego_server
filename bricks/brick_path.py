from os import path, getcwd


def brick_path(append=""):
    return path.join(path.dirname(path.realpath(__file__)), append)
