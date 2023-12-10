NUMBERS = [
    ["one", '1'],
    ["two", '2'],
    ["three", '3'],
    ["four", '4'],
    ["five", '5'],
    ["six", '6'],
    ["seven", '7'],
    ["eight", '8'],
    ["nine", '9']
]

input = open("Day 1\input.txt", "r")
sum = 0
# For each line, combine the first digit and last digit
for line in input:
    all_digits = []
    calibration_val = ''
    length = len(line)
    # For each character in the current line
    for i in range(length):
        char = line[i]
        # If the current character is a number (a digit, not a word)
        if char in [number[1] for number in NUMBERS]:
            all_digits.append(char)
        else:
            # Check if each possible number (as a word) is in the next 5 digits
            for number in NUMBERS:
                # Start with 3 letter number, then 4, then 5
                if number[0] == line[i:i+3]:
                    all_digits.append(number[1])
                elif number[0] == line[i:i+4]:
                    all_digits.append(number[1])
                elif number[0] == line[i:i+5]:
                    all_digits.append(number[1])
        
    calibration_val = all_digits[0] + all_digits[len(all_digits) - 1]
    sum += int(calibration_val)
print(sum)