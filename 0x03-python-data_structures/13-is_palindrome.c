#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * reverse - reverses a linked list
 * @head: double pointer to head node
 * Return: pointer to first node of reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp, *second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;

	second_half = slow;
	temp = reverse(&second_half);
	second_half = temp;

	while (*head && second_half)
	{
		if ((*head)->n == second_half->n)
		{
			*head = (*head)->next;
			second_half = second_half->next;
		}
		else
			return (0);
	}

	return (1);
}
