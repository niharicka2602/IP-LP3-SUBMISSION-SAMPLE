def factor(input1, input2):
    temp = 0
    for i in range(1, max(input1, input2)+1):
        if input1 % i == input2 % i == 0:
            temp += 1
    print(temp)
    return None

input1 = int(input())
input2 = int(input())
factor(input1, input2)