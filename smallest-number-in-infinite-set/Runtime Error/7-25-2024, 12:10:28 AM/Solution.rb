// https://leetcode.com/problems/smallest-number-in-infinite-set

class SmallestInfiniteSet

    def initialize
        @t = CRBTreeMap.new
        @c = 0
    end

    def pop_smallest
        @t.empty? ? @c += 1 : @t.delete_min
    end

    def add_back x
        @t[x] = x if x <= @c
    end

end
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet.new()
# param_1 = obj.pop_smallest()
# obj.add_back(num)