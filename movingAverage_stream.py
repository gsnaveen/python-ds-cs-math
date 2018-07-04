class MovingAverage:
    size = 0
    numVal = 0
    listVal = []
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.listVal) < self.size:
            self.listVal.append(val)
            self.numVal += 1
        else:
            self.listVal.pop(0)
            self.listVal.append(val)
            
        return sum(self.listVal)/self.numVal


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
if __name__ == "__main__":
    
    m = MovingAverage(3);
    print(m.next(1))
    print(m.next(10))
    print(m.next(3))
    print(m.next(5))
