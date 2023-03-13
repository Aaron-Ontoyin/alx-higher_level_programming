#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a linked list is palindrom
 * @head: head of linked list
 * Return: 1 if list is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_pal(head, *head));
}

/**
 * check_pal - checks if the list is palindrome
 * @head: ptr to the beginning of the list
 * @last: ptr to the end of the list
 * Return: 1 if  palindrom else 0
 */
int check_pal(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);

	if (check_pal(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

