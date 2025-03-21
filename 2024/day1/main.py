def get_data(filename):
    data = []
    with open("input.txt", "r") as file:
        for line in file:
            data.extend(map(int, line.split()))  # Convert numbers to int and add to list
    return data

def part1(data):
    left = []
    right = []

    for i in range(len(data)):
        if i % 2 == 0:
            left.append(data[i])
        else:
            right.append(data[i])

    left.sort()
    right.sort()

    ans = 0
    for i in range(len(left)):
        ans += abs(left[i] - right[i])

    return ans

def part2(data):
    left = []
    right = {}

    for i in range(len(data)):
        num = data[i]
        if i % 2 == 0:
            left.append(num)
        else:
            right[num] = right.get(num, 0) + 1

    ans = 0
    for val in left:
        if val in right and right[val] != 0:
            ans += (val * right[val])

    return ans
    

if __name__ == "__main__":
    input_data = get_data("./input.txt")
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))