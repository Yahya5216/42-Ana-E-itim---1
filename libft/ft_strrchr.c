/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/07 17:27:46 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/07 17:48:42 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	size_t	len;

	len = 0;
	while (s[len])
	{
		len++;
	}
	while(0 < len)
	{
		if ((unsigned char)s[len] == (unsigned char)c)
			return ((char *)(&s[len]));
		len--;
	}
	if ((unsigned char)s[len] == (unsigned char)c)
			return ((char *)(&s[len]));
	return (NULL);
}