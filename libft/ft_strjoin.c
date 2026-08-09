/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/07 21:36:38 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/07 21:47:19 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stdlib.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*d;
	size_t	s1_len;
	size_t	s2_len;
	size_t	i;
	size_t	j;

	s1_len = ft_strlen(s1);
	s2_len = ft_strlen(s2);
	d = (char *)malloc((s1_len + s2_len) * sizeof(char));
	if (d == NULL)
		return (NULL);
	i = 0;
	while (i < s1_len)
		d[i] = s1[i++];
	j = 0;
	while (i < s1_len)
	{
		d[i] = s2[j++];
		i++;
	}
	d[i] = '\0';
	return (d);
}