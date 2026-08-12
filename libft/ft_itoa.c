/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/12 14:42:41 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/12 19:29:40 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	return_len(long n)
{
	size_t	len;

	len = 0;
	if (n == 0)
		return (1);
	if (n < 0)
	{
		len++;
		n *= -1;
	}
	while (n > 0)
	{
		n = n / 10;
		len++;
	}
	return (len);
}

static void	fill_to_char(long nb, char *d, size_t len)
{
	if (nb < 0)
	{
		nb *= -1;
		d[0] = '-';
	}
	while (nb > 0)
	{
		d[--len] = (nb % 10) + '0';
		nb = nb / 10 ;
	}
}

char	*ft_itoa(int n)
{
	char	*d;
	size_t	len;
	long	nb;

	nb = n;
	len = return_len(nb);
	d = (char *)malloc((len + 1) * sizeof(char));
	if (!d)
		return (NULL);
	d[len] = '\0';
	if (nb == 0)
	{
		d[0] = '0';
		return (d);
	}
	fill_to_char(nb, d, len);
	return (d);
}
