// https://leetcode.com/problems/find-all-people-with-secret

/**
 * @param {number} n
 * @param {number[][]} meetings
 * @param {number} firstPerson
 * @return {number[]}
 */
var findAllPeople = function(n, meetings, firstPerson) {
    let res = new Array()
    res.push(0)
    res.push(firstPerson)
    let sortedM = meetings.sort((a,b)=>a[2]-b[2])
    let List_Meeting = new Array()
    sortedM.forEach((a)=>{
        List_Meeting.push([[a[0],a[2]],[a[1],a[2]]])
    })
    List_Meeting.forEach((a)=>{
        if (res.includes(a[0][0]) ){
            res.push(a[1][0])
        }
        if (res.includes(a[1][0]) ){
            res.push(a[0][0])
        }
    })

    return Array.from(new Set(res)).sort((a, b)=> a-b)
};