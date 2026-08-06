/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/06 02:18:02 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/06 02:37:06 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	memcmp(const void *s1, const void *s2, size_t n)
{
	size_t	i;
	const unsigned char *c1;
	const unsigned char	*c2;

	c1 = (const unsigned char *)s1;
	c2 = (const unsigned char *)s2;
	if (n == 0)
		return (0);
	i = 0;
	while (c1[i] == c2[i] && i < n - 1)
	{
		i++;
	}
	return (c1[i] - c2[i]);
}