def modify_string2(txt):
    done = ['a','e','i','o','u']
    result = []
    i = 0
    count=0
    for i in range(len(txt)):
        count +=1
        result.append(txt[i])
        if i!=len(txt)-1 and count >=3 and txt[i] not in done:
            result.append('_')
            done.append(txt[i])
            count=0
    
    return print("".join(result))
            
# Example usage
txt1='assalom'
txt2 = "abcabcdabcdeabcdefabcdefg"
output1 = modify_string2(txt1)
output2 = modify_string2(txt2)

print(output1)
print(output2)