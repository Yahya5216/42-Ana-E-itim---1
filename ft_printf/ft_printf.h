
#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

int ft_printf(const char *format, ...);
int ft_format_handler(va_list args, char format_char);
int	ft_print_char(char c);
int ft_print_string(char *s);
int ft_print_number(int n);
int ft_print_unsigned(unsigned int n);
int ft_print_hex(unsigned int n, char format);
int ft_print_pointer(unsigned long ptr);

#endif