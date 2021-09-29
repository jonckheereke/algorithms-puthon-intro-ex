def sequence(end):
    number1 = 2
    number2 = 1
    totalsum = 0

    while number2 < end:
        Sum = number1+number2
        number1=number2
        number2=Sum
        if Sum%2==0:
             totalsum+=Sum
    return totalsum
          
print(sequence(4000000))