/**
 * This program accepts a list of permisions for linux and returns the numeric value for each permisson.
 *
 * Task #2
 * @author Bryan Guzman
 * @date 02/25/18
 * ID 001265918
 */

#include <stdio.h>
#include <stdlib.h>
#define NUMBER_COUNT_MAX 10

size_t read_numbers(char numbers[], size_t n) {
    unsigned int i = 0;

    /* note that in Linux you can signal end of file/stream by key combination ctrl-d */
    /*The while loop reads all of the inputs and makes sure that the number of inputs stays within the bounds of the array. It will continue to read
    inputs until there are no more inputs left to read or the program reaches the end of the file*/
    while (i < n && scanf("%s\n", &numbers[i]) != EOF) {
        i++;
    }

    return i;
}

int main(int argc, char *argv[]) {
    char numbers[NUMBER_COUNT_MAX];
    size_t numberlen;
    char read = 'r', write = 'w', execute = 'x', dash = '-';
    int own = 0, gro = 0, use = 0;

    numberlen = read_numbers(numbers,NUMBER_COUNT_MAX);

    if(numberlen == 0){
        printf("invalid permission\n");
        exit(42);
    }

    /*Take the inputted array and separate it into three smaller arrays and add up the totals from each array
    whole thing would be much simpler as a switch case*/
    for(int i = 0; i < 9; i++){
        //Owner
        if(i >= 0 && i <= 2){
            if(i == 0){
                if(numbers[0] == read){
                    own += 4;
                }
                else if(numbers[0] == dash){
                    own += 0;
                } 
                else if(numbers[0] != read && numbers[0] != dash){
                    printf("invalid permission\n");
                    exit(42);
                }
            }
            if(i == 1){
                if(numbers[1] == write){
                    own += 2;                
                }
                else if(numbers[1] == dash){
                    own += 0;
                }
                else if(numbers[1] != write && numbers[1] != dash){
                    printf("invalid permission\n");
                    exit(42);
                }
            }
            if(i == 2){
                if(numbers[2] == execute){
                    own += 1;
                }
                else if(numbers[2] == dash){
                    own += 0;
                }
                else if(numbers[2] != execute && numbers[2] != dash){
                    printf("invalid permission\n");
                    exit(42);
                }
            }
        }
        //Group
        if(i >= 3 && i <= 5){
            if(i == 3){
                if(numbers[3] == read){
                    gro += 4;
                }
                else if(numbers[3] == dash){
                    gro += 0;
                }
                else if(numbers[3] != read && numbers[3] != dash){
                    printf("invalid permission\n");
                    exit(42);
                }
            }
            if(i == 4){
                if(numbers[4] == write){
                    gro += 2;
                }
                else if(numbers[4] == dash){
                    gro += 0;
                }
                else if(numbers[4] != write && numbers[4] != dash){
                    printf("invalid permission\n");
                    exit(42);
                }
            }
            if(i == 5){
                if(numbers[5] == execute){
                    gro += 1;
                }
                else if(numbers[5] == dash){
                    gro += 0;
                }
                else if(numbers[5] != execute && numbers[5] != dash){
                    printf("invalid permission\n");
                    exit(42);
                }
            }
        }
        //User
        if(i >= 6 && i <= 8){
            if(i == 6){
                if(numbers[6] == read){
                    use += 4;
                }
                else if(numbers[6] == dash){
                    use += 0;
                }
                else if(numbers[6] != read && numbers[6] != dash){
                    printf("invalid permission\n");
                    exit(42);
                }
            }
            if(i == 7){
                if(numbers[7] == write){
                    use += 2;
                }
                else if(numbers[7] == dash){
                    use += 0;
                }
                else if(numbers[7] != write && numbers[7] != dash){
                    printf("invalid permission\n");
                    exit(42);
                }
            }
            if(i == 8){
                if(numbers[8] == execute){
                    use += 1;
                }
                else if(numbers[8] == dash){
                    use += 0;
                }
                else if(numbers[8] != execute && numbers[8] != dash){
                    printf("invalid permission\n");
                    exit(42);
                }
            }
        }
    }
    //Print out the final values here
    printf("%d%d%d\n", own, gro, use);
    return 0;
}
