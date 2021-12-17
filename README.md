# Cinnamon
*Linux introspection utility*

## Running the module

* I used ubuntu20.04, you probably should use too because of kernel header.
* To watch the output use the **dmesg -wH** command
* For running the module just use the **make_load_unload.sh**

## Run volatility

* You can create profile using "create_profile.sh". the output will be in *profile/* folder.
Copy the profile to volatility folder (usually *volatility/volatility/plugins/overlays/linux*)
* For using volatility: **vol.py -l 127.0.0.1::2325 --profile=Linuxubuntu20x64 linux_pslist**

## Client Features
* For simple client you can run **nc localhost 2325**

Current API:
* hola: Get "swapper" (init_task) physical address
* bye: Disconnect
* vXXXXXvXXX: v[POSTION]v[LENGTH] Read bytes from position