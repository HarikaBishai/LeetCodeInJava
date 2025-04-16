class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int n1 = nums1.length;
        int n2 = nums2.length;
        int total = n1 + n2;
        int half = total / 2;

        int l = 0;
        int r = n1;

        while (l <= r) {
            int i = (l + r) / 2;
            int j = half - i;

            int aLeft = (i > 0) ? nums1[i - 1] : Integer.MIN_VALUE;
            int aRight = (i < n1) ? nums1[i] : Integer.MAX_VALUE;
            int bLeft = (j > 0) ? nums2[j - 1] : Integer.MIN_VALUE;
            int bRight = (j < n2) ? nums2[j] : Integer.MAX_VALUE;

            if (aLeft <= bRight && bLeft <= aRight) {
                if (total % 2 == 1) {
                    return Math.min(aRight, bRight);
                } else {
                    return (Math.max(aLeft, bLeft) + Math.min(aRight, bRight)) / 2.0;
                }
            } else if (aLeft > bRight) {
                r = i - 1;
            } else {
                l = i + 1;
            }
        }

        throw new IllegalArgumentException("Input arrays not sorted properly.");
    }
}
