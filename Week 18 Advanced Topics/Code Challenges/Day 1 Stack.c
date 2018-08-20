/*
Implement a stack data structure. You're provided with a struct representing the Stack, the createStack method, and a main function. Note how the createStack function allocates memory in order to initialize a new stack structure. 

Implement the methods isFull, isEmpty,  push, and pop. 

When the stack reaches its capacity, have it double in capacity so as to be able to accommodate additional inputs. Look into the realloc method as a possible way to do this. 
*/

#include <stdio.h>
#include <stdlib.h>

// Struct representing a Stack that holds an integer representing the 
// the index of the top of the stack, the total capacity that the stack
// can hold, and a pointer to an array of integers
typedef struct Stack {
  int top;
  unsigned int capacity;
  int* data;
} Stack;
 
// Function to create a stack of given capacity. It initializes size of
// stack as 0
Stack* createStack(unsigned int capacity)
{
    Stack* stack = malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->data = malloc(capacity * sizeof(int));
      
    return stack;
}

int isFull(Stack* stack)
{
    if (stack->top == stack->capacity - 1) {
        return 1;
    } else {
        return 0;
    }
}
 
int isEmpty(Stack* stack)
{
    if (stack->top == -1) {
        return 1;
    } else {
        return 0;
    }
}

void push(Stack* stack, int item)
{
    if (isFull(stack)) {
        stack->capacity *= 2;
        stack->data = realloc(stack->data, stack->capacity * sizeof(int));
    }
    stack->top++;
    stack->data[stack->top] = item;
}
 
int pop(Stack* stack)
{
    if (isEmpty(stack)) {
        return -1;
    }
    int value = stack->data[stack->top];
    stack->top--;
    return value;
}

// Program to test above functions
int main()
{
    Stack* stack = createStack(2);
  
    printf("stack is full: %d\n", isFull(stack));
    printf("stack is empty: %d\n", isEmpty(stack));
  
    push(stack, 10);
    printf("stack is empty: %d\n", isEmpty(stack));
    push(stack, 20);
  
    printf("stack is full: %d\n", isFull(stack));
  
    printf("%d popped from stack\n", pop(stack));
    printf("%d popped from stack\n", pop(stack));
    printf("%d popped from stack\n", pop(stack));
  
	const int push_count = 100000;

	printf("pushing %d things\n", push_count);
	for (int i = 0; i < push_count; i++) {
		push(stack, i);
	}

	printf("popping %d things\n", push_count);
	for (int i = push_count - 1; i >= 0; i--) {
		int v = pop(stack);

		if (v != i) {
			printf("Popped %d but expected %d\n", v, i);
		}
	}

  return 0;
}