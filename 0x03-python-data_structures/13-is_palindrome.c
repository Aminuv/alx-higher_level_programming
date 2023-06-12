#include "lists.h"
/**
 * is_palindrome - the function that checks a singly linked list
 * @head: the head of the linked list
 *
 * Return: 0 if is nt, else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *tmp, *prv;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	fast = *head;
	slow = *head;
	tmp = slow;
	prv = NULL;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		tmp->next = prv;
		prv  = tmp;
		tmp = slow;
	}
	if (fast != NULL)
		slow = slow->next;
	while (prv && slow)
	{
		if (prv->next != slow->next)
			return (0);

		prv = prv->next;
		slow = slow->next;
	}
	return (1);
}
