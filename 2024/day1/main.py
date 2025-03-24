import os

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

def parse_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.extend(map(int, line.split()))  # Convert numbers to int and add to list
    return data


def get_input_file():
    file_name = "input.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    full_file_path = os.path.join(script_dir, file_name)  # Construct the full path
    return full_file_path

if __name__ == "__main__":
    parsed_input = parse_input(get_input_file())

    print("Part 1:", part1(parsed_input))
    print("Part 2:", part2(parsed_input))