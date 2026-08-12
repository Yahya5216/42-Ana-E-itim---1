/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/07 21:36:38 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/12 19:04:54 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static void	fill_s1(char const *s1, char *d, int s1_len, int i)
{
	while (i < s1_len)
	{
		d[i] = s1[i];
		i++;
	}
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*d;
	size_t	s1_len;
	size_t	s2_len;
	size_t	i;

	if (!s1 || !s2)
		return (NULL);
	s1_len = ft_strlen(s1);
	s2_len = ft_strlen(s2);
	d = (char *)malloc((s1_len + s2_len + 1) * sizeof(char));
	if (d == NULL)
		return (NULL);
	i = 0;
	fill_s1(s1, d, s1_len, i);
	i += s1_len;
	s1_len = 0;
	while (s1_len < s2_len)
	{
		d[i] = s2[s1_len++];
		i++;
	}
	d[i] = '\0';
	return (d);
}
