def add(a,b):

    mlen = max(len(a),len(b))

    carry = 0
    result = ''
    a = a.zfill(mlen)
    b = b.zfill(mlen)

    for i in range(mlen -1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0

        result = ( '1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if carry > 0:
        result = '1' + result

    return result


print(add('1','111')) # 1000
print(add('111','111')) # 1110
print(add('111','1000')) #1111
