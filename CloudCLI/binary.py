def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = items[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

 # Example usage:
 numbers =[10, 20, 30, 40, 50,60,70]
target = 80
result = binary_search(numbers, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print("Target not found")