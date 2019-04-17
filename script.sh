#!/bin/bash
docker build -t omdb .
docker run -it omdb
