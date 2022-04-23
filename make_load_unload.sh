#!/bin/sh

cd src/module

sudo rmmod agent.ko
make
sudo insmod agent.ko
