class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

# Create an instance of MathDojo
md = MathDojo()

# Test add method
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5

# Test subtract method
y = md.subtract(10, 2, 1).subtract(3).result
print(y)  # should print -7
