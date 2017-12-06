#include "lists.h"

/**
 * insert_node - inserts node in sorted list
 * @head: head node
 * @number: number to be inserted
 * Return: new head node
 */
listint_t *insert_node(listint_t **head, int number)
{
        int i = 0, f = 0;
        listint_t *tmp;
        listint_t *new_node;

        new_node = malloc(sizeof(listint_t));
        if (new_node == NULL)
                return (NULL);

        tmp = *head;
        while (tmp != NULL)
        {
                if (i == 0 && tmp->n >= number)
                {
                        f++;
                        break;
                }
                if (tmp->n <= number && (tmp->next == NULL || tmp->next->n >= number))
                        break;
                tmp = tmp->next;
                i++;
        }

        tmp = *head;
        while (i != 0)
                tmp = tmp->next, i--;
        
        new_node->n = number;
        if (*head == NULL)
                new_node->next = NULL, *head = new_node;
        else if (f)
                new_node->next = tmp, *head = new_node;
        else
                new_node->next = tmp->next, tmp->next = new_node;
        return (*head);
}
