/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/11 13:59:23 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/11 18:25:17 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

unsigned int	ft_lstsize(t_list *lst)
{
	t_list			*newnode;
	unsigned int	i;

	i = 0;
	if (!lst)
		return (0);
	newnode = lst;
	while (newnode)
	{
		newnode = newnode->next;
		i++;
	}
	return (i);
}
