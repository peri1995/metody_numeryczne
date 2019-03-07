import random
import numpy as np

#x = [-100, 5, -78, -7, 2, 8, -3]
x = random.sample(range(-100, 100), 10)
print(x)
def funkcja(x):
	a = x[0]
	for i in x:
		if i < a:
			a = i
	print(a)
	print(x.index(a))

funkcja(x)