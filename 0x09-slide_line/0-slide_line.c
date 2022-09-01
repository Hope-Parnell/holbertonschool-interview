#include "slide_line.h"
#include <stdio.h>
/**
 * slideLeft - slides a line to the left
 * @line: line to slide
 * @size: length of the line
 */
void slideLeft(int *line, int size)
{
	int seek, firstZero = -1, end = size - 1, i;

	/*move 0s to the right*/
	for (seek = 0; seek < size; seek++)
	{
		if (line[seek] == 0)
		{
			if (firstZero == -1)
				firstZero = seek;
			end = firstZero;
			while (line[seek] == 0 && seek < size)
				seek++;
			if (seek < size)
			{
				line[firstZero++] = line[seek];
				line[seek] = 0;
			}
		}
	}
	for (seek = 0; seek < end; seek++)
	{
		if (line[seek] == line[seek + 1])
		{
			line[seek] *= 2;
			for (i = seek + 1; i < end; i++)
				line[i] = line[i + 1];
			line[end--] = 0;
		}
	}
}
/**
 * slideRight - slides a line to the right
 * @line: line to slide
 * @size: length of the line
 */
void slideRight(int *line, int size)
{
	int seek, firstZero = -1, end = 0, i;

	/*move 0s to the left*/
	for (seek = size - 1; seek >= 0; seek--)
	{
		if (line[seek] == 0)
		{
			if (firstZero == -1)
				firstZero = seek;
			end = firstZero;
			while (line[seek] == 0 && seek >= 0)
				seek--;
			if (seek >= 0)
			{
				line[firstZero--] = line[seek];
				line[seek] = 0;
			}
		}
	}
	for (seek = size - 1; seek > end; seek--)
	{
		if (line[seek] == line[seek - 1])
		{
			line[seek] *= 2;
			for (i = seek - 1; i > end; i--)
				line[i] = line[i - 1];
			line[end++] = 0;
		}
	}
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
	if (direction != SLIDE_LEFT && direction != SLIDE_RIGHT)
		return (CANNOT_SLIDE);
	if (direction == SLIDE_LEFT)
		slideLeft(line, size);
	else
		slideRight(line, size);
	return (DONE);
}
