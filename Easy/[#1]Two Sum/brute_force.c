/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i=0,j=0,b[20];
    int* result=(int*)malloc(2*sizeof(int));
    for(i=0;i<numsSize;i++){
        for(j=i+1;j<numsSize;j++){
            if(nums[i]+nums[j]==target){
                *returnSize=2;
                result[0]=i;
                result[1]=j;
                return result;
            }
            
        }
    }
    free(result);
    *returnSize=0;
    return NULL;
}