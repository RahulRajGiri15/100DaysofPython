friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random
print(random.choice(friends))

l = len(friends)
idx = random.randint(0,len(friends)-1)
print(friends[idx])
print(friends)