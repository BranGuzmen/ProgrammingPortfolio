/**
 * This program accepts a list of number and returns the lowest value.
 *
 * Task #1
 * @author Bryan Guzman
 * @date 02/25/18
 * ID 001265918
 */

#include <stdio.h>
#include <stdlib.h>
#define NUMBER_COUNT_MAX 100

size_t read_numbers(int numbers[], size_t n) {
    unsigned int i = 0;

    /* note that in Linux you can signal end of file/stream by key combination ctrl-d */
    /*The while loop reads all of the inputs and makes sure that the number of inputs stays within the bounds of the array. It will continue to read
    inputs until there are no more inputs left to read or the program reaches the end of the file*/
    while (i < n && scanf("%d\n", &numbers[i]) != EOF) {
        i++;
    }

    return i;
}

int main(int argc, char *argv[]) {
    int numbers[NUMBER_COUNT_MAX];
    size_t numberlen;
    int i, key, j;

    numberlen = read_numbers(numbers, NUMBER_COUNT_MAX);
    //If read_numbers returns a 0 it means that nothing was inputted which is caught here
    if(numberlen == 0){
        printf("no input numbers\n");
        exit(42);
    }
    //Sort the numbers inputted using insertion sort algorithm 
    for (i = 1; i < numberlen; i++){
        key = numbers[i];
        j = i-1;

        while(j>=0 && numbers[j] > key){
            numbers[j+1] = numbers[j];
            j= j-1;
        }
        numbers[j+1] = key;
    }

    //Print out the first element of the sorted array since it will always be the lowest number
    printf("%d\n", numbers[0]);
    return 0;
}
