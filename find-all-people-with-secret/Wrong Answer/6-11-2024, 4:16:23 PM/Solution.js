// https://leetcode.com/problems/find-all-people-with-secret

/**
 * @param {number} n
 * @param {number[][]} meetings
 * @param {number} firstPerson
 * @return {number[]}
 */
function groupMeetingsByIndex(sortedM) {
  return Object.groupBy(sortedM, (a) => a[2] )
}
const findAllPeople = (n, meetings, firstPerson) => {
    let res = new Set();
    res.add(0);
    res.add(firstPerson);
    meetings.sort((a, b) => a[2] - b[2]);

    const groupMeetingsByIndex = (sortedM) => {
        const groupedByIndex = {};
        sortedM.forEach((meeting) => {
            const time = meeting[2];
            if (!groupedByIndex[time]) {
                groupedByIndex[time] = [];
            }
            groupedByIndex[time].push(meeting);
        });
        return groupedByIndex;
    };

    const groupbY = groupMeetingsByIndex(meetings);

    for (let time in groupbY) {
        let toAdd = new Set();
        groupbY[time].forEach(([a, b, t]) => {
            if (res.has(a) || res.has(b)) {
                toAdd.add(a);
                toAdd.add(b);
            }
        });

        groupbY[time].forEach(([a, b, t]) => {
            if (toAdd.has(a)) {
                res.add(b);
            }
            if (toAdd.has(b)) {
                res.add(a);
            }
        });
    }

    return Array.from(res).sort((a, b) => a - b);
};
