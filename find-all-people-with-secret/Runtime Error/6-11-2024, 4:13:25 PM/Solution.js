// https://leetcode.com/problems/find-all-people-with-secret


var groupMeetingsByIndex = (sortedM) => {
  return Object.groupBy(sortedM, (a) => a[2] )
}

var findAllPeople = (n, meetings, firstPerson)=>{
    let res = new Array()
    res.push(0)
    res.push(firstPerson)
    let sortedM = meetings
    sortedM.sort((a, b) => a-b)
    console.debug("-----------------------------------------")
    console.debug("sorted M: ")
    //console.table(sortedM)
    console.debug(sortedM)
    const groupbY  = groupMeetingsByIndex(sortedM)
    console.debug("------------ groupbY ------------")
    console.table(groupbY)
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
          })
      console.warn("key : ", prop, "val A: ", groupbY[prop])
    }

    console.debug("result : ", res)
    return Array.from(new Set(res)).sort((a, b)=> a-b)
};



