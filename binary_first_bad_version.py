class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while True:
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                if mid == 1 or not self.isBadVersion(mid - 1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1

    def isBadVersion(self,v):
        myD = {
            1: False,
            2: False,
            3: False,
            4: True,
            5: True,
            6: True

        }
        return myD[v]


if __name__ == '__main__':

    a = Solution()

    print(a.firstBadVersion(6))
