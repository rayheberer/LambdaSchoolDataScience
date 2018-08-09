// Write a program that calls `fork()` and then calls some form of `exec()`
// to run the program `/bin/ls`. Try a few variants of `exec()`, such as 
// `execl()`, `execle()`, `execv()`, and others. Why do you think there 
// are so many variants of the same basic call?

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(void)
{
    int rc = fork();
    if (rc < 0) {    // fork failed; exit
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {    // child process
        execl("/bin/ls", "/bin/ls", "-l", NULL);
    } else {
        int wc = waitpid(rc, NULL, 0);
    }

    return 0;
}

/* The different variants are useful depending on how much one knows in advance about the sort of arguments
that are going to be passed to the process being executed. The other factor that matters is whether the name
of the file to be executed is known, or the path to it. */