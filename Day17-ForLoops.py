'''
Sometimes a programmer wants to execute a group of statements a certain number of times. 
This can be done using loops. Based on this loops are further classified into following main types;

> for loop
> while loop

The for Loop:
for loops can iterate over a sequence of iterable objects in python. 
Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
'''

# name = 'Abhishek'
# for i in name:
#     print(i)
#     if(i=="b"):
#         print("this is something Special!")

# colors = ["Red", "Green", "Blue"]
# for x in colors:
#     print(x)

#     for i in x:
#         print(i)

#----------------------------------------->
#Range function

for k in range(5):
    print(k+1)

print("---")

# range goes from n to n-1
# so if range is from 1 to 20000 it will go from 1 to 19999
for k in range(1,20000):
    print(k)

