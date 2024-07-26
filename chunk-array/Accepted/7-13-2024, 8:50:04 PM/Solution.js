// https://leetcode.com/problems/chunk-array

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const res = []
    for (let i=0, n= arr.length; i<n; i += size){
        res.push(arr.slice(i, i+size))
    }
    return res
};
