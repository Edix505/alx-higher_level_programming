#include "lists.h"
#include <stdio.h>

void reverse(listint_t **h_r)
{
    listint_t *prv;
    listint_t *crr;
    listint_t *nxt;

    prv = NULL;
    crr = *h_r;

    while (crr != NULL)
    {
        nxt = crr->next;
        crr->next = prv;
        prv = crr;
        crr = nxt;
    }

    *h_r = prv;
}


int compare(listint_t *h1, listint_t *h2)
{
    listint_t *tmp1;
    listint_t *tmp2;

    tmp1 = h1;
    tmp2 = h2;

    while (tmp1 != NULL && tmp2 != NULL)
    {
        if (tmp1->n == tmp2->n)
        {
            tmp1 = tmp1->next;
            tmp2 = tmp2->next;
        }
        else
        {
            return (0);
        }
    }

    if (tmp1 == NULL && tmp2 == NULL)
    {
        return (1);
    }

    return (0);
}


int is_palindrome(listint_t **head)
{
  listint_t *nhead, *tort, *hare, *ptort;
  listint_t *cut = NULL, *half, *it1, *it2;

  if (!head || !*head)
    return (1);

  nhead = *head;
  if (nhead->next != NULL)
    {
      for (hare = nhead, tort = nhead; hare != NULL && hare->next != NULL;
	   ptort = tort, tort = tort->next)
	hare = hare->next->next;
      if (hare != NULL)
	{
	  cut = tort;
	  tort = tort->next;
	}
      ptort->next = NULL;
      half = tort;
      it1 = reverse_listint(&half);
      for (it2 = *head; it2; it1 = it1->next, it2 = it2->next)
	{
	  if (it2->n != it1->n)
	    return (0);
	}
      if (cut == NULL)
	ptort->next = half;
      else
	{
	  ptort->next = cut;
	  cut->next = half;
	}
    }

  return (1);
}
