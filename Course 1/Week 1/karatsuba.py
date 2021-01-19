import math

def karatsuba(num1, num2):
    return karatsuba_recur(num1, num2)

def karatsuba_recur(num1, num2):
    if num1 < 10 or num2 < 10:
        return num1 * num2
    else:
        n = int(math.log10(num1)) + 1
        m = int(math.log10(num2)) + 1
        if n >= m:
            n_over_2 = n // 2
        else:
            n_over_2 = m // 2

        a = num1 // (10**n_over_2)
        b = num1 % (10**n_over_2)
        c = num2 // (10**n_over_2)
        d = num2 % (10**n_over_2)
        print(a,b,c,d)

        ac = karatsuba_recur(a,c)
        bd = karatsuba_recur(b, d)
        ad_bc = karatsuba_recur(a+b, c+d) - ac - bd

        return (10**(n_over_2 * 2) * ac) + (10**(n_over_2) * ad_bc) + bd  


print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592

, 2718281828459045235360287471352662497757247093699959574966967627))