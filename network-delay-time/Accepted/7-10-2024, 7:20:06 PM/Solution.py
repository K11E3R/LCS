// https://leetcode.com/problems/network-delay-time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(1, n+1)}
        for u,v,w in times:
            graph[u].append((v,w))
            
        dist = [float('inf')]*(n+1)
        dist[k] = 0
        pq = [(0, k)]
        
        
        while pq:
            c, u = min(pq, key=lambda x:x[0])
            pq.remove((c, u))
            
            if c > dist[u]:
                continue
        
            for v, wh in graph[u]:
                if dist[u] + wh < dist[v]:
                    dist[v] = dist[u] + wh
                    pq.append((dist[v], v))
        
        m = max(dist[1:])
        return m if m != float('inf') else -1
