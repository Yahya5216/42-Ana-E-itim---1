
#include <unistd.h>
#include <stdio.h>

int	ft_isalnum(int c);
int	ft_isalpha(int c);
int ft_isascii(int c);
int ft_isdigit(int c);
int ft_isprint(int c);
int ft_tolower(int c);
int ft_toupper(int c);

int main()
{
if(ft_isalnum(34))
	write(1, "bosluk", 6);
if(ft_isalnum('b'))
	write(1, "b", 1);
if(ft_isalnum('9'))
	write(1, "9", 1);
	return (0);
}

