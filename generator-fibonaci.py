def fibonacci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b

# Create the fibonacci generator
fib=fibonacci(5)

#Iterate and print the fibonacci numbers
for num in fib:
    print(num)
    
print("Generator Expression")
squares=(x**2 for x in range(5))


# Iterating over the generator
for square in squares:
    print(square)


print("Next In Generator")

def simple_generator():
    yield 1
    yield 2
    yield 3

gen=simple_generator()

print(next(gen))      #output: 1
print(next(gen))      #output: 2
print(next(gen))      #output: 3
