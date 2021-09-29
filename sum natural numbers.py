summation = 0

def calculate_totalsum(end, begin = 0):
    totalsum = 0
    for start in range(begin,end):
        if(start%7==0) or (start%9==0):
            totalsum+=start
    return totalsum
 
summation=calculate_totalsum(10000)
print(summation)
