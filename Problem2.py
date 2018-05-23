# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms

# Deals with first two numbers in Fibonacci
def F():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

# Rest of Fibonnaci
def SubFib(startNumber, endNumber):
    for cur in F():
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

answer = sum(x for x in SubFib(1, 4000000) if x%2 == 0)

print(answer)

# Answer: 4613732
