from collections import List

def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
    result = [0] * length        
    for s,e,v in updates:
        result[s] += v
        if e < length - 1: result[e+1] -= v
            
    for i in range(1, length): result[i] += result[i-1]
    return result
