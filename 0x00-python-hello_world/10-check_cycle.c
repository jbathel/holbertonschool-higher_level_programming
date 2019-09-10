#include "lists.h"

/**
 * check_cycle - calls function
 * @list: pointer to list
 * Description: Function that checks for a loop in a linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tortoise = list;

	if (!list)
		return (0);

	hare = list->next->next;
	tortoise = list->next;

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
