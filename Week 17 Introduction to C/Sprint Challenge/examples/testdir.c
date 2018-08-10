// gcc -Wall -Wextra -o testdir testdir.c

#include <stdio.h>
#include <dirent.h>

/**
 * Main
 */
int main(void)
{
  DIR *d = opendir(".");
  printf("Testing: %s\n", d == NULL? "FAIL": "PASS");
  closedir(d);

  return 0;
}