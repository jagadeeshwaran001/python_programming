#link for problem:-https://www.codechef.com/problems/FLOW002
T = int(input())
for tc in range(T):
	(a, b) = map(int, input().split(' '))
	ans = a%b
	print(ans)