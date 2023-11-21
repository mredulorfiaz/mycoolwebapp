#!/bin/bash

set -e

(while ! nc -z -w 1 db 3306; do echo "$(date) waiting for mysql to start"; sleep 5; done)

python main.py
