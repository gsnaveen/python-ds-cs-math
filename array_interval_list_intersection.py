def interSection(A,B):
    i = j = 0
    Alen = len(A); Blen = len(B)
    mlen = max(len(A),len(B))
    myO = []

    while i < len(A) and j < len(B):

        aStart , aEnd = A[i]
        bStart ,bEnd = B[j]

        if aEnd < bEnd:
            i += 1
        else:
            j += 1

        if aEnd >= bStart and bEnd >= aStart :
            tList = sorted([aStart,aEnd,bStart,bEnd])
            myO.append([tList[1],tList[2]])

    return myO

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


print(interSection(A,B))
