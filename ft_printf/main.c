
#include <stdio.h>
#include "ft_printf.h"

int main(void)
{
    printf("%d\n", printf("yahya %z yahya"));
    printf("%d\n", ft_printf("yahya %z yahya"));
}
