/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/11 19:06:53 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/11 19:12:48 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	t_list	*newnode;

	if (!lst || !f)
		return ;
	newnode = lst;
	while (newnode)
	{
		f(newnode->content);
		newnode = newnode->next;
	}
}
