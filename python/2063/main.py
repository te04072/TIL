# 홀수 n과 n개의 정수를 입력으로 받아 bubble sort로 중간값을 출력

T = int(input())
M = T//2
numbers = list(map(int, input().split())) # map과 split 괄호에 주의
for j in range(T) :
	for k in range(0, T-j-1) :
		if numbers[k] > numbers[k+1] :
			numbers[k], numbers[k+1] = numbers[k+1], numbers[k]
print(numbers[M])