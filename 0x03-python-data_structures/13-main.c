#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

     
int main(void)
{
  listint_t *head;

  head = NULL;
  add_nodeint_end(&head, 1);
  add_nodeint_end(&head, 17);
  add_nodeint_end(&head, 972);
  add_nodeint_end(&head, 50);
  add_nodeint_end(&head, 98);
  add_nodeint_end(&head, 98);
  add_nodeint_end(&head, 50);
  add_nodeint_end(&head, 972);
  add_nodeint_end(&head, 17);
  add_nodeint_end(&head, 1);
  print_listint(head);

  if (is_palindrome(&head) == 1)
    printf("list is a palindrome\n");
  else
    printf("list is not a palindrome\n");

  free_listint(head);

  return (0);
}
