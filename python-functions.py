#1. 

def sum_to(n):
  return n * (n +1)/2

print(sum_to(6))

#2. 

def largest(arg):
  arg.sort()
  return(arg[-1])

print(largest([1, 2, 3, 4, 0]))

#3.   

list = 'fleep floop'

occurrences = list.count('e')
print(occurrences)


#4.

def product(*args):
  total = 1
  for a in args:
    total *= a
  return total

print(product(2, 5, 5))

