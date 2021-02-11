
def linear_search(items, item):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high)
        print(mid)
        guess = items[mid]
        if guess == item:
            return mid
        if guess > mid:
            high = mid - 1
        else:
            low = mid + 1
    return None


exampleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 30]

print('Answer:', linear_search(exampleValues, 1))



