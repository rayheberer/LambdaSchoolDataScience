#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <errno.h>

#include <sys/stat.h>

/**
 * Main
 */
int main(int argc, char **argv)
{
    // Parse command line
    char path[64];
    if (argc > 1) {
        strcpy(path, argv[1]);
    } else {
        strcpy(path, ".");
    }

    // Open directory
    DIR *d = opendir(path);

    // setup file size holder
    struct stat buf;
    char file[128];
    

    if (d) {
        // Repeatly read and print entries
        struct dirent *ent = readdir(d);

        while (ent != NULL) {
            strcpy(file, path);
            strcat(file, "/");
            strcat(file, ent->d_name);
            stat(file, &buf);

            if (((buf.st_mode & S_IFREG) == 0) && 
                    ((buf.st_mode & S_IFDIR) != 0)) {
                printf("%10s\t", "<DIR>");
            } else {
                printf("%10ld\t", buf.st_size);
            }

            printf("%s\n", ent->d_name);
            ent = readdir(d);
        }
        // Close directory
        closedir(d);
    } else if (ENOENT == errno) {
        // Directory does not exist.
        printf("No such directory.\n");
        exit(1);
    }

    return 0;
}