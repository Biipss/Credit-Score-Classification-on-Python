#.............ASSIGNMENT..............
#1. Create a list using range(0,10) function.
#2. Transform those elements and store in new lists.
#	i.Square of the elements			(list_sq)
#      ii.Cube of the elements				(list_cube)
#    iii.Multiply all the elements with 10.		(lst_10)
#3.Using List Comprehension

#1
lst=list(range(0,10))
print(lst)

#Using for loop 
#2(i)
print("Using For Loop")
sqr2=[]
cube3=[]
mul10=[]
for val in lst:
    sqr2.append(val**2)
print(sqr2)

for val in lst:
    cube3.append(val**3)
print(cube3)

for val in lst:
    mul10.append(val*10)
print(mul10)

#3.using list comprehension
print("Using List Comprehension")
#3(i)
sqr=[val**2 for val in lst]
print(sqr)

#3(ii)
cube=[val**3 for val in lst]
print(cube)

#3(iii)
mul=[mul*10 for mul in lst]
print(mul)