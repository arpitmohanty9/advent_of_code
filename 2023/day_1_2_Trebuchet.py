# Your calculation isn't quite right. 
# It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.





import os

script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'inputs/day_1_Trebuchet.txt')


def fix_word(word):
    # apparently there is some 
    spelled_digits = {'one' : 'o1e', 
                      'two' : 't2o' ,
                      'three': 't3e',
                      'four': 'f4r',
                      'five': 'f5e',
                      'six' : 's6x',
                      'seven' : 's7n',
                      'eight' : 'e8t',
                      'nine': 'n9e'
                      }
    for key,val in spelled_digits.items():
          if key in word:
              word = word.replace(key,val)

    return word        
    
def calibration_value(word):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    spelled_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']
    # can I fix the string by replacing these strings so that my old logic works

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
    for word in file:
        # print(line , end='')
        print(fix_word(word))
        print(calibration_value(fix_word(word)))
        print('\n')
        final_sum += int(calibration_value(fix_word(word)))

print(final_sum)

