nums = [4, 8, 15, 16, 23, 42]
double_nums = [num*2 for num in nums ]

nums = range(11)
squares = [num**2 for num in nums]

nums = [4, 8, 15, 16, 23, 42]
add_ten = [num+10 for num in nums

nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [num/2 for num in nums]

nums = [4, 8, 15, 16, 23, 42]
parity = [num % 2 for num in nums]

names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, "+ name for name in names]

names = ["Elaine", "George", "Jerry", "Cosmo"]  
first_character = [first[0] for first in names]

names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(size) for size in names]


booleans = [True, False, True]
opposite = [not boo for boo in booleans]


names = ["Elaine", "George", "Jerry", "Cosmo"]
is_Jerry = [index=='Jerry' for index in names]

nums = [5, -10, 40, 20, 0]
greater_than_two = [index>2 for index in nums]


nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [i*j for(i,j) in nested_lists]

nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [i>j for i,j in nested_lists]


nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [i[0] for i in nested_lists]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
sums = [i+j for i,j in zip(a,b)]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [j/i for i,j in zip(a,b)]


capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
locations = [i+","+" "+j for i,j in zip(capitals,countries)]


names = ["Jon", "Arya", "Ned"]
ages = [14, 9, 35]
users = ["Name: "+n+", "+"Age: "+str(a) for n,a in zip(names,ages)]

a = [30, 42, 10]
b = [15, 16, 17]
greater_than = [i>j for i,j in zip(a,b)]




