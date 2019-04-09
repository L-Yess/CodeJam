def solve(x):
	indexes=[]
	s=""
	for i in x:
		if i=='4':
			s+='1'
		else: s+='0'
	num=int(s)
	return num, int(x)-num
	
if __name__ == '__main__':
	t = int(input())
	for x in range(1, t + 1):
		num=input().strip()
		a,b=solve(num)
		print('Case #{}: {} {}'.format(x,a,b))
		

