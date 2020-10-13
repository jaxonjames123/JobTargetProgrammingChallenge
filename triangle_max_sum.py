# Author: Jaxon Terrell
# Date: 10/13/2020

from io import StringIO
import os
import sys

def max_sum(filename):
    max_numbers = []
    max_sum = 0
    position = 0
    new_position = 0
    if os.path.exists(filename): ## Check to see if given input parameter exists before running
        print(f'{filename} exists')
        with open(filename) as f:
            while True:
                line_list = f.readline().split()
                if new_position > position:
                    position += 1
                for item in range(position, position+2):    # Because we only want adjacency, the next row will only conatin
                    try:
                        line_list[item] = float(line_list[item])    ## Cast each item in the list to a float, 
                                                                    ## in case we want to take the max sum of decimals
                    except IndexError:
                        break
                    except ValueError:  ## Exception handling if there is a string in the file
                        print('Please use a text file with numbers only')
                        sys.exit()
                if not line_list:
                    break
                try:
                    if line_list[position] < line_list[position+1]:
                        max_numbers.append(line_list[position+1])
                        new_position += 1
                    else: 
                        max_numbers.append(line_list[position])
                except IndexError:
                    max_numbers.append(line_list[position])
    else:
        print('File doesnt exist')
    for number in max_numbers:
        max_sum += number
    ## Commented the below print statement out because it was not asked for
    ## Prints the appropriate number taken from each line, good for if you wanted to see what the
    ## number used at a specific point was
    # print(f'Largest adjacent numbers from each line: {max_numbers}')
    print(f'The max sum of the triangle is: {max_sum:,.0f}') 
    print(f'The max sum of the triangle in decimal form is {max_sum}')
                ## This is code for if you wanted to take the largest number from each row, and not just the adjacent numbers
                ## Using a python "stack" (Inefficient due to nested for loop, has O(n^2) runtime for worst case)
                # for number in line_list:
                #     max_numbers.append(number)
                #     for second_number in line_list:
                #         if number < second_number:
                #             position = line_list.index(second_number)
                #             max_numbers.pop()
                #             break
filename = sys.argv[1]
max_sum(filename)  