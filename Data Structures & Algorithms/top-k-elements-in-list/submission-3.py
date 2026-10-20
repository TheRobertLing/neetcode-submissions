class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            Use a hashmap to figure out what the frequency of each number is

            The upper bound for frequency is always n
            Therefore we can use an array of size n, initialized with empty lists where the index represents the frequency

            we can slot the numbers into the correct index

            then loop


            for num in num
        """

        counts = Counter(nums)
        freqs = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            freqs[freq].append(num)

        flattened = [ num for item in reversed(freqs) for num in item ]
        return flattened[:k]
        

