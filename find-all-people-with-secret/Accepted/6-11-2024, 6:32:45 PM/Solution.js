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
    const parent = Array.from({ length: n }, (_, i) => i);
    const rank = Array(n).fill(0);

    const find = (x) => {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    };

    const union = (x, y) => {
        const rootX = find(x);
        const rootY = find(y);
        if (rootX !== rootY) {
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX] += 1;
            }
        }
    };

    union(0, firstPerson);
    meetings.sort((a, b) => a[2] - b[2]);

    const groupedByTime = groupMeetingsByIndex(meetings);

    for (const time in groupedByTime) {
        const currentMeetings = groupedByTime[time];
        const tempUnionFind = new Map();
        const participants = new Set();

        currentMeetings.forEach(([a, b]) => {
            tempUnionFind.set(a, find(a));
            tempUnionFind.set(b, find(b));
            participants.add(a);
            participants.add(b);
        });

        currentMeetings.forEach(([a, b]) => union(a, b));

        const knowsSecret = new Set();
        participants.forEach(p => {
            if (find(p) === find(0)) {
                knowsSecret.add(p);
            }
        });

        tempUnionFind.forEach((initialRoot, p) => {
            parent[p] = initialRoot;
        });

        currentMeetings.forEach(([a, b]) => {
            if (knowsSecret.has(a) || knowsSecret.has(b)) {
                union(a, b);
            }
        });
    }

    const result = [];
    for (let i = 0; i < n; i++) {
        if (find(i) === find(0)) {
            result.push(i);
        }
    }

    return result.sort((a, b) => a - b);
};