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

def main():
    numbers = Numbers()

    N = int(input("Enter the number of elements (N): "))
    while N <= 0:
        print("Please enter a positive integer for N.")
        N = int(input("Enter the number of elements (N): "))

    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.insert(num)

    X = int(input("Enter the number (X) to search for: "))
    index = numbers.search(X)
    print(index)

if __name__ == "__main__":
    main()
