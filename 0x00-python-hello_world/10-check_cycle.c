#include <stdlib.h>
#include "lists.h"


/**
* check_cycle - checks if linked list @list has cycle
* @list: pointer to head of linked list
* Return: 1 if true Else 0
*/
int check_cycle(listint_t *list)
{
	listint_t *slowpoke = list;
	listint_t *speedster = list;

	while (speedster != NULL && speedster->next != NULL)
	{
		slowpoke = slowpoke->next;
		speedster = speedster->next->next;

		if (slowpoke == speedster)
		return (1);
	}

	return (0);
}
