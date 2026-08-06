/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/05 18:37:04 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/06 01:05:31 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *s, int c, size_t n)
{
	unsigned char	*str;
	size_t	i;

	str = (unsigned char *)s;
	i = 0;
    while (i < n)
    {
		str[i] = (unsigned char)c;
		i++;
    }
	return (s);
}
