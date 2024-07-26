// https://leetcode.com/problems/network-delay-time

import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        pq = [(0, k)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            if current_dist > dist[u]:
                continue

            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        max_time = max(dist[1:])

        return max_time if max_time != float('inf') else -1
