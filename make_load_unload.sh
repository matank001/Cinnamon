#!/bin/sh

cd src/module

make
sudo insmod agent.ko
sudo rmmod agent.ko