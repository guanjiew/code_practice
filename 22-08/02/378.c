#include <stdlib.h>
#include <stdio.h>
// compare function for qsort
int cmp(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}
// kthSmallest function
int kthSmallest(int** matrix, int matrixRowSize, int matrixColSize, int k){
    // allocate 1d array to store the matrix
    int *arr = (int *)malloc(matrixRowSize * matrixColSize * sizeof(int));
    // copy the matrix to the array
    for (int i = 0; i < matrixRowSize; i++) {
        for (int j = 0; j < matrixColSize; j++) {
            arr[i * matrixColSize + j] = matrix[i][j];
        }  
    }
    // sort the array
    qsort(arr, matrixRowSize * matrixColSize, sizeof(int), cmp);
    // return the kth element
    return arr[k - 1];
}

// main function
void main() {
    // malloc an 2d array
    int **matrix = (int **)malloc(3 * sizeof(int *));
    for (int i = 0; i < 3; i++) {
        matrix[i] = (int *)malloc(3 * sizeof(int));
    }
    // assign the matrix
    matrix[0][0] = 1;
    matrix[0][1] = 5;
    matrix[0][2] = 9;
    matrix[1][0] = 10;
    matrix[1][1] = 11;
    matrix[1][2] = 13;
    matrix[2][0] = 12;
    matrix[2][1] = 13;
    matrix[2][2] = 15;
    int k = 8;
    int result = kthSmallest(matrix, 3, 3, k);
    printf("%d\n", result);

    // free the 2d array
    for (int i = 0; i < 3; i++) {
        free(matrix[i]);
    }
    free(matrix);


}

