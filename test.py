n = 17**987273 # 1.2 million digits number
digits = int(math.log10(n))
k = digits - 24 # i.e. first 24 digits
new_result = n / (10 ** k)
print new_result


a=[1,2,3,4,6,7,99,88,999]
    max= 0
    for i in a:
        if i > max:
            max=i
    print(max)

