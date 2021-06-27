a = int(input())
sum = []
for i in range(0,a):
    j, k = map(int, input().split())
    sum.append(j+k)

for j in sum:
    print(j)