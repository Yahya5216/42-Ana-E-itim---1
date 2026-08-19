
#include "ft_printf.h"

int	ft_print_hex(unsigned int n, char format)
{
	char *base;
	char c;
	int len;

	if (format == 'x') base = "0123456789abcedf";
	else base = "0123456789ABCDEF";
	len = 0;
	if (n > 15)
	{
		n = n / 16;
		len += ft_print_hex(n, format);
	}
	c = base[n % 16];
	write(1, &c, 1);
	len++;
	return (len);
}
