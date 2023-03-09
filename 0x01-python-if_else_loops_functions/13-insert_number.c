#include "lists.h"

/**
 * insert_node - inserts a numer in a sorted singly linked list
 * @head: pointer to pointer of head of list
 * @number: number to insert
 * Return: pointer to new node; NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = (NULL);

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	/* insert the new node */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
