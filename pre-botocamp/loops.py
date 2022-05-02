# 1. Basic - Print all integers from 0 to 150. Hint: use a for loop and range
# for x in range(0, 151):
#     print(x)

# 2. Multiples of Five (Optional) - Print all the multiples of 5 from 5 to 1,000
# for y in range(5,1001,5):
#     print(y)

# 3. Counting, the Dojo Way(Optional) - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for z in range(1,101):
    if z % 10  == 0:
        print("Coding Dojo")
    elif z % 5 == 0:
        print("Coding")
    else:
        print(z)
    