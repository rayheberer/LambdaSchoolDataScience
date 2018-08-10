/*
Write a program that reads an integer from stdin and uses that integer N to calculate the Nth Fibonacci number. Your program should print out your answer in the form of "Nth Fibonacci number is [YOUR ANSWER]".

Your program should prompt the user with "Enter an integer:".
*/

#include <stdio.h>
#include <assert.h>

int fibonacci_rec(int n) {
    if (n == 0) {
        return 0;
    }
    if (n == 1 || n == 2) {
        return 1;
    }
    
    return fibonacci_rec(n-1) + fibonacci_rec(n-2);
}

long int fibonacci_iter(int n) {
    if (n < 2) {
        return n;
    }
    
    long int n0, n1, n2;
    
    n0 = 0;
    n1 = 1;
    
    for (int i = 1; i < n; i++) {
        n2 = n0 + n1;
        n0 = n1;
        n1 = n2;
    }
    return n2;
}

int main(int argc, char* argv[])
{
  printf("Enter an integer:");
  
  int n;
  scanf("%d", &n);
  long int fib_number = fibonacci_iter(n);
  printf("Nth  Fibonacci number is %d", fib_number);
  return 0;
}