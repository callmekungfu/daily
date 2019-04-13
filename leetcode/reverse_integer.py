def reverse(x):
    if x > 2^31 - 1 or x < - 2^31:
        return 0
    num = str(x)
    new_num = ''
    if (num[0] == '-'):
        new_num += '-'
        num = num[1::]
    for i in range(len(num) - 1, -1, -1):
        new_num += num[i]
    return int(new_num)

print(reverse(120))