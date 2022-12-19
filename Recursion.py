print("Factorial Function")


def factorial(n):
    if n == 0:
        print('reached base case')
        return 1
    else:
        print('Currently on Call Stack: ' + str(n))
        return n * factorial(n - 1)


print(factorial(5))
print()

print("Drawing an English Ruler")


def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length."""
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length"""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


print(draw_ruler(4, 1))  # suppose to be 12, 4
print()

print("Binary Search")


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


nums = [22, 33, 44, 55, 101]
print(binary_search(nums, 22, 0, len(nums) - 1))
print(binary_search(nums, 8, 0, len(nums) - 1))
print(binary_search(nums, 44, 0, len(nums) - 1))
print(binary_search(nums, 22.5, 0, len(nums) - 1))
print(binary_search(nums, 101, 0, len(nums) - 1))
print()


def sumElementsInASequence(S, n):
    if n == 0:
        return 0
    else:
        return sumElementsInASequence(S, n - 1) + S[n - 1]


nums = [4, 6, 2, 5, 11]
print(sumElementsInASequence(nums, 3))


def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start: stop]"""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
print("Reverse Sequence")
reverse(nums, 0, len(nums))
for num in nums:
    print(num)







