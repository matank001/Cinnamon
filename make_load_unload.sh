#!/bin/sh

cd src/module

echo $1 | sudo -S rmmod agent.ko
make
echo $1 | sudo -S insmod agent.ko
