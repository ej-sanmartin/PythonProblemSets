# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# My answer (lines 4-12)
# squares of the first 100 natural numbers
a = sum(x**2 for x in range(1,101))

# squares of the sum of the first 100 natural numbers
sumNum = sum(x for x in range(1,101))
b = sumNum**2

# returns a negative value but the difference is the absolute number of the result
print(a - b)


# Another, clever way to answer this question in python
r = range(1, 101)
c = sum(r)
print(c*c - sum(i*i for i in r))

# Answer is 25164150
