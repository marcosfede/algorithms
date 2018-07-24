#include <stdio.h>
#include <stdlib.h>

#define FALSE 0
#define TRUE !FALSE

#define NODES_COUNT 250
#define NODE_TO_LOOP NODES_COUNT / 2
#define MAX_PRINTS NODES_COUNT * 2

/* Kinda obfuscated, yeah... */
/**
    How to find if there is a loop on a linked list.
    Time: O(n)
    Space: O(1)
*/

typedef struct _node * list;
typedef struct _node {
    int id;
    list next;
} node;

int loop_check(list);
void print_list(list);

int main()
{
    int i;
    node nodes[NODES_COUNT];
    list l;

    for (i = 0; i < NODES_COUNT - 1; i++) {
        nodes[i].id = i;
        nodes[i].next = &nodes[i + 1];
    }
    nodes[NODES_COUNT - 1].id = NODES_COUNT - 1;
    nodes[NODES_COUNT - 1].next = NULL;
    l = nodes;

    print_list(l);
    if (loop_check(l)) {
        printf("It loops!\n");
    }
    else {
        printf("It does not loop!\n");
    }

    nodes[NODES_COUNT - 1].next = &nodes[NODE_TO_LOOP];

    print_list(l);
    if (loop_check(l)) {
        printf("It loops!\n");
    }
    else {
        printf("It does not loop!\n");
    }

    return 0;
}

int loop_check(list l) {
    list turtle = l;
    while (l != NULL) {
        turtle = turtle->next;
        l = l->next;
        if (l != NULL) {
            l = l->next;
            if (turtle == l) {
                return TRUE;
            }
        }
        else {
            return FALSE;
        }
    }
    return FALSE;
}

void print_list(list l) {
    int count;
    for (count = 0; count < MAX_PRINTS && l != NULL; count++) {
        printf("%d ", l->id);
        l = l->next;
    }
    printf("\n");
}
