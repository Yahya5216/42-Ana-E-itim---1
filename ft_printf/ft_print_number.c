
#include "ft_printf.h"

int ft_print_number(int n)
{
    long    nb;
    int     len;
    char    c;

    nb = n;
    len = 0;
    if (nb < 0)
    {
        write(1, "-", 1);
        len++;
        nb = -nb;
    }
    if (nb > 9)
        len += ft_print_number(nb / 10);
    c = (nb % 10) + '0';
    write(1, &c, 1);
    len++;
    return (len);
}
