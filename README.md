# Cinnamon
*Linux introspection utility*

## Loading the module (on target machine)

* The module should run inside the target machine
* I used ubuntu20.04, you probably should use too because of kernel header.
* To watch the output use the **dmesg -wH** command
* For running the module just use the **make_load_unload.sh**

## Run volatility inside a container

* The app can run from anywhere with network access to target machine
* First create the image (There isn't a public image yet): **docker build -t cinnamon .**
* For running and executing commands: **docker run --network host -it cinnamon /bin/bash**
* See next part for the commands

## Run volatility

* You can create profile using "create_profile.sh". the output will be in *profile/* folder.
Copy the profile to volatility folder (usually *volatility/volatility/plugins/overlays/linux*)
* For using volatility: **python2 vol.py -l [IP]::2325 --profile=Linuxubuntu20x64 linux_pslist**

## Client Features
* For simple client you can run **nc localhost 2325**

Current API:
* hola: Get "swapper" (init_task) physical address
* bye: Disconnect
* vXXXXXvXXX: v[POSTION]v[LENGTH] Read bytes from position

## TODO
* Finish the investegatee docketfile
* Change the docker run execution args to network bridge and add -p (enalbe containers to ssh to one another)
* finish checking the automation process