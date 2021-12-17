# Cinnamon
Linux introspection utility

To run and compile the project:

* I used ubuntu20.04, you can use any linux dist.
* Run the command on machine: sudo cat /proc/kallsyms | grep init_task
* Paste the address of init_task in the variable "MY_INIT_TASK".
* To watch the output use the "dmesg -wH" command"
* For running the module just use the "make_load_unload.sh"

If you followed the steps you should see the letters: s w a p p e r



