def dist(a, b):
    return abs(ord(a)-ord(b))

def longestKInterspaceSubstring(word, k):
    temp = ""
    max = ""
    flag = 0
    for i in range(len(word) - 1):
        temp += word[i]
        if dist(word[i], word[i + 1]) > k:
            flag = 1
            if len(max) >= len(temp):
                max = max
            else:
                max = temp
        
            temp = ""
            
        if i == len(word) - 2:
            temp += word[i + 1]
            
    
    if flag == 0:
        max = temp
        
    return max
    