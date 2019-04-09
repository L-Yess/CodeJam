def solve(x):
	res=''
	for i in x:
		if i=='E':
			res+='S'
			continue
		res+='E'
	return res

if __name__ == '__main__':
	t = int(input())
	for x in range(1, t + 1):
		num=int(input().strip())
		string=input().strip()
		print('Case #{}: {}'.format(x,solve(string)))
		