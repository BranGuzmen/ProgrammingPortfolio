/**
* HOMEWORK06 - TASK01
*
* filegrep is a simplified version of grep. The output of running the program will replicate that of grep -n PATTERN FILE along with line numbers of
* where the pattern occured.
*
* The arguments provided to the program follow this convention:
*	filegrep PATTERN FILE
*
* If more or less than two arguments are provided an error will be thrown. If an invalid FILE is provided an error will also be thrown following the
* convention given by grep.
*
* @author Bryan Guzman
* @version 1.0
* Student ID: 001265918
* April 1, 2018
**/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 256

int main(int argc, char *argv[]){
    char fileLine[MAX_LENGTH];
	//Check to make sure the correct amount of arguments are provided
	if(argc > 3 || argc < 3){//3 because of the filename counting as an argument
		fprintf(stderr,"Usage: filegrep PATTERN FILE\n");
        exit(2);
	}
    //Assign arguments to variables for clarity
    char *pattern = argv[1];
    char *file = argv[2];

    FILE *grepFile;

    //If the file name doesn't exist or it can't be opened for reading
    if((grepFile = fopen(file,"r")) == NULL){
        fprintf(stderr, "grep: %s: No such file or directory\n", file);
        exit(3);
    }

    //Go through the file looking for the pattern and read a line the sizeof MAX_LENGTH
    int line = 1;//line count
    while(!feof(grepFile) && (fgets(fileLine, sizeof(fileLine), grepFile)) != NULL){
        //strstr returns NULL if pattern is not present in line
        if(strstr(fileLine,pattern) != NULL){
            fprintf(stdout,"%d:\t%s",line,fileLine);
        }
        line++;//Increment line count
    }

    fclose(grepFile);
    return 0;
}