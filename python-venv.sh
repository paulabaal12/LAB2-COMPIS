#!/bin/bash

python3 -m venv /opt/venv
source /opt/venv/bin/activate
pip install --upgrade pip
ln -sf /opt/venv/bin/python /usr/local/bin/python
ln -sf /opt/venv/bin/pip /usr/local/bin/pip

echo "Python virtual environment created and activated successfully"