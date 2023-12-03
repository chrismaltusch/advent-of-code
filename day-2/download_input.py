import requests

#this block of code automates the download of the input file; should only be run once not every single time

cookies = {'session': '53616c7465645f5f46485efdb1e993f0b2813dffb3438d335654dbb21ebe0ecb8206e5c5fdcd854605cbd3852f1c753eff3a3c3364341d3dc0d75029609429c6'}
url = 'https://adventofcode.com/2023/day/2/input'

response = requests.get(url, cookies=cookies)

if response.status_code == 200:
    input_data = response.text.splitlines()
else:
    print("Failed to download the input")

#this block of code is used to save the download to a text file

filename = 'input.txt'  # Name of the file where you want to save the input

with open(filename, 'w') as file:
    if isinstance(input_data, list):
        # If input_data is a list, write each element on a new line
        for line in input_data:
            file.write(line + '\n')
    else:
        # If input_data is a single string, just write it to the file
        file.write(input_data)

print(f"Input data saved to {filename}")