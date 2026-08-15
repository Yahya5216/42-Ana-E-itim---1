/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/11 19:12:02 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/13 14:16:31 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static void	clear_all(t_list *new, void *new_content, void (*del)(void *))
{
	if (new_content)
		del(new_content);
	ft_lstclear(&new, del);
}

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*list;
	t_list	*new;
	t_list	*newnode;
	void	*new_content;

	if (!lst || !f || !del)
		return (NULL);
	list = lst;
	new = NULL;
	while (list)
	{
		new_content = f(list->content);
		newnode = ft_lstnew(new_content);
		if (!newnode)
		{
			clear_all(new, new_content, del);
			return (NULL);
		}
		ft_lstadd_back(&new, newnode);
		list = list->next;
	}
	return (new);
}
