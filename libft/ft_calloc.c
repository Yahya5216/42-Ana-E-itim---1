/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/07 17:48:13 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/07 19:07:49 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
    void	*d;
	if (nmemb == 0 || size == 0)
		return (NULL);
	d = malloc(nmemb * size);
	ft_memset(d, 0, sizeof(d));
	return ((void *)(d));
}
