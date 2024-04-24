#!/usr/bin/env bash

unbind -n C-q
bind-key -n C-q run-shell "python $(pwd)/main.py"
