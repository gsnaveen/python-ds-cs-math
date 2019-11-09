class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):

        f,s,l = 0,0,len(A) -1
        lenS = len(A) -1
        A = list(A)

        while s <= l:
            val = int(A[s])
            if val == 0:
                A[f],A[s] = A[s],A[f]
                f += 1
                s += 1
            elif val == 2:
                A[l], A[s] = A[s], A[l]
                l -= 1
            else:
                s += 1

        print(A)

if __name__ == '__main__':
    a = Solution()
    print(a.sortColors('00111222120021'))
