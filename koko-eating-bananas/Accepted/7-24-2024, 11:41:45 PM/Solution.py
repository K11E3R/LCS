// https://leetcode.com/problems/koko-eating-bananas

def minEatingSpeed(piles: List[int], h: int) -> int:
    M, S, N = max(piles), sum(piles), len(piles)
    right, left = min(ceil(S/(h-N+1)), M) , ceil(S/h)
    if N == h: return M

    while right >= left:
        mid = (right + left) // 2
        if (t:=sum([ceil(x/mid) for x in piles])) > h:
            left = mid + 1
        else: 
            right = mid - 1
    return left

with open("user.out", 'w') as f:
    inputs = map(loads, stdin)
    for piles in inputs:
        h = next(inputs)
        print(minEatingSpeed(piles, h), file=f)
exit(0)