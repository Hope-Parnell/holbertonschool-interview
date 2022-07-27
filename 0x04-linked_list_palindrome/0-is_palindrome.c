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

	/*at end of list*/
	if (!right)
		return (1);
	/**
	 * if the contents of left and the contents of right are ever not equal,
	 * result will always be 0
	 */
	result = checkPalindrome(left, right->next) && ((*left)->n == right->n);
	/*update the address stored in left*/
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
