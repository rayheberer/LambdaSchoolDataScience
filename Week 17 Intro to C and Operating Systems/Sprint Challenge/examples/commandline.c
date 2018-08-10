/**
 * Try running with various command line args:
 *
 * ./commandline hello world
 * ./commandline this is a test
 * ./commandline
 */

#include <stdio.h>

int main(int argc, char **argv)
{
    int i;

    printf("There are %d command line argument(s):\n", argc);

    for (i = 0; i < argc; i++) {
        printf("   %s\n", argv[i]);
    }

    return 0;
}