def func(name, *args):
    sum = 0
    
    for i in args:
        sum += i

    
    return sum

result = func("AmiJog", 4, 5, 6, 7)
print(result) 


num = []
for i in range(1, 11):
    num.append(i)

print(num)

#list complision

num1 = [i**2 for i in range(1, 11)]
print(num1)