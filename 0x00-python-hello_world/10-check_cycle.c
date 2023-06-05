#include <stdlib.h>
#include "list.h"


/**
* check_cycle - checks if linked list @list has cycle
* @list: pointer to head of linked list
* Return: 1 if true Else 0
*/ 
int check_cycle(listint_t *list)
{
	Node* slow = head;
	Node* fast = head;

	while (fast != NULL && fast->next != NULL)
	{
	       slow = slow->next;
	       fast = fast->next->next;
	       
	       if (slow == fast)
	       	return (1);
	}

	return (0);
}