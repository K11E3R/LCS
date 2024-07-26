// https://leetcode.com/problems/find-all-people-with-secret

const findAllPeople = (n, meetings, firstPerson) => {
    const parent = Array.from({ length: n }, (_, i) => i);
    const rank = Array(n).fill(0);

    const find = x => (parent[x] === x ? x : (parent[x] = find(parent[x])));
    const union = (x, y) => {
        const rootX = find(x), rootY = find(y);
        if (rootX !== rootY) {
            if (rank[rootX] > rank[rootY]) parent[rootY] = rootX;
            else if (rank[rootX] < rank[rootY]) parent[rootX] = rootY;
            else { parent[rootY] = rootX; rank[rootX] += 1; }
        }
    };

    union(0, firstPerson);
    meetings.sort((a, b) => a[2] - b[2]);

    for (let i = 0; i < meetings.length; ) {
        const currentTime = meetings[i][2];
        const group = [];
        while (i < meetings.length && meetings[i][2] === currentTime) group.push(meetings[i++]);

        const initialParents = new Map();
        group.forEach(([a, b]) => {
            initialParents.set(a, find(a));
            initialParents.set(b, find(b));
            union(a, b);
        });

        const knowsSecret = new Set([...initialParents.keys()].filter(p => find(p) === find(0)));

        initialParents.forEach((initialParent, p) => parent[p] = initialParent);
        group.forEach(([a, b]) => (knowsSecret.has(a) || knowsSecret.has(b)) && union(a, b));
    }

    return Array.from({ length: n }, (_, i) => i).filter(i => find(i) === find(0));
};