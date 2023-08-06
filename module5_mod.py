class Numbers:
    def __init__(self):
        self.data = []

    def insert(self, num):
        self.data.append(num)

    def search(self, x):
        if x in self.data:
            return self.data.index(x) + 1
        else:
            return -1
