# Cinnamon
Linux introspection utility

To run and compile the project:

* I used ubuntu20.04, you probably should use too because of kernel header.
* Run the command on machine: sudo cat /proc/kallsyms | grep init_task
* Paste the address of init_task in the define "MY_INIT_TASK". Inside agent.c
* To watch the output use the "dmesg -wH" command"
* For running the module just use the "make_load_unload.sh"

* For client you can run "nc localhost 2325"

Current API:
* hola: SENDs swapper string
* bye: disconnect
* vXXXXXvXXX: v[POSTION]v[LENGTH] read bytes from postion

If you followed the steps you should see the letters "swapper" when you send "hola"



