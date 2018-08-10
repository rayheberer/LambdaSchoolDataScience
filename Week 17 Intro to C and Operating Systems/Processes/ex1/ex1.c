// Write a program that calls `fork()`. Before calling `fork()`, have the main process access a variable
// (e.g., x) and set its value to something (e.g., 100). What value is the variable in the child process?
// What happens to the variable when both the child and parent change the value of x?

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
    // initialize variable
    int x = 100;

    int rc = fork();
    if (rc < 0) {    // fork failed; exit
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {    // child process
        printf("child process here, variable value: %d\n", x);
        x = 50;
    } else {
        printf("parent process here, variable value: %d\n", x);
        x = 200;
    }
    
    printf("final variable value: %d\n", x);
    return 0;
}

/* The variable value is 100 in the child process. 
If the variable value is changed in the parent process, this does not affect its value in the child process and vice versa.