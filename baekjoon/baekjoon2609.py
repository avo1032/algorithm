[a, b] = list(map(int, input().split()))

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def lcm(x, y, gcd_value):
    return abs(x * y) // gcd_value


gcd_value = gcd(a, b)
lcm_value = lcm(a, b, gcd_value)

print(gcd_value)
print(lcm_value)
