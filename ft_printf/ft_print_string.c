
#include "ft_printf.h"

int	ft_print_string(char *s)
{
	int	i;

	i = 0;
	if (!s)
		s = "(null)";
	while (s[i])
		i++;
	write(1, s, i);
	return (i);
}