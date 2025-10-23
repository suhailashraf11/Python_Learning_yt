# # probleam
# 1. Ask user name;
# 2. ask you ages;
# 3. if user name  start with a or A and ages is above 10 then he can watch movies.
# 4. Then he can watch a movies > yes you can watch.
# 5 Else he cannot watch movies >sorry you cannot watch


for i in range(0, 1):
    user_name = input('enter your name: ')
    user_age = int(input('enter your ages: '))

if (user_name[0] == 'a' or user_name[0]== 'A') and (user_age >=10):
    print(f"You can watch movies in PVR and  your name start with {user_name} and ages {user_age}")
else:
    print(f"You can not watch movies in PVR as your name don't start with a {user_name} and ages is {user_age}")



