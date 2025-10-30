# 1. There is number 1234 add them 1+2+3+4+5 = 15

n = int(input('enter the number: '))
total = 0
for i in str(n):
    total = total + int(i)
print(total)

#
# # method 2
k = input('enter the number: ')
t = 0
i = 0
while i < len(k):
    t = t + int(k[i])
    i+=1
print (t)


