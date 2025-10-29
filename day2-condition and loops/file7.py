# using if elif else



age = int(input("Enter your age: "))
if age == 0 or age <0:
    print("you cannot  watch or invalid ages")
elif age < 3:
    print("Ticket is free")
elif 3 <= age <= 10:
    print("Ticket price is 150")
elif 11 <= age <= 60:
    print("Ticket price is 250")
else:
    print("It’s not safe for you!")



