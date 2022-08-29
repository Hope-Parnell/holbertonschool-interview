#include "slide_line.h"
#include <stdio.h>
/**
 * merge - merges a line
 * @line: line to merge
 * @start: index to start the merge
 * @end: index to end the merge
 * @d: direction to merge
 */
void merge(int *line, int start, int end, int d)
{
	int i;

	line[start - d] += line[start];
	for (i = start; i != end; i += d)
		line[i] = line[i + d];
	line[i] = 0;
}
/**
 * slide_line - slides a 2048 line left or right
 * @line: line to slide
 * @size: length of the line
 * @direction: direction to slide
 *
 * Return: 1 on success, 0 on failure
 */
int slide_line(int *line, size_t size, int direction)
{
	int start = direction == SLIDE_LEFT ? size - 1 : 0;
	int end = direction == SLIDE_LEFT ? 0 : size - 1;
	int i;

	if (direction != SLIDE_LEFT && direction != SLIDE_RIGHT)
		return (CANNOT_SLIDE);
	for (i = start; i != end; i += direction)
	{
		while (line[i + direction] == 0)
		{
			merge(line, i, start, -direction);
			i--;
		}
		if (line[i] == line[i + direction])
		{
			merge(line, i, start, -direction);
			i += direction;
			if (i == end)
				break;
		}
		while (line[i + direction] == 0)
		{
			merge(line, i, start, -direction);
			i--;
		}
	}
	return (DONE);
}
