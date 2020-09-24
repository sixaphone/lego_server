from os.path import join
from os import getcwd
from settings import APP_DIR


def app_path(*appends):
    return join(APP_DIR, *appends)


def brick_path(*appends):
    return app_path("bricks", *appends)