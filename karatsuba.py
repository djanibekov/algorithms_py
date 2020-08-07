#! works only with equal number of digits of both inputs


def karatsuba(x, y):
	size = len(str(x))
	if(size == 1):
		return x*y

	half = size // 2 
	a = x // 10 ** half
	b = x % 10 ** half
	c = y // 10 ** half
	d = y % 10 ** half

	ac = karatsuba(a, c)
	bd = karatsuba(b, d)
	ad_bc = karatsuba(a+b, c+d) - ac - bd

	return ac * 10 ** size + bd + ad_bc * 10 **half


x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
# print(type(x))
print(karatsuba(x, y))
