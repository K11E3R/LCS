// https://leetcode.com/problems/average-waiting-time

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time = time_calc = 0
        for arrivali, timei in customers:
            time_calc = max(time_calc, arrivali) + timei
            waiting_time += time_calc - arrivali
        return waiting_time / len(customers)