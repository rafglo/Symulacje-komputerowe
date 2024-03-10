def conversion(x, b):
    if x == 0:
        return "0"
    else:
        result = ""
        while x > 0:
            rem = x % b
            x //= b
            result += str(rem)
        return result[::-1]
    
def reversing(x):
    x_rev = x[::-1]
    return "0." + x_rev

a = reversing(conversion(13,2))

def reconversion(x, b):
    result = 0
    for i in range(2, len(x)):
        result += int(x[i]) * b**(-(int(i)-1))
    return result

print(reconversion(a,2))