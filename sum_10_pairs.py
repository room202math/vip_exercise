'''
Problem:
Write a program that allows for an integer array to be passed in and will then output all of the pairs that sum up to 10.  Please provide a solution that allows for 1) output all pairs (includes duplicates and the reversed ordered pairs), 2) output unique pairs only once (removes the duplicates but includes the reversed ordered pairs), and 3) output the same combo pair only once (removes the reversed ordered pairs). 


    For example passing in [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9] the following results should occur:



        1) output all pairs would output: [1,9], [1,9], [4,6], [4,6], [5,5], [5,5], [5,5], [5,5], [5,5], [5,5], [6,4], [6,4] [9,1] , [9,1] 

        2) output unique pairs only once would output: [1,9], [4,6], [5,5], [6,4], [9,1] 

        3) output the same combo pair only once would output: [1,9], [4,6], [5,5]   

----
Solution:

Each case runs in O(n) time, since there is a hash table lookup and constant number of operations for each unique value in the array.

Although it is trivial to count the value occurances with a dictionary, I've done this with Counter since it is optimized.  I create the Counter on initialization, since this
step is common to all cases.  This step takes O(n) time and O(n) additional space.

Hence the total time for all cases is O(2n) = O(n).
'''

from collections import Counter

class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.num_freqs = Counter(self.nums)

    def get_sum_10_pairs(self, duplicates=True, ordered=True):
        pairs = []
        if duplicates and ordered:
            for num in self.num_freqs:
                if self.num_freqs[10 - num]:
                    summand_1_count = self.num_freqs[num]
                    # Given 10-summands x and y which occur in the input i and j times respectively, the number of non-unique ordered pairs should be i * j.  
                    # From the fact that [5,5] occurs 6 rather than 3 * 3 = 9 times in your solution, I am inferring that 
                    # we never count the pair of a particular element with itself, although this is not stated in the spec.
                    # Hence this if statement to handle the special case of num == 5.
                    summand_2_count = self.num_freqs[num] - 1 if num == 5 else self.num_freqs[10 - num]
                    pairs += [[num, 10 - num]] * summand_1_count * summand_2_count
            return pairs
        if ordered:
            # Again, handling the special case of 5; don't count a pair of a given 5 with itself.
            self.num_freqs[5] = 1 if self.num_freqs[5] > 1 else 0
            for num in self.num_freqs:
                if self.num_freqs[10 - num]:
                    pairs.append([num, 10 - num])    
            return pairs
        if duplicates:
            raise ValueError("A solution for the duplicate but unordered case is not supported.")
        for num in self.num_freqs:
            if self.num_freqs[10 - num]:
                pairs.append([num, 10 - num])
                self.num_freqs[num] = 0
        return pairs