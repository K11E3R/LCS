// https://leetcode.com/problems/find-all-people-with-secret

class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        union(0, firstPerson)

        meetings.sort(key=lambda x: x[2])

        i = 0
        while i < len(meetings):
            current_time = meetings[i][2]
            current_meetings = []
            people = set()

            while i < len(meetings) and meetings[i][2] == current_time:
                x, y, _ = meetings[i]
                current_meetings.append((x, y))
                people.add(x)
                people.add(y)
                i += 1

            initial_parent = {p: find(p) for p in people}
            temp_parent = initial_parent.copy()

            for x, y in current_meetings:
                union(x, y)

            knows_secret = {p for p in people if find(p) == find(0)}

            for p in people:
                parent[p] = temp_parent[p]

            for x, y in current_meetings:
                if x in knows_secret or y in knows_secret:
                    union(x, y)

        return [i for i in range(n) if find(i) == find(0)]
