from time import sleep
from random import choice
lista=[22, 13, 99, 13, 22]
print("[13] Lula")
print("[22] Bolsonaro")
print("[99] Encerrar a votação")
print("\033[31mLula: 0\033[m")
print("\033[32mBolsonaro: 0\033[m")
L=0
B=0
t=0
n=0
while n!=99:
	n=choice(lista)
	if n==13:
		L=L+1
	if n==22:
		B=B+1
	if n==99:
		break
	t=t+1
	print("\033[31mLula: {}\033[m".format(L))
	print("\033[32mBolsonaro: {}\033[m".format(B))
	sleep(3)
print("\033[31mLula: {:.2f}%\033[m".format(L/t*100))
print("\033[32mBolsonaro: {:.2f}%\033[m".format(B/t*100))