class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first = 0
        second = 0
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []


        while first < n1 and second < n2:
            if nums1[first] <= nums2[second]:
                ans.append(nums1[first])
                first += 1
            else:
                ans.append(nums2[second])
                second += 1


        ans.extend(nums1[first:])
        ans.extend(nums2[second:])

        n = len(ans)


        if n % 2 == 0:
            return (ans[n // 2 - 1] + ans[n // 2]) / 2
        else:
            return ans[n // 2]