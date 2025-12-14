import random

random_num = random.randint(1,10)
print(random_num)

import  var
print(var.a)

# printing flaot numsbers
random_num_0_to_1 = random.random()*10
print(random_num_0_to_1)

random_float = random.uniform(1,10)
print(random_float)

#printing head and tail

random_head_or_tail = random.randint(0,1)
if(random_head_or_tail == 1): print("head")
else: print("tail")
