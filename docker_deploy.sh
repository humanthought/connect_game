#!/bin/bash

TAG=$(grep __version__ __init__.py | awk '{print $3}' | sed 's/\"//g')
docker build -t humanthought/connector_game:$TAG
docker push humanthought/connector_game:$TAG

