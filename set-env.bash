#!/bin/bash

# run: ./set-path.bash

cmd='export PYTHONPATH=${PYTHONPATH}:'"`pwd`"

if ! grep -- "$cmd" ~/.bashrc > /dev/null; then
  echo "$cmd" >> ~/.bashrc
fi
