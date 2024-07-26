// https://leetcode.com/problems/average-waiting-time

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time = time_calc = 0
        for a, b in customers:
            time_calc = max(time_calc, a) + b
            waiting_time += time_calc - a
        return waiting_time / len(customers)