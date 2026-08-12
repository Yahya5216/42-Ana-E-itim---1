/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/12 14:40:17 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/12 18:45:45 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	return_start_index(char const *s1, char const *set)
{
	size_t	i;
	size_t	j;
	int		flag;

	flag = 0;
	i = 0;
	while (s1[i])
	{
		j = 0;
		flag = 0;
		while (set[j])
		{
			if (s1[i] == set[j])
				flag = 1;
			j++;
		}
		if (flag == 0)
			return (i);
		i++;
	}
	return (i);
}

static size_t	return_last_index(char const *s1, char const *set)
{
	size_t	i;
	size_t	j;
	int		flag;

	flag = 0;
	i = ft_strlen(s1) - 1;
	while (1)
	{
		j = 0;
		flag = 0;
		while (set[j])
		{
			if (s1[i] == set[j])
				flag = 1;
			j++;
		}
		if (flag == 0)
			return (i);
		if (i == 0)
			break ;
		i--;
	}
	return (0);
}

static void	fill_the_char(size_t start, size_t last, char *d, char const *s1)
{
	size_t	i;

	i = 0;
	while (start <= last)
	{
		d[i] = s1[start];
		start++;
		i++;
	}
	d[i] = '\0';
}

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*d;
	size_t	start_index;
	size_t	last_index;

	start_index = return_start_index(s1, set);
	last_index = return_last_index(s1, set);
	if (s1[start_index] == '\0')
	{
		d = (char *)malloc(1 * sizeof(char));
		if (!d)
			return (NULL);
		d[0] = '\0';
		return (d);
	}
	d = (char *)malloc((last_index - start_index + 2) * sizeof(char));
	if (!d)
		return (NULL);
	fill_the_char(start_index, last_index, d, s1);
	return (d);
}
