class fibonacci_sequence:
    def __init__(self, n):
        self.leng = int(n)
        self.left = 0
        self.right = 1
        self.i = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i <= self.leng:
            self.i += 1
            self.left, self.right = self.right, self.left + self.right
            return self.left
        else:
            raise StopIteration
