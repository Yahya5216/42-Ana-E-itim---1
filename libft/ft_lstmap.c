/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/11 19:12:02 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/11 20:46:48 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void 	*f(void *i)
{
	unsigned char	*d;
	unsigned int	k;

	k = 0;
	d = (unsigned char *)i;
	while (d[k])
	{
		d[k] += 1;
		k++;
	}
	return (i);
}

void del(void *i)
{
	unsigned char	*d;
	unsigned int	k;
	
	k = 0;
	d = (unsigned char *)i;
	while (d[k])
	{
		d[k] = '\0';
		k++;
	}
}

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*list;
	t_list	*new;
	t_list	*newnode;

	if (!lst || !f || !del)
		return (NULL);
	list = lst;
	while (list)
	{
		newnode = ft_lstnew(f(list->content));
		ft_lstadd_back(&new, newnode);
		if(!new)
		{
			del(new->content);
			ft_lstclear(&new, del);
		}
		list = list->next;
	}
} //   yahya    aydilek



int main()
{
	t_list	*head = NULL;
	t_list *node1;
	t_list *node2;
	t_list *current;

	node1 = ft_lstnew("Merhaba");
	ft_lstadd_back(&head, node1);
	node2 = ft_lstnew("Dünya");
	ft_lstadd_back(&head, node2);
	current = head;
	
	while (current)
	{
		printf("context: %s\n", (char *)current->content);
		current = current->next;
	}
	
	
	
}