# for i in range(3):
#     print(i)
#Output
# 0
# 1
# 2

#===============================>

# print("While Loop")

# i=0
# while(i<=3):
#     print(i)
#     i = i+1
#Output
# 0
# 1
# 2
# 3 

#===============================>
'''
Else with While Loop
We can even use the else statement with the while loop. 
Essentially what the else statement does is that as soon as the while loop condition becomes False, 
the interpreter comes out of the while loop and the else statement is executed.
'''
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')