#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i, j;
    int *result = (int *)malloc(sizeof(int) * 2);
    for (i = 0; i < numsSize; i++) {
        for (j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    return NULL;
}




int main() {
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int returnSize;
    int *result = twoSum(nums, 4, target, &returnSize);
    printf("%d %d \n", result[0], result[1]);   
    free(result);
    return 0;
}

