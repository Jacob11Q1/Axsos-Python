class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        """Add one or more numbers to result"""
        self.result += num
        for n in nums:
            self.result += n
        return self  

    def subtract(self, num, *nums):
        """Subtract one or more numbers from result"""
        self.result -= num
        for n in nums:
            self.result -= n
        return self  


# ============================
# TESTING
# ============================

md = MathDojo()

x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)    

md = MathDojo()
print(md.add(1).result)         
print(md.add(3, 4).result)       
print(md.add(10, 20, 30).result)  


md = MathDojo()
print(md.subtract(5).result)           
print(md.subtract(2, 3).result)        
print(md.subtract(1, 1, 1, 1).result)  


md = MathDojo()
y = md.add(100, 50).subtract(30, 20).add(5).result
print(y)  