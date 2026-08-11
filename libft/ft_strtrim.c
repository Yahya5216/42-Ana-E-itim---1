
#include "libft.h"

// size_t	str_return_index(const char *big, const char *little, size_t len)
// {
// 	size_t	i;
// 	size_t	j;

// 	if (!little[0])
// 		return (-1);
// 	i = 0;
// 	while (big[i] && i < len)
// 	{
// 		j = 0;
// 		while (little[j] && big[i + j] == little[j] && (i + j) < len)
// 		{
// 			j++;
// 		}
// 		if (!little[j])
// 		{
// 			return (i);
// 		}
// 		i++;
// 	}
// 	return (-1);
// }
// char	*ft_strtrim(char const *s1, char const *set)
// {
// 	char	*d;
// 	size_t	total_len;
// 	size_t	set_len;
// 	size_t	mach;
// 	size_t	i;
	
// 	total_len = ft_strlen(s1) - ft_strlen(set);
// 	set_len = ft_strlen(set);
// 	d = (char *)malloc((total_len + 1) * sizeof(char));
// 	if (!d)
// 		return (NULL);
// 	mach = str_return_index(s1, set, set_len);
// 	if (mach == -1)
// 		return ((char *)s1);
// 	i = 0;
// 	while (i < mach)
// 		d[i] = s1[i++];
// 	i = set_len - 1;
// 	while (i < total_len)
// 		d[i] = s1[i++];
// 	d[i] = '\0';
// 	return (d);
// }