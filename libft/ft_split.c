/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/12 14:42:14 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/12 19:08:39 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	find_words_count(char const *s, char c)
{
	size_t	words;
	size_t	i;
	size_t	in_word;

	words = 0;
	i = 0;
	in_word = 0;
	while (s[i])
	{
		if (s[i] != c && !in_word)
		{
			in_word = 1;
			words++;
		}
		else if (s[i] == c)
			in_word = 0;
		i++;
	}
	return (words);
}

static size_t	find_word_len(char const *s, char c, size_t j)
{
	size_t	chars;

	chars = 0;
	while (s[j] && s[j] != c)
	{
		chars++;
		j++;
	}
	return (chars);
}

static void	clear_all(char **d)
{
	size_t	j;

	j = 0;
	if (!d)
		return ;
	while (d[j])
	{
		free(d[j]);
		j++;
	}
	free(d);
}

char	**ft_split(char const *s, char c)
{
	char	**d;
	size_t	i;
	size_t	j;
	size_t	word_len;

	d = (char **)ft_calloc((find_words_count(s, c) + 1), sizeof(char *));
	if (!d)
		return (NULL);
	i = 0;
	j = 0;
	while (i < find_words_count(s, c))
	{
		while (s[j] && s[j] == c)
			j++;
		word_len = find_word_len(s, c, j);
		d[i] = (char *)malloc((word_len + 1) * sizeof(char));
		if (!d[i])
		{
			clear_all(d);
			return (NULL);
		}
		ft_strlcpy(d[i++], &s[j], word_len + 1);
		j += word_len;
	}
	return (d);
}
