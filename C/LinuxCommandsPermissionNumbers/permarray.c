#include <stdio.h>
#include <stdlib.h>

int permute_array(int* arr, size_t len){
	int temp,temp2,zero, f = 0;
	int *tempArr[len + 1];

	for(int c = 0; c < len; c++){
		//If the element is less than zero go into this while loop to shift elements of array 1 to the right
		if(arr[c] <= 0){
			temp = arr[c];
			for(int i = 0; i < len; i++){
				//Will skip over index that has element <= 0
				if(i == c){
					continue;
				}
				else{
					tempArr[i+1] = &arr[i];
				}
				
			}
			tempArr[f] = &temp;
			zero = f; //Will store the last index of number <= 0    
			f++;             
		}
	}
	//Shift elements from tempArr to main arr
	for(int y = 0; y < len; y++){
		arr[y] = *tempArr[y];
	}

	return zero;
}

void insertionSort(int *arr, size_t len, int zero){
	int i, key, j;

	for(i = zero + 1; i < len; i++){
		key = arr[i];
		j = i-1;

		while(j >= 0 && arr[j] > key){
			arr[j+1] = arr[j];
			j = j-1;
		}
		arr[j+1] = key;
	}
}

void printArray(int *arr){
	for(int c = 0; c < sizeof(arr); c++){
		printf("%d ", arr[c]);
	}
	printf("\n");
}