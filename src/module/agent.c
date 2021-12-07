
#include <linux/module.h>	/* Needed by all modules */
#include <linux/kernel.h>	/* Needed for KERN_INFO */

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Cinnamon Group");
MODULE_DESCRIPTION("A simple example Linux module");
MODULE_VERSION("1.0");

int init_module(void)
{
	printk(KERN_INFO "Cinnamon: Hello world\n");

	/* 
	 * A non 0 return means init_module failed; module can't be loaded. 
	 */
	return 0;
}

void cleanup_module(void)
{
	printk(KERN_INFO "Cinnamon: Goodbye world\n");
}