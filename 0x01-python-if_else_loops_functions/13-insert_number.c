#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * *insert_node - Function that inserts number into a sorted singly linked list
 * @head: pointer to a pointer to head
 * @numebr: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	if ((head == NULL || (*head) == NULL))
		return (NULL);

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	current = *head;

	while (current != NULL)
	{
		if (new->n < current->n)
			current = current->next;
		else
		{
			new->next = current->next;
			current->next = new;
		}
	}
	return (new);
}
