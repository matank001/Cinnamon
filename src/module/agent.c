
#include <linux/module.h>	/* Needed by all modules */
#include <linux/kernel.h>	/* Needed for KERN_INFO */
#include <linux/sched.h>
//#include <asm/io.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Cinnamon Group");
MODULE_DESCRIPTION("A simple example Linux module");
MODULE_VERSION("1.0");

const void* MY_INIT_TASK = 0xffffffff8b813780; //sudo cat /proc/kallsyms | grep init_task
const size_t SWAPPER_LENGTH = 7;

int init_module(void)
{
    size_t i;
    void __iomem *io;
	printk(KERN_INFO "Cinnamon: Hello world\n");

    phys_addr_t physical_init_task = virt_to_phys(MY_INIT_TASK);
    printk(KERN_INFO "Cinnamon: Physical Address: %llu\n", physical_init_task);

    struct task_struct* swapper = MY_INIT_TASK;
    size_t swapper_offset_comm = (size_t)swapper->comm - (size_t)MY_INIT_TASK;

    printk(KERN_INFO "Cinnamon: Swapper comm offset %lu\n", swapper_offset_comm);

    io = ioremap(physical_init_task, 4096);

    if (io == NULL)
    {
        printk(KERN_INFO "Cinnamon: Failed obtain ioremap\n");
        return 0;
    }
    
    for (i = swapper_offset_comm; i < swapper_offset_comm + SWAPPER_LENGTH; i++)
    {
        char current_char = (char)ioread8(io + i);
        printk(KERN_INFO "%c", current_char);
    }

    printk(KERN_INFO "Cinnamon: Finish Writing\n");
    iounmap(io);
	return 0;
}

void cleanup_module(void)
{
	printk(KERN_INFO "Cinnamon: Goodbye world\n");
}