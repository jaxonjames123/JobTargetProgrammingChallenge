# JobTargetProgrammingChallenge
 A script that allows users to input a file containing a triangle of numbers,
 and starting from the top, adds the largest number that is adjacent to the largest number from the row above it
## For example:    
     5
    9 6
    4 6 8 
    0 7 1 5
 Would print a result of 27 (5 + 9 + 6 + 7)
 Due to not being previously specified, if the two candidates are the same value (9 and 9), the leftmost value is chosen
## To run the script: 
 1) cd projectdirectory
 2) python triangle_max_sum.py triangle.txt
