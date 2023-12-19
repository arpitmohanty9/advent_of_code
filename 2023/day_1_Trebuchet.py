# Day 1 : Trebuchet?!
# calibration document
# lines of text,
# each line contained spec calibration value
# calibration value = first digit + last digit
# single two-digit number.

# # eg. 
# 1abc2          - 12
# pqr3stu8vwx     - 38
# a1b2c3d4e5f    - 15
# treb7uchet     - 77

# total = 142

# sample data
# 7jlncfksix7rjgrpglmn9
# vcgkgxninerqjltdbhqzzpd4nine23
# fx3
# 8nrbjbpjpnineseven
# 7qlfhcsnxn7fpfhjcgr6eightsevenjlpchjtzpztwo
# 28rzgskgk94ninefive
# zdpxcql1eight5

import os

script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'inputs/day_1_Trebuchet.txt')


def calibration_value(word):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    i= 0
    j= len(word)-1
    i_finalized = False
    j_finalized = False
    while (i<j and not (i_finalized and j_finalized)):
        if word[i] not in digits:
            i+=1
        else :
            i_finalized = True
        if word[j] not in digits:
            j-=1
        else: j_finalized = True

    return word[i] + word[j]


final_sum = 0
# Open the file in read mode ('r')
with open(input_path, 'r') as file:
    for line in file:
        # print(line , end='')
        final_sum += int(calibration_value(line))

print(final_sum)

