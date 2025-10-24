# using if elif else



age = int(input("Enter your age: "))

if age < 3:
    print("Ticket is free")
elif 3 <= age <= 10:
    print("Ticket price is 150")
elif 11 <= age <= 60:
    print("Ticket price is 250")
else:
    print("It’s not safe for you!")



