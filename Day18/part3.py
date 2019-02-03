# fibonacci in one line


f = (lambda n,fib= [0,1]:fib[:] + [fib.append(fib[-1]+fib[-2]) or fib[-1] for i in range(n-len(fib))])

print(f(10))