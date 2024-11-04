#!/bin/bash
set -e

echo "Removing: $1"
./venv/bin/python remover.py $1

echo "Success!"
