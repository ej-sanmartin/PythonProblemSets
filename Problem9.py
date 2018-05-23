# A pythagorean triplet is a set of three natural numbers, a < b < c, for which
# a**2 + b**2 = c**2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# line 9-10, loops through 1-1000 for the values of a
# and b. Can't be more than 1000 because that is C's
# value, in accordance to the problem
for a in range(1, 1000):
     for b in range(a, 1000):
         # pythagorean theorem
         c = 1000 - a - b
         # Finds c
         if c > 0:
             # Needs to check for this combination once
             # because this instance only happens once
             # for which a + b + c = 1000
             if c*c == a*a + b*b:
                 print (a*b*c)
                 break
             
# Answer: 31875000
