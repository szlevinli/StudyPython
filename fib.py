def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, b, end=' ')
		a, b = b, a + b
	print()

def fib2(n):
	a = 0
	b = 1
	while a < n:
		print(a, b, end=' ')
		a = b
		b = a + b
	print()

