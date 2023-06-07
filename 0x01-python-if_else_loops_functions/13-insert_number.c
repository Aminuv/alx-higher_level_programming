#include "lists.h"

/**
 * insert_node - function in C that inserts a number into a sorted singly linked list.
 * @head: list of the head
 * @number: the new node
 *
 * Return: pointer
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *run, *new;

	run = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (run->next != NULL)
	{
		if ((run->next)->n >= number)
		{
			new->next = run->next;
			run->next = new;
			return (new);
		}
		run = run->next;
	}

	new->next = NULL;
	run->next = new;
	return (new);
}
