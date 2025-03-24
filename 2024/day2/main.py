import os

def is_row_valid(nums):
    # check if strictly increasing
    is_increasing = True
    for i in range(1, len(nums)):
        if(nums[i - 1] > nums[i]):
            is_increasing = False
            break

    # check if strictly decreasing
    is_decreasing = True
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            is_decreasing = False
            break
    
    if not is_increasing and not is_decreasing:
        return False

    for i in range(1, len(nums)):
        diff = abs(nums[i - 1] - nums[i])
        if diff != 1 and diff != 2 and diff != 3:
            return False

    return True

def is_row_valid2(nums):
    for i in range(len(nums)):
        if is_row_valid(nums[0:i] + nums[i + 1 : len(nums)]):
            return True

def part1(data):
    ans = 0
    for row in data:
        ans += 1 if is_row_valid(row) else 0
    return ans

def part2(data):
    ans = 0
    for row in data:
        ans += 1 if is_row_valid2(row) else 0
    return ans


def parse_input(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            row = line.split()
            int_row = []
            for num in row:
                int_row.append(int(num))
            data.append(int_row)
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
    