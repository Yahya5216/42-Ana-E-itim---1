/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/11 18:32:37 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/12 21:22:57 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void*))
{
	t_list	*newnode;

	if (!lst || !del || !*lst)
		return ;
	while (*lst)
	{
		newnode = (*lst)->next;
		del((*lst)->content);
		free(*lst);
		*lst = newnode;
	}
}
