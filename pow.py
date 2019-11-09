class solution:

    def myPow(self,base: float,power : int) -> float:
        value = 1
        for i in range(abs(power)):
            value *= base

        if power < 0:
            value = (1/value)

        return value

if __name__ == '__main__':

    a = solution()
    base = 2.000
    power = 10
    print(a.myPow(base,power))
    power = -2
    print(a.myPow(base, power))
