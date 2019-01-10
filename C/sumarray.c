#include <stdio.h>
#include <stdlib.h>
#define NUMBER_COUNT_MAX 100

size_t read_numbers(int numbers[], size_t n) {
  unsigned int i = 0;

  /* note that in Linux you can signal end of file/stream by key combination ctrl-d */
  /*The while loop reads all of the inputs and makes sure that the number of inputs stays within the bounds of the array. It will continue to read
  inputs until there are no more inputs left to read or the program reaches the end of the file*/
  while (i < n && scanf("%d", &numbers[i]) != EOF) {
    i++;
  }

  return i;
}

int main(int argc, char *argv[]) {
  int numbers[NUMBER_COUNT_MAX];
  size_t numberlen;
  int i, sum;

  numberlen = read_numbers(numbers, NUMBER_COUNT_MAX);
  for (sum = 0, i = 0; i < numberlen; sum += numbers[i], i++);
  printf("read %d integers, total: %d\n", numberlen, sum);

  return 0;
}
