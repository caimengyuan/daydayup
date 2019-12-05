
# test.assert_equals(dig_pow(92, 1), -1)
# test.assert_equals(dig_pow(46288, 3), 51)

def dig_pow(n, p):
    # your code
    l = []
    while n > 0:
        l.append(n%10)
        n = n // 10
    l = l[::-1]
    sum = 0
    for i in range(len(l)):
        sum += l[i] ** p
        p += 1
    print(sum//n if sum%n == 0 else -1)

dig_pow(89, 1)