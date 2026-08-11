/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yaydilek <yaydilek@student.42istanbul.c    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/08/10 16:27:52 by yaydilek          #+#    #+#             */
/*   Updated: 2026/08/11 21:25:40 by yaydilek         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <fcntl.h>
void	ft_putchar_fd(char c, int fd)
{
    write(fd, &c, 1);
}
int main()
{
int f = 2;
// f = open("a.txt", O_CREAT | O_WRONLY , 0777);

// printf("%d",f);

ft_putchar_fd('a',f);
}