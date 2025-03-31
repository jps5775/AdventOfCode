import os
import re

def part2(data):
    ans = 0
    # print(data)
    for row in data:
        x = int(row[0])
        y = int(row[1])
        ans += x * y
    return ans

def part1(data):
    ans = 0
    for row in data:
        x = int(row[0])
        y = int(row[1])
        ans += x * y
    return ans

def parse_input2(filename):
    data = ""
    with open(filename, "r") as file:
        data = file.read()

    new_data = []
    is_enabled = True
    for i in range(len(data)):
        if data[i] == "d":
            print("found d")
            # check if do
            check_do = data[i:i+4]
            if check_do == "do()":
                is_enabled = True
                i += 5
                print("found do")
            # check if don't
            check_dont = data[i:i+7]
            if check_dont == "don't()":
                is_enabled = False
                i += 8
                print("found don't")
        if is_enabled:
            new_data.append(data[i])

    new_input_str = ''.join(new_data)

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return re.findall(pattern, new_input_str)

def parse_input1(filename):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    # matches will be in this format [('12', '34'), ('56', '78'), ('9', '10')]

    matches = []
    with open(filename, "r") as file:
        matches = re.findall(pattern, file.read())
    return matches

def get_input_file():
    file_name = "input.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    full_file_path = os.path.join(script_dir, file_name)  # Construct the full path
    return full_file_path

if __name__ == "__main__":
    print("Part 1:", part1(parse_input1(get_input_file())))
    print("Part 2:", part2(parse_input2(get_input_file())))