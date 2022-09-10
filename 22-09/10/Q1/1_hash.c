#include <stdio.h>
#include <stdlib.h>
#include "uthash.h"
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

struct hash_table {
    int key;
    int value;
    UT_hash_handle hh;
};

struct hash_table *hash_table = NULL;

void insert(int key, int val){
    // Update the value if the key already exists, otherwise insert a new key-value pair
    struct hash_table *s;
    HASH_FIND_INT(hash_table, &key, s);
    if (s == NULL) {
        s = (struct hash_table *)malloc(sizeof(struct hash_table));
        s->key = key;
        s->value = val;
        HASH_ADD_INT(hash_table, key, s);
    } else {
        s->value = val;
    }
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i;
    struct hash_table *s;
    for (i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        (hash_table, &complement, s);
        if (s != NULL) {
            int *result = (int *)malloc(sizeof(int) * 2);
            result[1] = i;
            result[0] = s->value;
            *returnSize = 2;
            return result;
        }
        insert(nums[i], i);
    }
    *returnSize = 0;
    return NULL;
}





int main() {
    int nums[] = {3,3};
    int target = 6;
    int returnSize;
    int *result = twoSum(nums, 2, target, &returnSize);
    printf("%d %d \n", result[0], result[1]);   
    free(result);
    return 0;
}

