
#include "ft_printf.h"

int ft_format_handler(va_list args, char format_char)
{
    if (format_char == 'c')
        return (ft_print_char(va_arg(args, int))); 
    else if (format_char == 's')
        return (ft_print_string(va_arg(args, char *)));
    else if (format_char == 'd' || format_char == 'i')
        return (ft_print_number(va_arg(args, int)));
    else if (format_char == 'x' || format_char == 'X')
        return (ft_print_hex(va_arg(args, unsigned int), format_char));
    else if (format_char == 'p')
        return (ft_print_pointer(va_arg(args, unsigned long)));
    else if (format_char == 'u')
        return (ft_print_unsigned(va_arg(args, unsigned int)));
    else if (format_char == '%')
        return (ft_print_char('%'));

    return (0);
}

int ft_printf(const char *format, ...)
{
    va_list args;
    int i = 0;
    int total_length = 0;

    va_start(args, format);
    while (format[i] != '\0')
    {
        if (format[i] == '%')
        {
            i++;
            if(format[i] == '\0')
                return (-1);
            total_length += ft_format_handler(args, format[i]);
        }
        else
        {
            write(1, &format[i], 1);
            total_length++;
        }
        i++;
    }
    va_end(args);    
    return (total_length);
}
