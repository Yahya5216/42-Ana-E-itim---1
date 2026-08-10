
#ifndef LIBFT_H
# define LIBFT_H

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

typedef struct	s_list
{
	void *content;
	struct s_list *next;
}	t_list;

void    *ft_memset(void *s, int c, size_t n);
size_t  ft_strlen(const char *str);
char	*strnstr(const char *big, const char *little, size_t len);
size_t ft_strlcpy(char *dst, const char *src, size_t size);

#endif
