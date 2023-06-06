#include <stdlib.h>
#include "lists.h"


/**
* insert_node - inserts node in ordered linked list
* @head: pointer to pointer to head of singly linked list
* @number: value of node to insert
*
* Return: pointer to inserted node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *node = malloc(sizeof(*node));

	if (node == NULL)
		return (NULL);

	node->n = number;

	if (curr == NULL)
	{
		*head = node;
		node->next = NULL;
		return (node);
	}

	while (curr)
	{
		if (number <= curr->n)
		{
			if (prev == NULL)
			{
				node->next = curr;
				*head = node;
				return (node);
			}
			else
			{
				prev->next = node;
				node->next = curr;
				return (node);
			}
		}
		prev = curr;
		curr = curr->next;
	}
	prev->next = node;
	node->next = NULL;
	return (node);

}
