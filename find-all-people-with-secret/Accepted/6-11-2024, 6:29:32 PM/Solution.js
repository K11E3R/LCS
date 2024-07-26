// https://leetcode.com/problems/find-all-people-with-secret

function findAllPeople(n, meetings, firstPerson) {
    const parent = Array.from({ length: n }, (_, i) => i);
    const rank = Array(n).fill(0);

    function find(x) {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    function union(x, y) {
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
    }

    union(0, firstPerson);

    meetings.sort((a, b) => a[2] - b[2]);

    let i = 0;
    while (i < meetings.length) {
        const currentTime = meetings[i][2];
        const currentMeetings = [];
        const people = new Set();

        while (i < meetings.length && meetings[i][2] === currentTime) {
            const [x, y] = meetings[i];
            currentMeetings.push([x, y]);
            people.add(x);
            people.add(y);
            i += 1;
        }

        const initialParent = new Map();
        for (const p of people) {
            initialParent.set(p, find(p));
        }

        for (const [x, y] of currentMeetings) {
            union(x, y);
        }

        const knowsSecret = new Set();
        for (const p of people) {
            if (find(p) === find(0)) {
                knowsSecret.add(p);
            }
        }

        for (const p of people) {
            parent[p] = initialParent.get(p);
        }

        for (const [x, y] of currentMeetings) {
            if (knowsSecret.has(x) || knowsSecret.has(y)) {
                union(x, y);
            }
        }
    }

    return Array.from({ length: n }, (_, i) => i).filter(i => find(i) === find(0));
}