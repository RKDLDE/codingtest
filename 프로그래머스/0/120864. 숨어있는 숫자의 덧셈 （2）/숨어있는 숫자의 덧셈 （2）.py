import re
def solution(my_string):
    answer = 0
    ms = re.split('a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z', my_string.lower())
    for i in ms:
        if i.isdigit():
            answer += int(i)    
    return answer