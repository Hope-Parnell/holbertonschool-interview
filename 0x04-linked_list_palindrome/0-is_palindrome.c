#include "lists.h"

/**
 * checkPalindrome - uses recursion to check if list is a palindrome
 * @left: address of left node(will be updated as recursion resolves)
 * @right: right node
 *
 * Return: 1 if palindrome otherwise 0
 */
int checkPalindrome(listint_t **left, listint_t *right)
{
	int result;

	if (!right)
		return (1);
	result = checkPalindrome(left, right->next) && ((*left)->n == right->n);
	(*left) = (*left)->next;
	return (result);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: address of the head node
 *
 * Return: 1 if palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	return (checkPalindrome(head, *head));
}
