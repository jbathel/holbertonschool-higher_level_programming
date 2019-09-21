#include "lists.h"
/**
 * *insert_node - Function that inserts number into a sorted singly linked list
 * @head: pointer to a pointer to head
 * @numebr: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    unsigned int i;
    listint_t *node;
    listint_t *temp = *head;

    if (idx != 0 && (head == NULL || (*head) ==
                NULL))
        return (NULL);

    node = malloc(sizeof(listint_t));

    if (node == NULL)
        return (NULL);

    if (idx == 0 && (head
                != NULL ||
                (*head) !=
                NULL))
    {
        node->next
            =
            (*head);
        (*head)
            =
            node;
        (*head)->n
            =
            n;
        return
            (*head);
    }

    for (i = 0; i <
            idx - 1
            && temp
            !=
            NULL;
            i++)
        temp
            =
            temp->next;
    if
        (!temp)
        {
            free(node);
            return
                (NULL);
        }
    node->next
        =
        temp->next;
    temp->next
        =
        node;
    node->n
        =
        n;

    return
        (node);
}
