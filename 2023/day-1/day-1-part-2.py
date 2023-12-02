import re
import wordninja
import ast

#mapping to identify strings and convert to integers

mapping = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

#not ideal but this will map any strings that are multiple digits to the integer value

mapping_entries = {f'{i}': i for i in range(1, 10000000)}

#this line added the mapping entry to the mapping we're using above to combine the two

mapping.update(mapping_entries)

#function that uses wordninja to split characters & words

def separate_alphabets_numbers(line):
    alphabets = "" 
    numbers = ""
    word = wordninja.split(line)

    for char in line:
        if char.isalpha():
            alphabets += char
        elif char.isdigit():
            numbers += char

    return alphabets, numbers, word

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
output_filename = 'output.txt'
test_file = 'test.txt'
part2_final_file = 'part2.txt'
processed_filename = 'processed.txt'
final_filename = 'final.txt'

#this block of code parses the text; day-1 requests parsing out all the text from the numbers

with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    for line in infile:
        alphabets, numbers, word = separate_alphabets_numbers(line)
        # For example, write the separated alphabets and numbers to a new file
        outfile.write(f"{word}\n")

with open (output_filename, 'r') as infile, open(processed_filename, 'w') as outfile:
    for line in infile:
        items = ast.literal_eval(line)
        mapped_items = []
        for item in items:
            if item in mapping:
                mapped_items.append(mapping[item])
        outfile.write(f"{mapped_items}\n")

with open (processed_filename, 'r') as infile, open(final_filename, 'w') as outfile:
    for line in infile:
        # line = infile.readline().strip()
        my_list = ast.literal_eval(line)
        first_item = my_list[0]
        last_item = my_list[-1]
        outfile.write(f"{first_item}{last_item}\n")

#final processing for first and last digit for part 2; improved from part 1

with open(final_filename, 'r') as infile, open(part2_final_file, 'w') as outfile:
    for line in infile:
            first_digit,last_digit = get_first_last_digits(line.strip())
            outfile.write(f"{first_digit}{last_digit}\n")

result_part2 = sum_numbers_in_file (part2_final_file)
print(f"The answer is for part 2:", result_part2)