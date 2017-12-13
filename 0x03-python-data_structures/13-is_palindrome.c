#include "lists.h"

/**
 * is_palindrome - finds if linked list is palindrome
 * @head: pointer to list
 * Return: 0 if not and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *finder;
	int i;
	int *number;
	int length;

	finder = *head;

	while (finder != NULL)
		finder = finder->next, length++;

	number = malloc(sizeof(int) * length);
	if (!number)
		return (0);

	finder = *head;
	i = 0;
	while (finder)
	{
		number[i++] = finder->n;
		finder = finder->next;
	}
	
	i = 0, length--;
	while (number[i] == number[length])
	{
		if (i == length || i > length)
		{
			free(number);
			return(1);
		}
		i++, length--;
	}
	free(number);
	return (0);
}
