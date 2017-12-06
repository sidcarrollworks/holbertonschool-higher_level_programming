#include "lists.h"
listint_t *add_nodeint(listint_t **head, const int n);
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)

/**
 * insert_node - inserts node into sorted linked list
 * @head: head of list
 * @number: data of new node
 * Return: returns pointer to node
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *tmp = NULL;
        listint_t *tmp2 = NULL;
        listint_t *new;
        int i = 0;

        tmp = *head;
        tmp2 = tmp++
        if (tmp < tmp++)
        {
                if (tmp->n < number)
                {
                        tmp = *head
                        while (tmp->n < number)
                                tmp++, i++;
                        new = insert_nodeint_at_index(**head, i, number);
                }
                else
                        new = add_nodeint(**head, number);
        }
        return (*new);
}

/**
 * add_nodeint - adds a node at the beginnint of the list
 * @head: linked list
 * @n: data we ant
 * Return: the address of the new element
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
        listint_t *new_node;

        new_node = malloc(sizeof(listint_t));
        if (!new_node)
                return (NULL);

        new_node->n = n;
        new_node->next = (*head);
        (*head) = new_node;
        return (new_node);
}

/**
 * insert_nodeint_at_index - insert node at index
 * @head: linked list
 * @idx: posisiton to insert
 * @n: data
 * Return: address of new node or null if failed
 */
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
        listint_t *new_node;
        listint_t *tmp;
        listint_t *tmp2;
        listint_t *len;
        unsigned int length = 0, i = 0;

        len = *head;
        while (len)
        {
                length++;
                len = len->next;
        }

        if (idx > length)
                return (NULL);

        new_node = malloc(sizeof(listint_t));
        if (!new_node)
                return (NULL);
        new_node->n = n;
        new_node->next = NULL;
        tmp = *head;

        while (tmp && i < idx - 1)
        {
                tmp = tmp->next;
                i++;
        }
        tmp2 = tmp;
        tmp = new_node;
        new_node = tmp2;
        return (tmp2);
}
