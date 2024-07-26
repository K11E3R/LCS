// https://leetcode.com/problems/find-all-people-with-secret

function groupMeetingsByIndex(sortedM) {
  return Object.groupBy(sortedM, (a) => a[2] )
}


var findAllPeople = (n, meetings, firstPerson)=>{
    let res = new Array()
    res.push(0)
    res.push(firstPerson)
    let sortedM = meetings

    // console.debug("-----------------------------------------")
    // console.log("sorted M: ")
    // console.table(sortedM)
    // console.log(sortedM)
    const groupbY  = groupMeetingsByIndex(sortedM)
    // console.debug("------------ groupbY ------------")
    // console.table(groupbY)
    for (var prop in groupbY) {
      // console.log("key : ", prop, "val B: ", groupbY[prop])
      groupbY[prop].sort((a,b) => {
          if(res.includes(a[0]) || res.includes(a[1])){
            return -1
          }
        })

      groupbY[prop].forEach((a)=>{
          //console.debug("res second : ", res)
          if (res.includes(a[0]) ){
                  //console.debug("case 0 0 :", a)
                  res.push(a[1])
              }
              if (res.includes(a[1]) ){
                  //console.debug("case 1 0 :", a)
                  res.push(a[0])
              }
          })
      //console.log("key : ", prop, "val A: ", groupbY[prop])
    }

    //console.debug("base result : ", res)
    // console.debug("-----------------------------------------")
    // console.table("listed meetings : ")
    // console.table(List_Meeting)
    // console.log(List_Meeting)
    //console.debug("-----------------------------------------\n")
    // TODO
    // check if all time checker(List_Meeting) in same list
    // console.log("List_Meeting[0]: ", List_Meeting[0])
    // console.log("List_Meeting B: ",List_Meeting)

    // const groupedByTime = groupMeetingsByIndex(List_Meeting, 1);
    //console.log("groupedBYtime : ", groupedByTime)

    // console.log("List_Meeting A: ",List_Meeting)
    // console.debug("-----------------------------------------\n")
    //console.table(groupedByTime['1'])

    //console.debug("-------------LIST MEETINGS ----------------")

    // List_Meeting.forEach((a)=>{
    //     //console.debug("res second : ", res)

    //     if (res.includes(a[0][0]) ){
    //             //console.debug("case 0 0 :", a)
    //             res.push(a[1][0])
    //         }
    //         // if (res.includes(a[1][0]) ){
                //console.debug("case 1 0 :", a)
    //             res.push(a[0][0])
    //         }
    //     }
    // )
    //console.debug("result : ", res)
    // console.debug("-----------------------------------------")
    return Array.from(new Set(res)).sort((a, b)=> a-b)
};
