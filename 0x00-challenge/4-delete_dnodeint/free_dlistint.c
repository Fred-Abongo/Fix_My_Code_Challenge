#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * free_dlistint - Free a list
 *
 * @head: A pointer to the first element of the list
 */
void free_dlistint(dlistint_t *head)
{
    dlistint_t *current, *tmp;

    current = head;
    while (current != NULL)
    {
        tmp = current;
        current = current->next;
        free(tmp);
    }
    head = NULL; // Optional: Set head to NULL to indicate empty list
}
