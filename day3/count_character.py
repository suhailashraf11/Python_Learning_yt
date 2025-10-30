# ask a user for name
# example - Suhail Ashraf

name = input('enter the name: ')
temp = " "
i = 0
while i < len(name):
    if name[i] not in temp:
        temp = temp + name[i]
        print(f'{name[i]} : {name.count(name[i])}')

    i = i+1





