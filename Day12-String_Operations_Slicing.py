print("===++++++++++++++++++ SECTION 1 ++++++++++++++++++===")
'''
Length of a String
We can find the length of a string using len() function.
'''

fruit = "Mango"
len1 = len(fruit)
print("The letter", fruit , "has" , len1 , "Words" )


print("===++++++++++++++++++ SECTION 2 ++++++++++++++++++===")
'''
==================================================================================
String as an array
A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.
'''
pie = "Apple Pie"
print(pie[:5])  #returns character from 0th index to the given index (eg: 5th index)
print(pie[6])	#returns character at specified index

print("======")
print(pie[0])   #A
print(pie[1])   #p
print(pie[2])   #p
print(pie[3])   #l
print(pie[4])   #e
print(pie[5])   #Blank Space
print(pie[6])   #P
print(pie[7])   #i
print(pie[8])   #e


print("===++++++++++++++++++ SECTION 3 ++++++++++++++++++===")
'''
============================================================
String Slicing : This method of specifying the start and end index to specify a part of a string is called slicing.
'''
pie = "Shreyank"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index

print("===++++++++++++++++++ SECTION 4 ++++++++++++++++++===")
'''
Loop through the String : Strings are arrays and arrays are iterable. Thus we can loop through strings.
'''
alphabets = "ABCDE"
for i in alphabets:
    print(i)