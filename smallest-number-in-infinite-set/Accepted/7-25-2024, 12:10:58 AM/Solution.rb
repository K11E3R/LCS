// https://leetcode.com/problems/smallest-number-in-infinite-set

class SmallestInfiniteSet
    def initialize()
        @set = Set.new
        for i in(1).upto(1000)
            @set.add(i)
        end
    end


=begin
    :rtype: Integer
=end
    def pop_smallest()
        num = @set.min
        @set.delete(num)
        num
    end


=begin
    :type num: Integer
    :rtype: Void
=end
    def add_back(num)
        @set.add(num) unless @set.include?(num)
    end


end

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet.new()
# param_1 = obj.pop_smallest()
# obj.add_back(num)