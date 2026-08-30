
#include "ft_printf.h"

int	ft_print_string(char *s)
{
	int	i;

	i = 0;
	if (!s)
	{
		write(1, "(null)", 6);
        return (6);
	}
	while (s[i])
		i++;
	write(1, s, i);
	return (i);
}