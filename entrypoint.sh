#!/usr/bin/env bash

chmod 777 ./entryfile.sh
./entryfile.sh

exec "$@"