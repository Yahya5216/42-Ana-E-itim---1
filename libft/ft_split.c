
#include "libft.h"

size_t	find_words_count(char const *s, char c)
{
	size_t	words;
	size_t	i;
	size_t in_word;

	words = 0;
	i = 0;
	in_word = 0;
	while (s[i])
	{
		if(s[i] != c && !in_word)
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

size_t	find_word_len(char const *s, char c, size_t j)
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

char	**ft_split(char const *s, char c)
{
	char	**d;
	size_t	i;
	size_t	j;
	size_t	word_len;

	d = (char **)malloc((find_words_count(s, c) + 1) * sizeof(char *));
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
			return (NULL);
		ft_strlcpy(d[i++], &s[j], word_len + 1);
		j += word_len;
	}
	d[i] = NULL;
	return (d);
}
