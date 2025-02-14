def modify_string(txt):
    vowels = "aeiou"
    result = []
    previous_underscore=[]
    i = 2
    
    while i < len(txt):
        result.append(txt[i-2])
        result.append(txt[i-1])
        result.append(txt[i])
        j = i

        while j < len(txt):
            if txt[j] in vowels or txt[j] in previous_underscore:
                j+1
                result.append(txt[j+1])
            elif j+1 == len(txt):
                break
            else:
                result.append('_')
                previous_underscore.append(txt[j])
                break
            j += 1
        
        i = j+3

    return "".join(result)

# Example usage
txt1='assalom'
txt2 = "abcabcdabcdeabcdefabcdefg"
output1 = modify_string(txt1)
output2 = modify_string(txt2)

print(output1)
print(output2)
