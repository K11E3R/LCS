// https://leetcode.com/problems/find-all-people-with-secret

/**
 * @param {number} n
 * @param {number[][]} meetings
 * @param {number} firstPerson
 * @return {number[]}
 */

function groupMeetingsByIndex(sortedM) {
  const groupedByIndex = {};
  sortedM.forEach((meeting) => {
    const index = meeting[2];
    if (!groupedByIndex[index]) {
      groupedByIndex[index] = [];
    }
    groupedByIndex[index].push(meeting);
  });
  return groupedByIndex;
}


var findAllPeople = (n, meetings, firstPerson)=>{
    let res = new Array()
    res.push(0)
    res.push(firstPerson)
    let sortedM = meetings
    let List_Meeting = new Array()
    sortedM.forEach((a)=>{
        List_Meeting.push([[a[0],a[2]],[a[1],a[2]]])
      })
    sortedM.sort((a, b) => a[2]-b[2])
    const groupbY  = groupMeetingsByIndex(sortedM)
    for (var prop in groupbY) {
      groupbY[prop].sort((a,b) => {
        if(res.includes(a[0]) || res.includes(a[1])){
          return -1
        }
      })
    groupbY[prop].forEach((a)=>{
        if (res.includes(a[0]) ){
                res.push(a[1])
            }
            if (res.includes(a[1]) ){
                res.push(a[0])
            }
        }
    )}
    return Array.from(new Set(res)).sort((a, b)=> a-b)
};