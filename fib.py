#
def fib(n): # write Fibonacci series up to n
    '''Print a Fibpnacci series up to n.'''
    a, b = 0, 1
    while a < n:
		# print(a, end=' ')
	    a, b = b, a+b
    print()

s = fib(5)
print(s)
