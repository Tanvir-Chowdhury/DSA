import math  # importing math module which contains ceil() and floor()


def karatsuba(x, y):
    if x < 10 and y < 10:  # base cases
        return x * y

    b = int(10)  # base of number
    n = max(len(str(x)), len(str(y)))  # finding max number of digits in both numbers
    m = int(math.ceil(float(n) / 2))  # half number of max digits

    x_h = int(math.floor(x / 10 ** m))  # dividing x into 1st half
    x_l = int(x % (10 ** m))  # dividing x into 2nd half

    y_h = int(math.floor(y / 10 ** m))  # dividing y into 1st half
    y_l = int(y % (10 ** m))  # dividing y into 2nd half

    s1 = karatsuba(x_h, y_h)  # 1st recursive call (step-1)
    s2 = karatsuba(x_l, y_l)  # 2nd recursive call (step-2)
    s3 = karatsuba(x_h + x_l, y_h + y_l)  # 3rd recursive call (step-3)
    s4 = s3 - s2 - s1
    return int(s1 * (b ** (m*2)) + s4 * (b ** m) + s2)  # final output


result = karatsuba(1234, 45678)
print(result)
