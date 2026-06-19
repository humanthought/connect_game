#!/bin/bash
# AI disclosure: docker commands were created by claude. TAG variable added manually.

TAG=$(grep __version__ __init__.py | awk '{print $3}' | sed 's/\"//g')
docker build -t humanthought/connect_game:$TAG .
docker push humanthought/connect_game:$TAG

