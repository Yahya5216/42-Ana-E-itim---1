
#include "ft_printf.h"

int ft_format_handler(va_list args, char format_char)
{
    int print_length = 0;

    if (format_char == 'c')
    {
        print_length += ft_print_char(va_arg(args, int)); 
    }
    else if (format_char == 's')
    {
        print_length += ft_print_string(va_arg(args, char *));
    }
    else if (format_char == 'd' || format_char == 'i')
    {
        print_length += ft_print_number(va_arg(args, int));
    }
    else if (format_char == 'x' || format_char == 'X')
    {
        print_length += ft_print_hex(va_arg(args, unsigned int), format_char);
    }
    else if (format_char == 'p')
    {
        print_length += ft_print_pointer(va_arg(args, unsigned long));
    }
    else if (format_char == 'u')
    {
        print_length += ft_print_unsigned(va_arg(args, unsigned int));
    }
    else if (format_char == '%')
    {
        print_length += ft_print_char('%');
    }

    return (print_length);
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
