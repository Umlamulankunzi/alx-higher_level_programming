#include <stdio.h>
#include "lists.h"


/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: pointer to head of linked list
* Return: 1 if list is palindrome Else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *first_head = *head;
	listint_t *curr = *head;
	int size_list = len_list(*head);
	int index = 1, sec_head_index, mid_lst = size_list / 2;
	int result;

	sec_head_index = (size_list % 2 == 0) ? mid_lst + 1 : mid_lst + 2;

	while (index != sec_head_index)
	{
		curr = curr->next;
		index += 1;
	}

	reverse_list(&curr);

	result = compare_lists(first_head, curr);
	reverse_list(&curr);
	return (result);

}


/**
* compare_lists - compares values of a linked list
* @f_head: pointer to head of first linked list
* @s_head: pointer to head of second linked list
* Return: 1 if lists equal Else 0
*/
int compare_lists(listint_t *f_head, listint_t *s_head)
{
	while (s_head != NULL)
	{
		if (s_head->n != f_head->n)
			return (0);

		s_head = s_head->next;
		f_head = f_head->next;
	}
	return (1);
}


/**
* len_list - find size of a singly linked list.
* @head: pointer to head of linked list
* Return: int
*/
int len_list(listint_t *head)
{
	if (head)
		return (1 + len_list(head->next));

	return (0);
}


/**
* reverse_list - reverese a singly linked list.
* @head: pointer to head of linked list
*
*/
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*head = prev;
}
