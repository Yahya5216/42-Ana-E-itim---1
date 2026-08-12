/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/11 14:32:58 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/12 22:02:18 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*newnode;

	if (!new || !lst)
		return ;
	if (!(lst[0]))
	{
		*lst = new;
		return ;
	}
	newnode = ft_lstlast(*lst);
	newnode->next = new;
}
