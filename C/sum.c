/**
*This program will accept command line arguements (ints), add them together and return the sum.
*If no arguments are provided for the program it will return "No input numbers"
*
*@author Bryan Guzman
*@version 1.0
*System Programming: HW05-Task1
*March 3, 2018
*ID: 001265918
**/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[]){
	int *numInput, num, sum = 0;
	char dash = '-';

	//Check to make sure that number arugments were provided
	if(argc <= 1){
		printf("no input numbers");
		return 0;
	}

	//For loop to extract arguements stored in argv and convert them to ints
	for(int i = 1; argv[i] != '\0'; i++){
		if(isdigit(*argv[i]) || *argv[i] == dash){
			sscanf(argv[i], "%d", &num);
			sum += num;

		}
		else{
			printf("Element %d, %d is not a number\n", i, num);
			return 0;
		}
	}

	printf("%d\n", sum);
	return 0;
}