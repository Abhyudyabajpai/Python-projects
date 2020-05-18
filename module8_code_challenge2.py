#Contains A
contains_a = lambda word: "a" in word
print contains_a("banana")
print contains_a("apple")
print contains_a("cherry")

#Long string
long_string = lambda x : len(x)>12
print long_string("short")
print long_string("photosynthesis")

#Ends with A
ends_in_a = lambda x : x[-1] == 'a'
print ends_in_a("data")
print ends_in_a("aardvark")

#Double or Zero
double_or_zero = lambda num : num*2 if num > 10 else 0
print double_or_zero(15)
print double_or_zero(5)

#Even/Odd
even_or_odd = lambda num : "even" if num%2==0 else "odd"
print even_or_odd(10)
print even_or_odd(5)

#Multiple of three
multiple_of_three = lambda num: "multiple of three" if num%3 ==0 else "not a multiple"
print multiple_of_three(9)
print multiple_of_three(10)

#Movie rating
rate_movie = lambda rating:"I liked this movie" if rating>8.5 else "This movie was not very good"
print rate_movie(9.2)
print rate_movie(7.2)

#One's Place
ones_place = lambda num: num%10 
print ones_place(123)
print ones_place(4)

#Double Square
double_square = lambda num: 2*(num**2)
print double_square(5)
print double_square(3)

#Add random
import random
add_random = lambda num: num+random.randint(1,10)
print add_random(5)
print add_random(100)

