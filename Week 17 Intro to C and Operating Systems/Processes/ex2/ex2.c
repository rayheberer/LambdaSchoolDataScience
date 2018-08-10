// Write a program that opens the text.txt  file (with the `fopen()` system call) located in this directory 
// and then calls `fork()` to create a new process. Can both the child and parent access the file descriptor 
// returned by `fopen()`? What happens when they are written to the file concurrently?

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(void)
{
    FILE * file;
    file = fopen("text.txt", "w");

    if (file == NULL) {
        printf("no such file");
        return 0;
    }

    int rc = fork();
    if (rc < 0) {    // fork failed; exit
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {    // child process
        fputs("hello from child\n", file);
        fclose(file);
    } else {
        fputs("hello from parent\n", file);
        fclose(file);
    }
    
    return 0;
}

/* Both the parent and child processes can access the file. If they are both written to the file, then whichever process runs second
has its write content written to the file directly after that which was written by the first process. */