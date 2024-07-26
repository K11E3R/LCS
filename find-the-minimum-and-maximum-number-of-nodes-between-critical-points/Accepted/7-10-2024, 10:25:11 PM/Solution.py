// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points

def nodesBetweenCriticalPoints(nums: List[int]) -> List[int]:
    firstCP = None
    currCP = None
    minDist = None
    
    for i, num in enumerate(nums[1:-1], 1):
        if (num > nums[i - 1] and num > nums[i + 1]) or (num < nums[i - 1] and num < nums[i + 1]):
            if firstCP is None:
                firstCP = i
            else:
                minDist = min(minDist, i - currCP) if minDist else i - currCP
            currCP = i

    minDist = -1 if not minDist else minDist
    maxDist = -1 if firstCP == currCP else currCP - firstCP
    return f'[{minDist},{maxDist}]'

f = open('user.out','w')
for i in map(loads, stdin):
    f.write(f'{nodesBetweenCriticalPoints(i)}\n')
f.flush()
exit(0)