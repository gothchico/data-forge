#!/bin/bash

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="$ROOT_DIR/data-forge"
echo "PYTHONPATH set to: $PYTHONPATH"