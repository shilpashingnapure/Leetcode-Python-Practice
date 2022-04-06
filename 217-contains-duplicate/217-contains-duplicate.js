/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    var d = {}
    for(let i = 0 ; i < nums.length ; i++){
        if(nums[i] in d){
            d[nums[i]]++;
            return true
        }else{
            d[nums[i]] = 1
        }
    }
    return false
    
};