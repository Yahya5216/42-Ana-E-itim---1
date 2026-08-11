/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/11 14:11:13 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/11 18:24:31 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	t_list	*newnode;

	if (!lst)
		return (NULL);
	newnode = lst;
	while (newnode->next)
	{
		newnode = newnode->next;
	}
	return (newnode);
}
