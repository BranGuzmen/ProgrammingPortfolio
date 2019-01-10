/**
 * This program accepts a list of permisions for linux and returns the numeric value for each permisson.
 *
 * Task #3
 * @author Bryan Guzman
 * @date 02/25/18
 * ID 001265918
 */

#include <stdio.h>
#include <stdlib.h>
#include "permarray.c"
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
    int index; //Will be used to store the index outputted by permute_array()
    size_t numberlen;

    numberlen = read_numbers(numbers, NUMBER_COUNT_MAX);
    index = permute_array(numbers, numberlen);
    insertionSort(numbers, numberlen, index);
    printf("\n%zu\n", numberlen);
    printArray(numbers);

    return 0;
}