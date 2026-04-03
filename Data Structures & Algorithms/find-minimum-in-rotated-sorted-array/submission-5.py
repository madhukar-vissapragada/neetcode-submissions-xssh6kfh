class Solution:
    def findMin(self, A: List[int]) -> int:
        low = 0
        high = len(A) - 1

        while low < high:
            mid = (low + high) // 2

            if A[mid] > A[high]:
                low = mid + 1
            else:
                high = mid

        return A[low]
