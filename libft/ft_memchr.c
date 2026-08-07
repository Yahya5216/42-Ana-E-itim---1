/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/06 01:09:34 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/07 20:09:19 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void *memchr(const void *s, int c, size_t n)
{
    size_t i;
    unsigned char *a;

    i = 0;
    a = (unsigned char *)s;
    while (i < n)
    {
        if (a[i] == (unsigned char)c)
            return (void *)(a+i);
        i++;
    }
    return (NULL);
}
