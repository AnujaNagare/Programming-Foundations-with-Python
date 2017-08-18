# check if entered number is even or odd
a = 5

if a%2 == 0:
	print('even')
else:
	print('odd')
	

# print 'hello' 5 times with for 
seq = [1,2,3,4,5]
for num in seq:
	print('hello')


# use while loop
i = 1

while i < 5:
	print('i is: {}'.format(i))
	i = i + 1 


# use range
for x in range(0,5):
	print(x)

# list range
print(list(range(10)))

# using append
x = [1,2,3,4]
out = []
for num in x:
	out.append(num**2)
	print(out)

# alternative way for list comprehension
print([num**2 for num in x])

# creating a function
def my_func(name = 'Default Name'):
	print('Hello '+name)

# calling function
my_func('Anuja')
my_func()

print(my_func)

# find square of number using function
def square(num):
	"""
	Multiple lines of comment
	"""
	return num**2

output = square(2)

print(output)

# normal function 
def times2(var): return var*2

# written as lambda function 
t = lambda var:var*2
print(t(6))

print(times2(5))
# map()
print(map(times2, seq))
print(list(map(times2,seq)))

print(list(map(lambda var:var*2,seq)))

# using filter
print(list(filter(lambda num:num%2 == 0,seq)))

# lower
s = 'Hello my name is Anuja'
print(s.lower())

#  upper
print(s.upper())

# split
print(s.split())

# tweet split
tweet = 'Go Sports! #Sports'
tweet.split('#')

print(tweet.split('#'))

# using dictionary
d = {'k1':1, 'k2':2}
print(d.keys())
print(d.items())

lst = [1,2,3,4,5]
print(lst.pop())
print(lst)

item = lst.pop()

first = lst.pop(0)
print(lst)

print('x' in [1,2,3])
print('x' in ['x','y','z'])

# tuple unpacking
x = [(1,2), (3,4),(5,6)]

for item in x:
	print(item)

for (a,b) in x:
	print(a)
	print(b)
	











