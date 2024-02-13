lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

num = lower
while num <= upper:
    if num > 1:
        i = 2
        while i < num:
            if (num % i) == 0:
                break
            i += 1
        else:
            print(num)
    num += 1