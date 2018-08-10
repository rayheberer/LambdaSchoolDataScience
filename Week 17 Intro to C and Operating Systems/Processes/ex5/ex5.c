// Write a program that forks a child and creates a shared pipe
// between the parent and child processes. Have the child write 
// the three messages to the parent and have the parent print out 
// the messages. 

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

#define MSGSIZE 16

char* msg1 = "hello world #1";
char* msg2 = "hello world #2";
char* msg3 = "hello world #3";

int main(void)
{
    int p[2];
    if (pipe(p) < 0) {
        fprintf(stderr, "pipe failed\n");
        exit(1);
    }

    int rc = fork();
    if (rc < 0) {    // fork failed; exit
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {    // child process
        // write messages
        write(p[1], msg1, MSGSIZE);
        write(p[1], msg2, MSGSIZE);
        write(p[1], msg3, MSGSIZE);
        close(p[1]);

        exit(0);
    } else {
        int wc = waitpid(rc, NULL, 0);

        char msg1[MSGSIZE], msg2[MSGSIZE], msg3[MSGSIZE];
        
        read(p[0], msg1, MSGSIZE);
        printf("message 1: %s\n", msg1);
        read(p[0], msg2, MSGSIZE);
        printf("message 2: %s\n", msg2);
        read(p[0], msg3, MSGSIZE);
        printf("message 3: %s\n", msg3);
        close(p[0]);
    }


    return 0;
}
