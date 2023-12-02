import re

def separate_alphabets_numbers(line):
    alphabets = "" 
    numbers = ""

    for char in line:
        if char.isalpha():
            alphabets += char
        elif char.isdigit():
            numbers += char

    return alphabets, numbers

def get_first_last_digits(number):
    number_str = str(number)
    first_digit = number_str[0]
    first_digit = int(first_digit)
    last_digit = number_str[-1]
    last_digit = int(last_digit)

    return first_digit, last_digit

def sum_numbers_in_file(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into parts (assuming numbers are separated by spaces)
            parts = line.split()

            # Convert each part to an integer and add to the total
            for part in parts:
                try:
                    number = int(part)
                    total += number
                except ValueError:
                    # This handles the case where the part is not a number
                    continue

    return total

input_filename = 'input.txt'
output_filename = 'part1_processed.txt'
part1_final_file = 'part1_solution.txt'

#parses the text; day-1 requests parsing out all the text from the numbers

with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    for line in infile:
        alphabets, numbers = separate_alphabets_numbers(line)
        # For example, write the separated alphabets and numbers to a new file
        outfile.write(f"{numbers}\n")

#final processing for first and last digit for part 1; included comments from mistakes

with open(output_filename, 'r') as infile, open(part1_final_file, 'w') as outfile:
    for line in infile:
        # the if statement was not needed for 1 character lines - made this more complicated than it needed to be
        # if len(line.strip()) >= 2: 
            first_digit,last_digit = get_first_last_digits(line.strip())
            #this .strip() was breaking everything; looks like it didn't like the whitespacing
            outfile.write(f"{first_digit}{last_digit}\n")
        # else:
        #     outfile.write(line)

result_part1 = sum_numbers_in_file (part1_final_file)
print(f"The answer is for part 1:", result_part1)
