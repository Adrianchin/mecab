#!/bin/sh
export FLASK_APP=./tokenizer/index.py
flask run --host=0.0.0.0 --port=8010