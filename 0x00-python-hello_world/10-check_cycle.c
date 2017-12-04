#include "lists.h"
/**
 * check_cycle - check for a loop in linked list
 * @list: head of list
 * Return: 0 if no cycle and 1 if cycle
 */
int check_cycle(listint_t *list)
{
        listint_t *current = list;
        listint_t *check = NULL;
        int since = 0;
        int sinceScale = 2;

        do
        {
                if (check == current)
                        return (1);
                if (since >= sinceScale)
                {
                        check = current;
                        since = 0;
                        sinceScale = 2 * sinceScale;
                }
                since++;
        } while ((current = current->next) != NULL);
        return (0);
}
