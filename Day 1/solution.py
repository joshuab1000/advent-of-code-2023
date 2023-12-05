NUMBERS = "0123456789"
input = open("Day 1\input.txt", "r")
sum = 0
# For each line, combine the first digit and last digit
for line in input:
    all_digits = []
    calibration_val = ''
    for char in line:
        if char in NUMBERS:
            all_digits.append(char)
    calibration_val = all_digits[0] + all_digits[len(all_digits) - 1]
    sum += int(calibration_val)
print(sum)