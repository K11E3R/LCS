// https://leetcode.com/problems/height-checker

/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
    let s = [...heights]
    s.sort((a,b)=>a-b)
    let c = 0
    s.forEach( (elem, i ) => {
        if (heights[i] !== elem){
            c++
        }
    }
    )
    // for(let i=0; i<heights.length;i++){
    //     if (heights[i] !== s[i]){
    //         c++
    //     }
    // }
    return c
};
