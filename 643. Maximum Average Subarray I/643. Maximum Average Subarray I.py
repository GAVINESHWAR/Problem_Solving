class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        average = round(current_sum/k, 5)
        j=0
        for i in range(k,len(nums)):
            current_sum+= nums[i] - nums[j]
            ag = current_sum/k
            average = max(average, ag)
            j+=1
        return round(average, 5)