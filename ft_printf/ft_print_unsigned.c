
#include "ft_printf.h"

int ft_print_unsigned(unsigned int n)
{
    int     len;
    char    c;

    len = 0;
    if (n > 9)
        len += ft_print_unsigned(n / 10);
    c = (n % 10) + '0';
    write(1, &c, 1);
    len++;
    return (len);
}
