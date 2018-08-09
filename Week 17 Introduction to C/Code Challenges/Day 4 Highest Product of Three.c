/*
Given an array of integers, write a function that finds the highest product of three from amongst any three integers in the array. You can assume any input arrays have at least three integers. 

You'll need to take into account the fact that it is possible for the highest product of three from a given array to be the product of two negative numbers and a positive number. 

For example, given the array [-90, -15, 6, 9, 10], the highest product of any three numbers from this array is -90 * -15 * 10 which yields 13,500.

Remember to start off by thinking through and coming up with an algorithm that will solve this problem regardless of what programming language you use. Once you have an algorithm, implement it.. 

The macros MAX, MIN, and SIZE have already been defined for you. Use them just like you would any other function.
*/

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define MAX(a, b) (((a) > (b)) ? (a) : (b))
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define SIZE(arr) (sizeof(arr) / sizeof(arr[0]))

int highestProductOf3(int arr[], int length)
{
  // in any array, it will either be the 3 largest
  // or the largest, and the 2 smallest
  // so we can just check both cases
  
  int top1 = 0;
  int top2 = 0;
  int top3 = 0;
  int bottom1 = 0;
  int bottom2 = 0;
  
  for (int i = 0; i < length; i++) {
      if (arr[i] > top1) {
          top3 = top2;
          top2 = top1;
          top1 = arr[i];
      } else if (arr[i] > top2) {
          top3 = top2;
          top2 = arr[i];
      } else if (arr[i] > top3) {
          top3 = arr[i];
      } else if (arr[i] < bottom1) {
          bottom2 = bottom1;
          bottom1 = arr[i];
      } else if (arr[i] < bottom2) {
          bottom2 = arr[i];
      }
  }
  
  return MAX(top1*top2*top3, top1*bottom1*bottom2);
}

int main(int argc, char* argv)
{
  int arr1[] = {-10, -10, 1, 3, 2};
  int arr2[] = {1, 10, -5, 1, -100};
  int arr3[] = {5, -20, 19, 16, 4};
  
  printf("Highest product of arr1 is: %d\n", highestProductOf3(arr1, SIZE(arr1)));
  printf("Highest product of arr2 is: %d\n", highestProductOf3(arr2, SIZE(arr2)));
  printf("Highest product of arr3 is: %d\n", highestProductOf3(arr3, SIZE(arr3)));
  
  return 0;
}