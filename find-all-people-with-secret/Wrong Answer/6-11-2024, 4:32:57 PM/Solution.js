// https://leetcode.com/problems/find-all-people-with-secret


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

const findAllPeople = (n, meetings, firstPerson) => {
    let res = new Set([0, firstPerson]);
    console.log("res val : ", res)
    meetings.sort((a, b) => a[2] - b[2]);

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
            if (toAdd.has(a) || toAdd.has(b) ) {
                res.add(b);
                res.add(a);
            }
        });
    }
    console.log("last res val : ", res)
    return Array.from(res).sort((a, b) => a - b);
};