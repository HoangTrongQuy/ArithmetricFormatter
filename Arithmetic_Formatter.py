def arithmetic_arranger(a):
    # Processing string: split at " "
    b = a.split()
    lst = []
    for i in b:
        # convert string to int
        if i.isdigit():
            i = int(i)
            lst.append(i)

    for i in b:
        if i == '+':
            print(sumEleAll(lst))
        elif i =='-':
            print(subEleAll(lst))

def sumEleAll(arr):
    # Sum element in array
    sum = 0
    for i in arr:
        sum += i
    return sum

def subEleAll(arr):
    # Subtrace element in array
    sub = 0
    for i in range(len(arr)):
        if i == 0:
            sub += arr[i]
        else: sub -= arr[i]
    return sub

if __name__=='__main__':
    lst = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    for i in lst:
        arithmetic_arranger(i)