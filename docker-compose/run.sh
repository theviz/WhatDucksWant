#!/bin/bash
sudo docker-compose build
sudo docker-compose up -d
sudo docker logs --follow docker-compose_app_1
