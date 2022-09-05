class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # swap
        total_left = (len(nums1) + len(nums2) + 1)//2
        i = None
        # TODO(NANO) 想办法对k二分

if __name__ == '__main__':
    pass