# 1. Basic - Print all integers from 0 to 150. Hint: use a for loop and range
for x in range(0, 151):
    print(x)

# 2. Multiples of Five (Optional) - Print all the multiples of 5 from 5 to 1,000
for y in range(5,1001,5):
    print(y)

# 3. Counting, the Dojo Way(Optional) - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for z in range(1,101):
    if z % 10  == 0:
        print("Coding Dojo")
    elif z % 5 == 0:
        print("Coding")
    else:
        print(z)

# 4. Whoa. That Sucker's Huge(Optional) - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0;
for a in range(0,500001):
    if a % 2 != 0:
        sum+=a
print(sum);

# 5. Countdown by Fours(Optional) - Print positive numbers starting at 2018, counting down by fours.
for b in range(2018,0,-4):
    print(b);
    
# 6. Flexible Counter (Optional) - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 10
highnum = 255
mult = 5

for c in range(lowNum,highnum):
    if c * mult < highnum:
        print(c * mult)