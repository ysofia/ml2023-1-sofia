def find_index(numbers, x):
    for i in range(len(numbers)):
        if numbers[i] == x:
            return i + 1
    return -1

def main():
    try:
        N = int(input("Enter the number of elements (N): "))
        numbers = []
        for i in range(N):
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)

        X = int(input("Enter the number to search (X): "))
        index = find_index(numbers, X)

        print(index)

    except ValueError:
        print("Enter valid integers.")

if __name__ == "__main__":
    main()
