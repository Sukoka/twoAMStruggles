/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *output = malloc(2*sizeof(int)); 
    output[0] = -1; 
    output[1] = -1; 
    for(int i = 0 ; i<numsSize; i++){
        for(int j = i+1; j<numsSize; j++){
            int sum = nums[i] + nums[j]; 
            if(sum == target){
                output[0] = i; 
                output[1] = j; 
                return output; 
            }
        }
    }
    *returnSize = 2; 
    return NULL; 
}
int main(){
    int nums[] = {2,7,11,15}; 
    int target = 18;
    int size = sizeof(nums)/sizeof(nums[0]); 
    int returnSize = 0; 
    int *r = twoSum(nums, size, target, &returnSize); 
    if(r[0] != -1){
        printf("%d %d", r[0], r[1]); 
        free(r); 
    }else{
        printf("Nothing"); 
    }
    return 0; 
}