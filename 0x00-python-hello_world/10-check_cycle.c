#include "lists.h"

/**
 * check_cycle - Verify if a Linked List contains a Cycle
 * @list: The Linked List to Check from
 * Return: 1 if it has and 0 if no cycle exist
 */
int check_cycle(listint_t *list)
{
	listint_t *fst = list;
	listint_t *slw = list;

	if (!list)
		return (0);
	while (fst && slw && fst->next)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
			return (1);
	}
	return (0);
}
