# excercise
import random
nums  = int(input('enter the number'))

rand_nums = random.randrange(0, 5)

if nums == rand_nums:
    print(nums, rand_nums , "win")
else:
    print(nums, rand_nums, 'you loss')


