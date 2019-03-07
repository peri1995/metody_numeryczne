x = int(input('Podaj liczbe: '))
if x == 0:
	silnia = 1
elif x == 1:
	silnia = 1
else:
	tab = [1, 1]
	for i in range(2, x+1):
		tab.append(tab[i - 1]*i)
	silnia = tab[-1]
print(silnia)