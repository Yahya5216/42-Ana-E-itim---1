/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/22 20:46:20 by aryaprak          #+#    #+#             */
/*   Updated: 2026/08/29 18:30:57 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	rotate_stack(t_node **stack)
{
	t_node	*temp;
	t_node	*last_node;

	if (!stack || !*stack || !(*stack)->next)
		return (0);
	temp = *stack;
	*stack = (*stack)->next;
	last_node = find_last_node(stack);
	last_node->next = temp;
	temp->next = NULL;
	return (1);
}

void	ra(t_node **a, t_benchmark *bench)
{
	if (!rotate_stack(a))
		return ;
	printf_count_only(bench, "ra\n", 3);
	benchmark_count(bench, OP_RA);
}

void	rb(t_node **b, t_benchmark *bench)
{
	if (!rotate_stack(b))
		return ;
	printf_count_only(bench, "rb\n", 3);
	benchmark_count(bench, OP_RB);
}

void	rr(t_node **a, t_node **b, t_benchmark *bench)
{
	int	a_rotated;
	int	b_rotated;

	a_rotated = rotate_stack(a);
	b_rotated = rotate_stack(b);
	if (!a_rotated && !b_rotated)
		return ;
	printf_count_only(bench, "rr\n", 3);
	benchmark_count(bench, OP_RR);
}
