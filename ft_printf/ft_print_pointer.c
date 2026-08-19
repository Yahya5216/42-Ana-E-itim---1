
#include "ft_printf.h"

static int ft_print_ptr_hex(unsigned long n)
{
    int     len;
    char    *base;
	char	c;

    len = 0;
    base = "0123456789abcdef";
    if (n > 15)
        len += ft_print_ptr_hex(n / 16);
	c = base[n % 16];
    write(1, &c, 1);
    len++;
    return (len);
}

int ft_print_pointer(unsigned long ptr)
{
    int len;

    len = 0;
    if (!ptr)
    {
        write(1, "(nil)", 5);
        return (5);
    }
    write(1, "0x", 2);
    len += 2;
    len += ft_print_ptr_hex(ptr);
    return (len);
}