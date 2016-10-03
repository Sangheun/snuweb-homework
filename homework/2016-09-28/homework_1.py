# 1. 구구단
num = int(input("input number: "))
for i in range(1,10):
    result = '{} x {} = {}'.format(num, i, i*num)
    print(result)
