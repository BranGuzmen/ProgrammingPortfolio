/**
 * HOME06 - TASK02
 *
 * This program will act like the ls -al command provided by GNU/Linux. The program will accept a
 * command line argument and prints all the details of all files.
 *  Specifics:
 *      -Arguments provided will either be a file name or directory name. If the argument provided is
 *      a directory name all of the files within it will be listed. If it is a filename only the corresponding
 *      file will be printed
 *      -'.' and '..' should also be accepted by the program and print out
 *
 * @author Bryan Guzman
 * @version 1.0
 * @date April 5th, 2018
 * Student ID 001265918
 */
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <time.h>
#include <pwd.h>
#include <grp.h>

int listDirectory(const char *directoryName);
long totalBlock(const char *directoryName);

int listDirectory(const char *directoryName){
    struct dirent* cDir; //Current directory
    struct stat stats;
    struct tm lt;
    struct passwd *userID;
    struct group *grp;
    long total = totalBlock(directoryName);

    DIR* directory = opendir(directoryName);

    //Check for improperly initialized directory
    if(directory == NULL){
        fprintf(stderr, "list_dir : %s : %s\n",directoryName, strerror(errno));
        exit(EXIT_FAILURE);
    }

    fprintf(stdout,"%s:\ntotal %ld\n", directoryName, total);

    while((cDir = readdir(directory))){
        char buff[1024];
        errno = 0;
        snprintf(buff, sizeof buff, "%s/%s", directoryName, cDir->d_name);
        //Get owner name
        if((stat(buff, &stats)) == 0) {
            userID = getpwuid(stats.st_uid);
            grp = getgrgid(stats.st_gid);
            total += stats.st_blocks;
        }
        else{
            fprintf(stderr, "%s: %s\n", buff, strerror(errno));
            exit(EXIT_FAILURE);
        }


        //Get the time the file/directory was last modified
        time_t time1 = stats.st_mtime;
        localtime_r(&time1, &lt);
        char timeBuff[80];
        strftime(timeBuff, sizeof(timeBuff), "%c", &lt);


        if(userID != 0){
            fprintf(stdout, (S_ISDIR(stats.st_mode)) ? "d" : "-");
            fprintf(stdout, (stats.st_mode & S_IRUSR) ? "r" : "-");
            fprintf(stdout, (stats.st_mode & S_IWUSR) ? "w" : "-");
            fprintf(stdout, (stats.st_mode & S_IXUSR) ? "x" : "-");
            fprintf(stdout, (stats.st_mode & S_IRGRP) ? "r" : "-");
            fprintf(stdout, (stats.st_mode & S_IWGRP) ? "w" : "-");
            fprintf(stdout, (stats.st_mode & S_IXGRP) ? "x" : "-");
            fprintf(stdout, (stats.st_mode & S_IROTH) ? "r" : "-");
            fprintf(stdout, (stats.st_mode & S_IWOTH) ? "w" : "-");
            fprintf(stdout, (stats.st_mode & S_IXOTH) ? "x" : "-");

            fprintf(stdout, "%4d %2s %4s %5ld %2s %2s\n", stats.st_nlink, userID->pw_name, grp->gr_name,(long)stats.st_size, timeBuff, cDir->d_name);
        }
        else{
            fprintf(stdout, (S_ISDIR(stats.st_mode)) ? "d" : "-");
            fprintf(stdout, (stats.st_mode & S_IRUSR) ? "r" : "-");
            fprintf(stdout, (stats.st_mode & S_IWUSR) ? "w" : "-");
            fprintf(stdout, (stats.st_mode & S_IXUSR) ? "x" : "-");
            fprintf(stdout, (stats.st_mode & S_IRGRP) ? "r" : "-");
            fprintf(stdout, (stats.st_mode & S_IWGRP) ? "w" : "-");
            fprintf(stdout, (stats.st_mode & S_IXGRP) ? "x" : "-");
            fprintf(stdout, (stats.st_mode & S_IROTH) ? "r" : "-");
            fprintf(stdout, (stats.st_mode & S_IWOTH) ? "w" : "-");
            fprintf(stdout, (stats.st_mode & S_IXOTH) ? "x" : "-");

            fprintf(stdout, "%d %d \t %d \t %ld \t %s \t %s\n", stats.st_nlink,stats.st_uid, stats.st_gid, (long)stats.st_size, timeBuff, cDir->d_name);
        }
    }

    closedir(directory);
    fprintf(stdout, "\n");
    return 0;
}

//Just used to calculate the total block
long totalBlock(const char *directoryName) {
    struct dirent *cDir; //Current directory
    struct stat stats;
    long total = 0;

    DIR *directory = opendir(directoryName);

    //Check for improperly initialized directory
    if (directory == NULL) {
        fprintf(stderr, "list_dir : %s : %s\n", directoryName, strerror(errno));
        exit(EXIT_FAILURE);
    }

    while ((cDir = readdir(directory))) {
        char buff[1024];
        errno = 0;
        snprintf(buff, sizeof buff, "%s/%s", directoryName, cDir->d_name);
        //Get owner name
        if ((stat(buff, &stats)) == 0) {
            total += stats.st_blocks;
        } else {
            fprintf(stderr, "%s: %s\n", buff, strerror(errno));
            exit(EXIT_FAILURE);
        }
    }
    closedir(directory);
    return total;
}

int main(int argc, char* argv[]){

    if(argc == 1){
        return listDirectory(".");
    }
    else{
        int a = 0;
        for(int i = 1; i < argc; i++){
            if(listDirectory(argv[i]) != 0){
                a = 1;
            }
        }
        return a;
    }
}

