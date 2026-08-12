/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/11 19:12:02 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/12 22:01:51 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
/*
void	*f(void *i)
{
	unsigned char	*d;
	unsigned int	k;	

	k = 0;
	d = (unsigned char *)i;
	while (d[k])
	{
		d[k] = d[k] + 1;
		k++;
	}
	return ((void *)d);
}

void	del(void *i)
{
	unsigned char	*d;
	unsigned int	k;

	k = 0;
	d = (unsigned char *)i;
	while (d[k])
	{
		d[k] = 0;
		k++;
	}
}
*/
t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*list;
	t_list	*new;
	t_list	*newnode;

	if (!lst || !f || !del)
		return (NULL);
	list = lst;
	new = NULL;
	while (list)
	{
		newnode = ft_lstnew((void *)f(list->content));
		if (!newnode)
		{
			ft_lstclear(&newnode, del);
			free(newnode);
		}
		ft_lstadd_back(&new, newnode);
		list = list->next;
	}
	return (new);
}
/*
int main()
{
	t_list	*head = NULL;
	t_list *node1;
	t_list *node2;
	t_list *current;

	char d[] = "merhaab";
	char c[] = "kaan";
	node1 = ft_lstnew(d);
	ft_lstadd_back(&head, node1);
	node2 = ft_lstnew(c);
	ft_lstadd_back(&head, node2);
	ft_lstmap(head, f, del);
	current = head;
	while (current)
	{
		printf("context: %s\n", (char *)current->content);
		printf("context: %p\n", (void *)current->next);
		current = current->next;
	}
}
	*/