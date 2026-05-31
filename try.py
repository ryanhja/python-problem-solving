nbs = [8, 4, 5, 1, 3, 9, 7, 6]

def tri_number(numbers):
    for j in range(len(numbers)):
        for i in range(len(numbers) - 1):
            if numbers[i + 1] < numbers[i]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    return numbers

print(tri_number(nbs))