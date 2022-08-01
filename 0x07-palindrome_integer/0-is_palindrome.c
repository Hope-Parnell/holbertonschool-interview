#include "palindrome.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a unsined long int is a palindrome
 * @n: number to be checked
 *
 * Return: 1 if palindrome, otherwise 0
 */
int is_palindrome(unsigned long n)
{
	unsigned long reverse = 0, temp;

	for (temp = n; temp != 0; temp /= 10)
		reverse = (reverse * 10) + (temp % 10);
	return (reverse == n ? 1 : 0);
}
