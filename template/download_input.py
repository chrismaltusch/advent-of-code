import requests

#this block of code automates the download of the input file; should only be run once not every single time

cookies = {'session': '53616c7465645f5fab86d3a643a0a8975027e4910b52363c27daa71bd0adc4e5386cf1ae6d437ae9b7995f120baa22a80df943d5b76983de4ca853273fecadfe'}
url = 'https://adventofcode.com/2023/day/4/input'

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