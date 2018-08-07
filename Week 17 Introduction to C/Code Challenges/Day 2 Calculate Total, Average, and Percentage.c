/*
Write a C program that accepts exactly five floats from a user and calculates the total, average, and percentage of those five floats.  Imagine these floats are test scores out of 100 points each. 

When your program is executed, it should prompt the user to enter 5 floats. Once the user has done so, your program should receive those inputs and calculate the total, average, and percentage of those input floats.

Your program's output should look something like the following:

Example Input

    Enter 5 floats: 95.2 76.6 85.4 90.0 89.1

Output

  Total = 436.30
  Average = 87.26       // Total / 5.0
  Percentage = 87.26%   // (Total / 500.0) * 100

You all know about printf function for printing some output from a C program. Look up how to have a C program accept user input in response to a prompt. 
*/

#include <stdio.h>

int main()
{
  float n1, n2, n3, n4, n5;
  printf("Enter 5 floats:");
  scanf("%f %f %f %f %f", &n1, &n2, &n3, &n4, &n5);
  
  float total = n1 + n2 + n3 + n4 + n5;
  float average = total / 5.0;
  float percentage = (total / 500.0) * 100;
  printf("Total = %.2f\nAverage = %.2f\nPercentage = %.2f%%", 
  total, average, percentage);
  return 0;
}