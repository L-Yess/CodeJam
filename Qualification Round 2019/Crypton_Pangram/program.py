from math import sqrt
import time

chars=[chr(x) for x in range(65,91)]

def factorize(x,N):
	for i in range(3, N, 2):
		if(x%i==0):
			return i, int(x/i)

def solve(liste,N):
	chars=[chr(x) for x in range(65,91)]
	p,q=factorize(liste[0],N)
	factor=p
	if liste[1]%factor!=0: factor==q
	l=[factor]

	for i in liste:
		factor=int(i/factor)
		l.append(factor)
	l2=l
	l = list( dict.fromkeys(l) )
	l.sort()
	d=dict()
	for i in range(len(l)):
		d[l[i]]=chars[i]
	s=""
	for i in l2:
		s+=d[i]
	return s

if __name__ == '__main__':
	t=int(input())
	for x in range(1, t + 1):
		N, L = input().strip().split()
		N=int(N)
		l=input().strip().split()
		for i in range(len(l)):
			l[i]=int(l[i])
		print('Case #{}: {}'.format(x, solve(l,N)))

