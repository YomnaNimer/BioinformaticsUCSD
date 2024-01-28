# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    Pattern = Reverse(Pattern)  # reverse all letters in a string
    Pattern = Complement(Pattern)  # complement each letter in a string
    return Pattern

def Reverse(Pattern):
    reverse_pattern = ""
    for i in range(len(Pattern)):
        reverse_pattern += Pattern[len(Pattern)-i-1]
    return reverse_pattern                        

def Complement(Pattern):
    new_pattern = ""
    for i in range(len(Pattern)):
        if Pattern[i] == "A":
            new_pattern += "T"
        elif Pattern[i] == "T":
            new_pattern += "A"
        elif Pattern[i] == "G":
            new_pattern += "C"
        elif Pattern[i] == "C":
            new_pattern += "G"
    return new_pattern

Pattern="AAAACCCGGT"

print (ReverseComplement(Pattern))
