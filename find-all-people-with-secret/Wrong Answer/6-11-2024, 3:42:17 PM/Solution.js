// https://leetcode.com/problems/find-all-people-with-secret

function groupMeetingsByIndex(sortedM) {
  return Object.groupBy(sortedM, (meeting) => meeting[2]);
}

const findAllPeople = (n, meetings, firstPerson) => {
    let res = new Set();
    res.add(0);
    res.add(firstPerson);

    // Sort meetings by time
    meetings.sort((a, b) => a[2] - b[2]);

    // Group meetings by time
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

    // Process each time group
    for (let time in groupbY) {
        let currentMeetings = groupbY[time];
        let peopleWithInfo = new Set();

        currentMeetings.forEach(([a, b, t]) => {
            if (res.has(a) || res.has(b)) {
                peopleWithInfo.add(a);
                peopleWithInfo.add(b);
            }
        });

        currentMeetings.forEach(([a, b, t]) => {
            if (peopleWithInfo.has(a)) {
                res.add(b);
            }
            if (peopleWithInfo.has(b)) {
                res.add(a);
            }
        });
    }

    return Array.from(res).sort((a, b) => a - b);
};