#!/bin/bash

python3 -m pip install --upgrade pip

apt install virtualenv -y

rm -rf venv

virtualenv -p python3 venv

PWD=`pwd`

setup_env () {
  . $PWD/venv/bin/activate
  pip install -r requirements.txt --no-cache-dir
}

setup_env
