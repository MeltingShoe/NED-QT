#!/usr/bin/env bash

tmux display-popup "echo bussin"
unbind -n C-q
bind-key -n C-q run-shell "python $(pwd)/main.py"
